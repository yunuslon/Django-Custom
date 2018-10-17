from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Plomba
from management.plomba import helpers
# Create your views here.

class ListPlombaView(View):
    def get(self, request):
        template = 'plomba/index.html'
        plomba = Plomba.objects.all()
        data = {
            
            'plomba' : plomba,
        }
        return render(request, template, data)

