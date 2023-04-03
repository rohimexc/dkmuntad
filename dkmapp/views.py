from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.http import JsonResponse
from dkmapp.models import *
from dkmapp.forms import *
from django.db.models import Q,Avg
from django.contrib.auth.models import User
import pandas as pd
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    dkm=DKM.objects.all()
    post=Postingan.objects.all().order_by('date')
    testimoni=Testimoni.objects.all().order_by('id')
    pertanyaan=Pertanyaan.objects.all().order_by('id')
    data_ketua=[]
    for a in dkm:
        if a.jabatan=='ketua' or a.jabatan=='sekretaris' or a.jabatan == 'bendahara':
            data_ketua.append(a)
        elif 'PIC' in a.jabatan or 'Koordinator' in a.jabatan:
            data_ketua.append(a)
    context={'data_ketua':data_ketua,
             'post':post[:3],
             'pertanyaan':pertanyaan[:2],
             'testimoni':testimoni[:5],
             }
    return render(request,'index.html',context)

def tim(request,id_dkm):
    dkm=DKM.objects.get(id_dkm=id_dkm)
    if "Koordinator" in dkm.jabatan:
        jab_koord=dkm.jabatan
        jab_ang=dkm.jabatan.replace('Koordinator','Anggota')
    elif "PIC" in dkm.jabatan:
        jab_koord=dkm.jabatan
        jab_ang=dkm.jabatan.replace('PIC ','')
    if dkm.jabatan == 'ketua' or dkm.jabatan == 'sekretaris' or dkm.jabatan == 'bendahara':
        data_dkm=DKM.objects.filter(Q(jabatan='ketua')|Q(jabatan='sekretaris')|Q(jabatan='bendahara'))
        testimoni_tim=Testimoni.objects.filter(Q(nama__jabatan='ketua')|Q(nama__jabatan='sekretaris')|Q(nama__jabatan='bendahara'))
        nama_tim='Inti'
    else:
        data_dkm=DKM.objects.filter(Q(jabatan=jab_koord)|Q(jabatan=jab_ang))
        testimoni_tim= Testimoni.objects.filter(Q(nama__jabatan=jab_koord)|Q(nama__jabatan=jab_ang))
        nama_tim=jab_koord.split()
        nama_tim = nama_tim[1:]
        nama_tim = ' '.join(nama_tim)
    context={'dkm':data_dkm, 'testimoni':testimoni_tim, 'nama_tim':nama_tim}
    return render(request, 'tim.html', context)

def faq(request):
    form=PertanyaanMhsForm()
    pertanyaan=Pertanyaan.objects.all()
    if request.method == 'POST':
        form=PertanyaanMhsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pertanyaan Diajukan')
        return redirect('faq')
    context={'form':form, 'pertanyaan':pertanyaan}
    return render(request,'faq.html',context)

@login_required(login_url='database')
def data_testimoni(request):
    form=TestimoniForm()
    if request.method == 'POST':
        form=TestimoniForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.nama=DKM.objects.get(id_dkm=request.user)
            f.save()
            messages.success(request, 'Data Berhasil Disimpan')
        return redirect('data-testimoni')
    data_testimoni=Testimoni.objects.all()
    context={'data_testimoni':data_testimoni, 'form':form}
    return render(request,'dkmapp/data_testimoni.html',context)

@login_required(login_url='database')
def edit_testimoni(request,id):
    testimoni=Testimoni.objects.get(id=id)
    form=TestimoniForm(instance=testimoni)
    if request.method == 'POST':
        form=TestimoniForm(request.POST,instance=testimoni)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Disimpan')
        return redirect('data-testimoni')
    context={'form':form}
    return render(request,'dkmapp/edit.html',context)

@login_required(login_url='database')
def hapus_testimoni(request,id):
    testimoni=Testimoni.objects.get(id=id)
    if request.method == 'POST':
        testimoni.delete()
    return redirect('data-testimoni')
    
@login_required(login_url='database')
def data_post(request):
    form=PostForm()
    if request.method == 'POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Disimpan')
            return redirect('data-post')
    data_post=Postingan.objects.all()
    context={'data_post':data_post, 'form':form}
    return render(request,'dkmapp/data_post.html',context)

@login_required(login_url='database')
def edit_post(request,id):
    post=Postingan.objects.get(id=id)
    form=PostForm(instance=post)
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Disimpan')
        return redirect('data-post')
    context={'form':form}
    return render(request,'dkmapp/edit.html',context)

@login_required(login_url='database')
def hapus_post(request,id):
    post=Postingan.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
    return redirect('data-post')

