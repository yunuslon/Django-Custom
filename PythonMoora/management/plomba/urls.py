
from django.conf.urls import url
from management.plomba import views

urlpatterns = [
    url (r'^$', views.ListPlombaView.as_view(), name='view'),
   
]