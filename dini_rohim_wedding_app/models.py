from django.db import models

# Create your models here.
class Kehadiran(models.Model):
    KONFIRMASI=(('Hadir','Hadir'),('Tidak Hadir','Tidak Hadir'))
    nama=models.CharField(max_length=50, null=True)
    konfirmasi=models.CharField(max_length=20, choices=KONFIRMASI, null=True)
    jumlah=models.PositiveIntegerField(null=True)
    pesan=models.CharField(max_length=1000, null=True)
    waktu=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nama
    
    
class Undangan(models.Model):
    KETERANGAN=(('Sudah Dikirim','Sudah Dikirim'),('Belum Dikirim','Belum Dikirim'))
    nama=models.CharField(max_length=100, null=True)
    no_wa=models.IntegerField(null=True)
    link=models.CharField(max_length=200, null=True)
    ket=models.CharField(max_length=20, choices=KETERANGAN, null=True, default='Belum Dikirim')
    def __str__(self):
        return self.nama