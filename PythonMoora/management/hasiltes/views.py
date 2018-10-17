from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import HasilTes
# Create your views here.

class ListHasilTesView(View):
    def get(self, request):
        template = 'hasiltes/index.html'
        hasiltes = HasilTes.objects.all()
        data = {
            
            'hasiltes' : hasiltes,
        }
        return render(request, template, data)