@login_required(login_url='database')
def data_pertanyaan(request):
    form=PertanyaanDKMForm()
    dkm=DKM.objects.get(id_dkm=request.user)
    if request.method == 'POST':
        form=PertanyaanDKMForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.nama='user'
            f.nim='user'
            f.pemberi_jawaban=DKM.objects.get(id_dkm=request.user)
            f.save()
            average_rating_dkm = Ulasan.objects.filter(diulas__id_dkm=request.user).aggregate(Avg('bintang'))
            jumlah_pertanyaan_dijawab = Pertanyaan.objects.filter(pemberi_jawaban__id_dkm=request.user).count()
            jumlah_pertanyaan=Pertanyaan.objects.all().count()
            point_pertanyaan=jumlah_pertanyaan_dijawab/jumlah_pertanyaan
            try:
                rate_dkm=(average_rating_dkm['bintang__avg'] + point_pertanyaan + 3)/1.8
            except:
                rate_dkm=(0 + point_pertanyaan + 3)/1.8
            rate_dkm_int=int(round(rate_dkm,0))
            dkm.rating=rate_dkm_int
            dkm.save()
            messages.success(request, 'Data Berhasil Disimpan')
        return redirect('data-pertanyaan')
    data_pertanyaan=Pertanyaan.objects.all()
    context={'data_pertanyaan':data_pertanyaan, 'form':form}
    return render(request,'dkmapp/data_pertanyaan.html',context)

@login_required(login_url='database')
def edit_pertanyaan(request,id):
    pertanyaan=Pertanyaan.objects.get(id=id)
    form=PertanyaanDKMForm(instance=pertanyaan)
    dkm=DKM.objects.get(id_dkm=request.user)
    if request.method == 'POST':
        form=PertanyaanDKMForm(request.POST,instance=pertanyaan)
        if form.is_valid():
            f=form.save(commit=False)
            f.pemberi_jawaban=DKM.objects.get(id_dkm=request.user)
            f.save()
            average_rating_dkm = Ulasan.objects.filter(diulas__id_dkm=request.user).aggregate(Avg('bintang'))
            jumlah_pertanyaan_dijawab = Pertanyaan.objects.filter(pemberi_jawaban__id_dkm=request.user).count()
            jumlah_pertanyaan=Pertanyaan.objects.all().count()
            point_pertanyaan=jumlah_pertanyaan_dijawab/jumlah_pertanyaan
            try:
                rate_dkm=(average_rating_dkm['bintang__avg'] + point_pertanyaan + 3)/1.8
            except:
                rate_dkm=(0 + point_pertanyaan + 3)/1.8
            rate_dkm_int=int(round(rate_dkm,0))
            dkm.rating=rate_dkm_int
            dkm.save()
            messages.success(request, 'Data Berhasil Disimpan')
        return redirect('data-pertanyaan')
    context={'form':form}
    return render(request,'dkmapp/edit.html',context)

@login_required(login_url='database')
def hapus_pertanyaan(request,id):
    pertanyaan=Pertanyaan.objects.get(id=id)
    dkm=DKM.objects.get(id_dkm=request.user)
    if request.method == 'POST':
        pertanyaan.delete()
        average_rating_dkm = Ulasan.objects.filter(diulas__id_dkm=request.user).aggregate(Avg('bintang'))
        jumlah_pertanyaan_dijawab = Pertanyaan.objects.filter(pemberi_jawaban__id_dkm=request.user).count()
        jumlah_pertanyaan=Pertanyaan.objects.all().count()
        point_pertanyaan=jumlah_pertanyaan_dijawab/jumlah_pertanyaan
        try:
            rate_dkm=(average_rating_dkm['bintang__avg'] + point_pertanyaan + 3)/1.8
        except:
            rate_dkm=(0 + point_pertanyaan + 3)/1.8
        rate_dkm_int=int(round(rate_dkm,0))
        dkm.rating=rate_dkm_int
        dkm.save()
    return redirect('data-pertanyaan')

