from django import forms
from tkinter import Widget
from django.forms import DateInput
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from .models import *
# Create your forms here.

class DKMform(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'type':'email','required':True,}))
    def __init__(self, *args, **kwargs):
        super(DKMform, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['name'].empty_label = '--'
        self.fields['phone'].empty_label = '--'
        self.fields['email'].empty_label = '--'
        self.fields['gender'].empty_label = 'Pilih Gender'
        self.fields['jabatan'].empty_label = 'Pilih Jabatan'
        self.fields['photo'].empty_label = '--'
        self.fields['photo'].required = False
        self.fields['instagram'].required = False
        self.fields['linkedin'].required = False
    class Meta:
        model=DKM
        fields='name','phone','email','gender','photo','instagram','linkedin','jabatan','pengalaman'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'phone':forms.TextInput(attrs={'class':'form-control',}),
            'instagram':forms.URLInput(attrs={'class':'form-control','required':False,}),
            'linkedin':forms.URLInput(attrs={'class':'form-control','required':False,}),
            'pengalaman':forms.Textarea(attrs={'class':'form-control','rows':'2'}),
            'gender':forms.Select(attrs={'class':'form-control','required':True,}),
            'jabatan':forms.Select(attrs={'class':'form-control','id':'relation','required':True,'disabled': 'disabled'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            }
        
class TestimoniForm(ModelForm):
    class Meta:
        model=Testimoni
        fields = 'testimoni',
        widgets={
            'testimoni':forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),
            }
        
        
class PostForm(ModelForm):
    class Meta:
        model=Postingan
        fields = '__all__'
        widgets={
            'judul':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'caption':forms.Textarea(attrs={'class':'form-control', 'rows':'2','required':True,}),
            'post': forms.FileInput(attrs={'class':'form-control'}),
            }
        
class PertanyaanDKMForm(ModelForm):
    class Meta:
        model=Pertanyaan
        fields = 'pertanyaan','jawaban',
        widgets={
            'pertanyaan':forms.Textarea(attrs={'class':'form-control', 'rows':'2','required':True,}),
            'jawaban':forms.Textarea(attrs={'class':'form-control', 'rows':'2','required':True,}),
            }
        
class PertanyaanMhsForm(ModelForm):
    class Meta:
        model=Pertanyaan
        fields = 'nim','nama','pertanyaan'
        widgets={
            'nim':forms.TextInput(attrs={'class':'form-control','placeholder': 'Masukkan NIMmu', 'required':True,}),
            'nama':forms.TextInput(attrs={'class':'form-control','placeholder': 'Masukkan Namamu','required':True,}),
            'pertanyaan':forms.Textarea(attrs={'class':'form-control','placeholder': 'Masukkan Pertanyaanmu', 'rows':'1','required':True,}),
            }