from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import NilaiAkademik
# Create your views here.

class ListNilaiAkademikView(View):
    def get(self, request):
        template = 'nilai_akademik/index.html'
        nilai_akademik = NilaiAkademik.objects.all()
        data = {
            
            'nilai_akademik' : nilai_akademik,
        }
        return render(request, template, data)

