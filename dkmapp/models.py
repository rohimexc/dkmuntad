from django.db import models

# Create your models here.
class DKM(models.Model):
    jk=(('male','Laki-laki'),('female','Perempuan'))
    rl=(
        ('inti','inti'),
        ('fasilitator','fasilitator'),
        ('anggota','anggota'),
        )
    st=(('aktif','aktif'),
        ('tidak aktif','tidak aktif')
        )
    jbtn=(('ketua','ketua'),
        ('sekretaris','sekretaris'),
        ('bendahara','bendahara'),
        ('Koordinator Public Relation','Koordinator Public Relation'),
        ('Koordinator Event Organizer','Koordinator Event Organizer'),
        ('Koordinator Creative marketing & Promotion','Koordinator Creative marketing & Promotion'),
        ('PIC Fasilitator FKIP','PIC Fasilitator FKIP'),
        ('PIC Fasilitator FISIP','PIC Fasilitator FISIP'),
        ('PIC Fasilitator FEB','PIC Fasilitator FEB'),
        ('PIC Fasilitator FAHUM','PIC Fasilitator FAHUM'),
        ('PIC Fasilitator FATEK','PIC Fasilitator FATEK'),
        ('PIC Fasilitator FMIPA','PIC Fasilitator FMIPA'),
        ('PIC Fasilitator FAPERTA','PIC Fasilitator FAPERTA'),
        ('PIC Fasilitator FAPETKAN','PIC Fasilitator FAPETKAN'),
        ('PIC Fasilitator FKM','PIC Fasilitator FKM'),
        ('PIC Fasilitator FAHUT','PIC Fasilitator FAHUT'),
        ('Anggota Public Relation','Anggota Public Relation'),
        ('Anggota Event Organizer','Anggota Event Organizer'),
        ('Anggota Creative marketing & Promotion','Anggota Creative marketing & Promotion'),
        ('Fasilitator FKIP','Fasilitator FKIP'),
        ('Fasilitator FISIP','Fasilitator FISIP'),
        ('Fasilitator FEB','Fasilitator FEB'),
        ('Fasilitator FAHUM','Fasilitator FAHUM'),
        ('Fasilitator FATEK','Fasilitator FATEK'),
        ('Fasilitator FMIPA','Fasilitator FMIPA'),
        ('Fasilitator FAPERTA','Fasilitator FAPERTA'),
        ('Fasilitator FAPETKAN','Fasilitator FAPETKAN'),
        ('Fasilitator FKM','Fasilitator FKM'),
        ('Fasilitator FAHUT','Fasilitator FAHUT'),
        )
    id_dkm=models.CharField(max_length=20)
    nim_nidn=models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    email= models.EmailField(null=True,blank=True)
    phone= models.CharField(null=True,max_length=12, blank=True)
    gender= models.CharField(null=True,choices=jk, max_length=12)
    photo=models.ImageField(upload_to='profil',null=True)
    instagram = models.URLField(max_length=100,null=True, blank=True)
    linkedin = models.URLField(max_length=100,null=True, blank=True)
    status=models.CharField(null=True, choices=st, max_length=200,blank=True)
    prodi=models.CharField(max_length=100,null=True, blank=True)
    jabatan=models.CharField(max_length=100, choices=jbtn, null=True, blank=True)
    rating=models.IntegerField(null=True, blank=True)
    pengalaman=models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Testimoni(models.Model):
    nama=models.ForeignKey(DKM, on_delete=models.CASCADE, null=True, blank=True)
    testimoni=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.testimoni
    
    
class Postingan(models.Model):
    judul=models.CharField(max_length=50,null=True)
    caption=models.CharField(max_length=400,null=True)
    post=models.ImageField(upload_to='post',null=True)
    date=models.DateField(auto_created=True, auto_now_add=True)
    def __str__(self):
        return self.judul
    
class Ulasan(models.Model):
    bintang=models.IntegerField(null=True, blank=True)
    ulasan=models.CharField(max_length=200,null=True, blank=True)
    diulas=models.ForeignKey(DKM, on_delete=models.CASCADE)
    def __str__(self):
        return self.ulasan
    
class Pertanyaan(models.Model):
    nim=models.CharField(max_length=9,null=True,blank=True)
    nama=models.CharField(max_length=30,null=True,blank=True)
    pertanyaan=models.CharField(max_length=300,null=True)
    jawaban=models.CharField(max_length=1000,null=True,blank=True)
    pemberi_jawaban=models.ForeignKey(DKM, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.pertanyaan
    
class Nilai_DKM(models.Model):
    dkm=models.ForeignKey(DKM, on_delete=models.CASCADE)
    nilai=models.FloatField(null=True, blank=True, default=5.0)
    def __str__(self):
        return self.dkm.name
    