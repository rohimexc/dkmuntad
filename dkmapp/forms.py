from django import forms
from tkinter import Widget
from django.forms import DateInput
from django.forms import ModelForm
from .models import *
# Create your forms here.

class DKMform(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'type':'email','required':True,}))
    class Meta:
        model=DKM
        fields='name','phone','email','gender','photo','instagram','linkedin','pengalaman',
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'phone':forms.TextInput(attrs={'class':'form-control',}),
            'instagram':forms.URLInput(attrs={'class':'form-control','required':False,}),
            'linkedin':forms.URLInput(attrs={'class':'form-control','required':False,}),
            'pengalaman':forms.Textarea(attrs={'class':'form-control','rows':'2'}),
            'gender':forms.Select(attrs={'class':'form-control','required':True,}),
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