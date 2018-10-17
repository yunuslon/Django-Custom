
from django.conf.urls import url
from management.siswa import views

urlpatterns = [
    url (r'^$', views.ListSiswaView.as_view(), name='view'),
]