def database(request):
    data_dkm=DKM.objects.all()
    id_dkm=request.user
    form = DKMform()
    if request.method == 'POST':
        id_dkm = request.POST.get('subject')
        if data_dkm.filter(id_dkm=id_dkm).exists():
            dkm = DKM.objects.get(id_dkm=id_dkm)
            if "Koordinator" in dkm.jabatan:
                jab_koord=dkm.jabatan
                jab_ang=dkm.jabatan.replace('Koordinator','Anggota')
            elif "Anggota" in dkm.jabatan:
                jab_koord=dkm.jabatan.replace('Anggota','Koordinator')
                jab_ang=dkm.jabatan
            elif "PIC" in dkm.jabatan:
                jab_koord=dkm.jabatan
                jab_ang=dkm.jabatan.replace('PIC ','')
            else:
                jab_koord=dkm.jabatan.replace('Fasilitator','PIC Fasilitator')
                jab_ang=dkm.jabatan
            if dkm.jabatan == 'ketua' or dkm.jabatan == 'sekretaris' or dkm.jabatan == 'bendahara':
                data_dkm=DKM.objects.filter(Q(jabatan='ketua')|Q(jabatan='sekretaris')|Q(jabatan='bendahara'))
            else:
                data_dkm=DKM.objects.filter(Q(jabatan=jab_koord)|Q(jabatan=jab_ang))
            user = authenticate(username=id_dkm, password='@DKMcompletepassword123')
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {dkm}.")
        else:
            dkm=None
            messages.error(request,'ID DKM kamu salah/tidak terdaftar')
    try:
        dkm = DKM.objects.get(id_dkm=id_dkm)
        if "Koordinator" in dkm.jabatan:
            jab_koord=dkm.jabatan
            jab_ang=dkm.jabatan.replace('Koordinator','Anggota')
        elif "Anggota" in dkm.jabatan:
            jab_koord=dkm.jabatan.replace('Anggota','Koordinator')
            jab_ang=dkm.jabatan
        elif "PIC" in dkm.jabatan:
            jab_koord=dkm.jabatan
            jab_ang=dkm.jabatan.replace('PIC ','')
        else:
            jab_koord=dkm.jabatan.replace('Fasilitator','PIC Fasilitator')
            jab_ang=dkm.jabatan
            
        if dkm.jabatan == 'ketua' or dkm.jabatan == 'sekretaris' or dkm.jabatan == 'bendahara':
            data_dkm=DKM.objects.filter(Q(jabatan='ketua')|Q(jabatan='sekretaris')|Q(jabatan='bendahara'))
        else:
            data_dkm=DKM.objects.filter(Q(jabatan=jab_koord)|Q(jabatan=jab_ang))   
    
    except:
        messages.info(request, "ID DKM kamu salah/tidak terdaftar")
        return redirect('index')
    context={'dkm':data_dkm,'form':form}
    return render(request, 'dkmapp/database.html', context)

def edit(request,id_dkm):
    dkm = DKM.objects.get(id_dkm=id_dkm)
    form=DKMform(instance=dkm)
    if request.method == 'POST':
        form=DKMform(instance=dkm, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Data berhasil disimpan')
            return redirect('database')
    context={'form':form}
    return render(request, 'dkmapp/edit.html', context)   
    
def logoutpage(request):
    logout(request)
    return redirect('index')

def refresh(request):
    dkm=DKM.objects.all()
    dkm.delete()
    sheet_id="1VVJOjD2xWPKL6fqDC3eHF6lnae0bqze7ArIJV7HTmGE"
    df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv",usecols = ['NAMA UPPER','NO WA D&M','Email Address','NIM/NIDN','ID','PRODI'])
    # Loop through the rows of the DataFrame and create instances of MyModel
    for index, row in df.iterrows():
        instance = DKM(name=row['NAMA UPPER'],
                       phone=row['NO WA D&M'],
                       email=row['Email Address'],
                       nim_nidn=row['NIM/NIDN'],
                       id_dkm=row['ID'],
                        prodi=row['PRODI'],
                        status='aktif',
                        gender='female'
                        )
        instance.save()
        new_user = User.objects.create_user(
        username=instance.id_dkm,
        email=instance.email,
        password='@DKMcompletepassword123'
        )
        new_user.save()
        messages.success(request,"Berhasil Refresh Data")
    return redirect('database')

def profile (request,id_dkm):
    dkm=DKM.objects.get(id_dkm=id_dkm)
    context={'dkm':dkm}
    return render(request,'profile.html', context)

def ulasan (request, id_dkm):
    dkm=DKM.objects.get(id_dkm=id_dkm)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        print(rating)
        print(comment)
        buat_ulasan=Ulasan.objects.create(
          bintang=rating,
          ulasan=comment,
          diulas=dkm 
        )
        buat_ulasan.save()
        average_rating_dkm = Ulasan.objects.filter(diulas__id_dkm=id_dkm).aggregate(Avg('bintang'))
        jumlah_pertanyaan_dijawab = Pertanyaan.objects.filter(pemberi_jawaban__id_dkm=id_dkm).count()
        jumlah_pertanyaan=Pertanyaan.objects.all().count()
        point_pertanyaan=jumlah_pertanyaan_dijawab/jumlah_pertanyaan
        rate_dkm=(average_rating_dkm['bintang__avg'] + point_pertanyaan + 3)/1.8
        rate_dkm_int=int(round(rate_dkm,0))
        dkm.rating=rate_dkm_int
        dkm.save()
        messages.success(request,"Ulasan Dikirim")
    return redirect('index')
    