from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.http import JsonResponse
from dini_rohim_wedding_app.models import *
from dini_rohim_wedding_app.forms import *
from django.db.models import Q,Avg
from django.contrib.auth.models import User
import pandas as pd
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode
from django.urls import reverse
# Create your views here.


def index(request):
    kehadiran = Kehadiran.objects.all().order_by('-id')
    if request.method == 'POST':
        nama = request.POST.get('nama')
        konfirmasi = request.POST.get('status')
        jumlah = request.POST.get('jumlah')
        pesan = request.POST.get('pesan')

        buat_pesan=Kehadiran.objects.create(
            nama=nama,
            jumlah=jumlah,
            konfirmasi=konfirmasi,
            pesan=pesan
        )
        buat_pesan.save()
        messages.success(request,"Pesan Dikirim")
        return redirect('index')
    context={
        'kehadiran':kehadiran,
        }
    return render(request,'dini_rohim_wedding_app/index.html',context)


def data_undangan(request):
    undangan = Undangan.objects.all()
    def generate_url(nama=''):
        url = reverse('index')  # Ganti 'nama_view' dengan nama view Anda
        params = {'n': nama}
        if any(params.values()):  # Cek apakah ada parameter yang tidak kosong
            url += '?' + urlencode({k: v for k, v in params.items() if v})
        return url

    if request.method == 'POST':
        nama = request.POST.get('nama')
        no_wa = request.POST.get('no_wa')
        link = generate_url(nama)
        buat_pesan=Undangan.objects.create(
            nama=nama,
            no_wa=no_wa,
            link=link,
        )
        buat_pesan.save()
        messages.success(request,"Tambah Data Berhasil")
        return redirect('data-undangan')
    context={
        'undangan':undangan,
        }
    return render(request, 'dini_rohim_wedding_app/data-undangan.html',context)