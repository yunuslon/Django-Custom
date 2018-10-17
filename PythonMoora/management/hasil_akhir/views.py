from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karakter,NilaiAkademik,HasilTes,Siswa,Plomba,Kelas
from management.hasil_akhir import helpers
from reportlab.pdfgen import canvas
from django.template.loader import get_template

# Create your views here.

class ListMatrixAwalView(View):
    def get(self, request):
        template = 'hasil_akhir/nilai_awal.html'
        nl = helpers.Matrix_Awal().as_matrix()
        data = {
            'nl' : nl,
        }
        return render(request, template, data)

class ListMatrixView(View):
    def get(self, request):
        template = 'hasil_akhir/index.html'
        sw = Siswa.objects.all()
        nl = helpers.Matrix(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        return render(request, template, data)

class ListPembobotanView(View):
    def get(self, request):
        template = 'hasil_akhir/hasil_pembobotan.html'
        sw = Siswa.objects.all()
        nl = helpers.Pembobotan(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        return render(request, template, data)

class ListRangkingView(View):
    def get(self, request):
        template = 'hasil_akhir/rangking.html'
        sw = Siswa.objects.all()
        nl = helpers.Hasil_akhir(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        return render(request, template, data)

        # view untuk Report
        
class GeneratePDFtbl(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hasil_akhir/reporttbl.html')
        sw = Siswa.objects.all()
        nl = helpers.Matrix(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('hasil_akhir/reporttbl.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFnilai_awal(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hasil_akhir/reportnilai_awal.html')
        sw = Siswa.objects.all()
        nl = helpers.Matrix_Awal().as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('hasil_akhir/reportnilai_awal.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFpembobotan(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hasil_akhir/report_pembobotan.html')
        sw = Siswa.objects.all()
        nl = helpers.Pembobotan(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('hasil_akhir/report_pembobotan.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFrangking(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hasil_akhir/report_rangking.html')
        sw = Siswa.objects.all()
        nl = helpers.Hasil_akhir(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('hasil_akhir/report_rangking.html', data)
        return HttpResponse(pdf, content_type='application/pdf')