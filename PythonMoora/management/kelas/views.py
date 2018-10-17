from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Kelas
# Create your views here.

class ListKelasView(View):
    def get(self, request):
        template = 'kelas/index.html'
        kelas = Kelas.objects.all()
        data = {
            
            'kelas' : kelas,
        }
        return render(request, template, data)

