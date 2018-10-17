from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import TesOlimpiade
from django.contrib.auth.mixins import LoginRequiredMixin
from tesolimpiade import helpers
# Create your views here.

class HarusLogin(LoginRequiredMixin):
    login_url = '/login/'



def getTotalSoal():
    label = []
    data = []
    cball = TesOlimpiade.objects.all()
    for cr in cball:
        label.append(cr.pertayaan)
        c = len(TesOlimpiade.objects.filter(pertayaan=cr.pertayaan))
        data.append(c)
    lc = helpers.HelpersSoal(label, data)
    return lc

class ListTesOlimpiadeView(HarusLogin,View):
    template_name = 'tesolimpiade/index.html'
    def get(self, request):
        tesolimpiade = TesOlimpiade.objects.all()
        soal = [tesolimpiade.pertayaan for tesolimpiade in TesOlimpiade.objects.all()]
        panjang =  [tesolimpiade.pertayaan for tesolimpiade in TesOlimpiade.objects.all()]
        # soal = [tesolimpiade.count() for olim in Club.objects.all()]
        data = {
        	'tesolimpiade2' : tesolimpiade,
            'TotalSoal' : getTotalSoal(),
            'tesolimpiade': {
                'total': TesOlimpiade.objects.all().count()

                # 'soal_total': TesOlimpiade.objects.filter(pertayaan='pertayaan').count()
            },
            
        }
        
        return render(request, self.template_name, data)

# class ListTesOlimpiadeSoalView(HarusLogin,View):
#     template_name = 'tesolimpiade/index.html'
#     def get(self, request):
#         tesolimpiade = TesOlimpiade.objects.all()
#         data = {
            
#             'tesolimpiade2' : tesolimpiade
#         }
#         return render(request, self.template_name, data)


