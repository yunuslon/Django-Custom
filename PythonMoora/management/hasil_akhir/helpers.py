import pandas as pd
import numpy as np
import math
from pandas import DataFrame, read_csv
from orm.models import Kelas,Siswa,HasilTes,Karakter,NilaiAkademik,Plomba
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 


#reportPDF
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='apllication/pdf')
    return None



sw=Siswa.objects.all()

def ListNilaiAkademik(sw):
    if len(sw)>0:
        cols = ['Nilai']
        
        kel ={
            cols[0] : [int(a.nilai_akademiks.nilai) for a in sw],
        }
        dfmt = pd.DataFrame(data=kel)
        return dfmt
    else:
        return[]
def ListHaisilTes(sw):
    if len(sw)>0:
        cols = ['Nilai']
        
        htsm ={
            cols[0] : [int(a.hasiltess.nilai) for a in sw],
        }
        dfhtsm = pd.DataFrame(data=htsm)
        return dfhtsm
    else:
        return[]
def ListKarakter(sw):
    if len(sw)>0:
        cols = ['Nilai']
        
        kar ={
            cols[0] : [int(a.karakters.nilai) for a in sw],
        }
        dfkar = pd.DataFrame(data=kar)
        return dfkar
    else:
        return[]
def ListKelas(sw):
    if len(sw)>0:
        cols = ['Nilai']
        
        kel ={
            cols[0] : [int(a.kelass.nilai) for a in sw],
        }
        dfkel = pd.DataFrame(data=kel)
        return dfkel
    else:
        return[]

def ListPlomba(sw):
    if len(sw)>0:
        cols = ['Nilai']
        
        plb ={
            cols[0] : [int(a.plombas.nilai) for a in sw],
        }
        dfpl = pd.DataFrame(data=plb)
        return dfpl
    else:
        return[]


def Hasil_NilaiAkademikG(sw):
    mt=ListNilaiAkademik(sw)
    b = 0
    tampung=[]
    for y in range(len(sw)):
        a=(math.pow(mt.Nilai[y],2))
        b = b+a
    for i in range(len(sw)):
        s = mt.Nilai[i]
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    NilaiAkademik=pd.DataFrame(data=tampung,columns=['NilaiAkademik'])
    return NilaiAkademik

def HasilTesG(sw):
    htmk=ListHaisilTes(sw)
    b = 0
    tampung=[]
    for y in range(len(sw)):
        a=(math.pow(htmk.Nilai[y],2))
        b = b+a
    for i in range(len(sw)):
        s = htmk.Nilai[i]
        ad=s/(math.sqrt(b))
        tampung.append(ad)

    dfhstmtk=pd.DataFrame(data=tampung,columns=['Hasil Tes'])
    return dfhstmtk

def Hasil_KarakterG(sw):
    kr=ListKarakter(sw)
    b = 0
    tampung=[]
    for y in range(len(sw)):
        a=(math.pow(kr.Nilai[y],2))
        b = b+a
    for i in range(len(sw)):
        s = kr.Nilai[i]
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    Karakter=pd.DataFrame(data=tampung,columns=['Karakter'])
    return Karakter

def Hasil_KelasG(sw):
    kl=ListKelas(sw)
    b = 0
    tampung=[]
    for y in range(len(sw)):
        a=(math.pow(kl.Nilai[y],2))
        b = b+a
    for i in range(len(sw)):
        s = kl.Nilai[i]
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    Kelas=pd.DataFrame(data=tampung,columns=['Kelas'])
    return Kelas

def Hasil_PlombaG(sw):
    plb=ListPlomba(sw)
    b = 0
    tampung=[]
    for y in range(len(sw)):
        a=(math.pow(plb.Nilai[y],2))
        b = b+a
    for i in range(len(sw)):
        s = plb.Nilai[i]
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    Plomba=pd.DataFrame(data=tampung,columns=['Penglaman Lomba'])
    return Plomba

# Matrix Awal

def Matrix_Awal():
    swa={'Nama':[a.nama for a in sw ]}
    dfswa= pd.DataFrame(data=swa)
    na=ListNilaiAkademik(sw)
    krt=ListKarakter(sw)
    pl=ListPlomba(sw)
    ht=ListHaisilTes(sw)
    kl=ListKelas(sw)

    new=pd.concat([dfswa,na,krt,pl,ht,kl],axis=1)
    return new
    
# Gabungan Matrix
    
def Matrix(sw):
    swa={'Nama':[a.nama for a in sw ]}
    dfswa= pd.DataFrame(data=swa)
    na=Hasil_NilaiAkademikG(sw)
    krt=Hasil_KarakterG(sw)
    pl=Hasil_PlombaG(sw)
    htm=HasilTesG(sw)
    hk=Hasil_KelasG(sw)
    
    bna=round(na,4)
    bkrt=round(krt,4)
    bpl=round(pl,4)
    bhtm=round(htm,4)
    bhk=round(hk,4)
        
    new = pd.concat([dfswa,bna,bkrt,bpl,bhtm,bhk],axis=1)
    return new

# Gabungan Pembobobotan
def Pembobotan(sw):
    swa={'Nama':[a.nama for a in sw ]}
    dfswa= pd.DataFrame(data=swa)
    na=Hasil_NilaiAkademikG(sw)*0.25
    krt=Hasil_KarakterG(sw)*0.2
    pl=Hasil_PlombaG(sw)*0.15
    htm=HasilTesG(sw)*0.25
    hk=Hasil_KelasG(sw)*0.15
    
    bna=round(na,4)
    bkrt=round(krt,4)
    bpl=round(pl,4)
    bhtm=round(htm,4)
    bhk=round(hk,4)
        
    new = pd.concat([dfswa,bna,bkrt,bpl,bhtm,bhk],axis=1)
    return new

def Hasil_akhir(sw):
    swa={'Nama':[a.nama for a in sw ]}
    dfswa= pd.DataFrame(data=swa)
    na=Hasil_NilaiAkademikG(sw)*0.25
    krt=Hasil_KarakterG(sw)*0.2
    pl=Hasil_PlombaG(sw)*0.15
    htm=HasilTesG(sw)*0.25
    hk=Hasil_KelasG(sw)*0.15
    pl.columns=['pl']
    htm.columns=['htm']
    Benefit=na.NilaiAkademik+krt.Karakter+pl.pl+htm.htm
    Rangking=Benefit-hk.Kelas
    ra=round(Rangking,4)
    bnf=round(Benefit,4)
    bhk=round(hk,4)
    new =pd.concat([dfswa,bnf,bhk,ra],axis=1)
    new.columns=['Nama','Benefit','Coast','Rangking']
    hasil=new.sort_values(['Rangking'],ascending=[False])
    return hasil