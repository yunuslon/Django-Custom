from django.db import models
from django.contrib.auth.models import User
import time
import os
from orm import FileUploader

class Siswa(models.Model):
    
    nama = models.CharField(max_length=100, blank=True, null=True)
    PRIA = 'PR'
    WANITA = 'WN'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),
    )
    jenis_kelamin = models.CharField(
        max_length=2,
        choices=JK_CHOICES,
        default=PRIA,
    )
    alamat = models.TextField(blank=True, null=True)
    tanggal_lahir = models.DateField(auto_now=False, auto_now_add=False)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'Siswa'
        ordering = ['id']

class NilaiAkademik(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='nilai_akademiks', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Nilai_Akademik'
        ordering = ['id']

class HasilTes(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='hasiltess', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'HasilTes'
        ordering = ['id']

class Kelas(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='kelass', blank=True, null=True)   
    jenjang = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

  
    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Kelas'
        ordering = ['id']


class Karakter(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='karakters', blank=True, null=True)
    sikap = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Karakter'
        ordering = ['id']

class Plomba(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='plombas', blank=True, null=True)
    intensitas = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Plomba'
        ordering = ['id']

class TesOlimpiade(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tesolimpiades')
    no = models.IntegerField(default=0)
    gambar = models.ImageField(upload_to="gambar",
                             null=True,
                             blank=True,
                             help_text="Upload Foto Soal Anda",
                             default="../media/gambar/a.png"
                             )

    pertayaan = models.TextField(blank=True, null=True)
    jawabanA = models.CharField(max_length=200, blank=True, null=True)
    jawabanB = models.CharField(max_length=200, blank=True, null=True)
    jawabanC = models.CharField(max_length=200, blank=True, null=True)
    jawabanD = models.CharField(max_length=200, blank=True, null=True)
    jawabanE = models.CharField(max_length=200, blank=True, null=True)
    kunci = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.pertayaan

    class Meta:
        db_table = 'TesOlimpiade'
        ordering = ['id']

