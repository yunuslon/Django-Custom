"""PythonMoora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from app.config import setting
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/', include('login.urls', namespace='login')),
    # url(r'^', views.LoginView.as_view(), name='login'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^dologin/$', views.AksiLoginView.as_view(), name='dologin'),
    url(r'^dologout/$', views.AksiLogoutView.as_view(), name='dologout'),

    url(r'^siswa/', include('management.siswa.urls', namespace='siswa')),
    url(r'^kelas/', include('management.kelas.urls', namespace='kelas')),
    url(r'^hasiltes/', include('management.hasiltes.urls', namespace='hasiltes')),
    url(r'^nilai_akademik/', include('management.nilai_akademik.urls', namespace='nilai_akademik')),
    url(r'^karakter/', include('management.karakter.urls', namespace='karakter')),
    url(r'^plomba/', include('management.plomba.urls', namespace='plomba')),
    url(r'^hasil_akhir/', include('management.hasil_akhir.urls', namespace='hasil_akhir')),
    url(r'^tesolimpiade/', include('tesolimpiade.urls', namespace='tesolimpiade')),

]

urlpatterns +=  staticfiles_urlpatterns()
urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)