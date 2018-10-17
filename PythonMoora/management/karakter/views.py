from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karakter
# Create your views here.

class ListKarakterView(View):
    def get(self, request):
        template = 'karakter/index.html'
        karakter = Karakter.objects.all()
        data = {
            
            'karakter' : karakter,
        }
        return render(request, template, data)

