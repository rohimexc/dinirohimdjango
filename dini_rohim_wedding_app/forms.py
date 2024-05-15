from django import forms
from tkinter import Widget
from django.forms import DateInput
from django.forms import ModelForm
from .models import *


class Kehadiranform(ModelForm):
    class Meta:
        model=Kehadiran
        fields='nama','jumlah','konfirmasi','pesan',
        widgets={
            'nama':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'jumlah':forms.TextInput(attrs={'class':'form-control','type':'number', 'required':True,}),
            'konfirmasi':forms.Select(attrs={'class':'form-control','required':True,}),
            'pesan':forms.TextInput(attrs={'class':'form-control','required':True,}),
            }
        
