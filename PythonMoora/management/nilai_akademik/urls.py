
from django.conf.urls import url
from management.nilai_akademik import views

urlpatterns = [
    url (r'^$', views.ListNilaiAkademikView.as_view(), name='view'),
    
]