
from django.conf.urls import url
from management.karakter import views

urlpatterns = [
    url (r'^$', views.ListKarakterView.as_view(), name='view'),
   
   

]