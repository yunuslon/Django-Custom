from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Siswa
# Create your views here.

class ListSiswaView(View):
    def get(self, request):
        template = 'siswa/index.html'
        siswa = Siswa.objects.all()
        data = {
            
            'siswa' : siswa,
        }
        return render(request, template, data)