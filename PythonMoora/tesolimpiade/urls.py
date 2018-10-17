from django.conf.urls import url
from tesolimpiade import views

urlpatterns = [
    url (r'^$', views.ListTesOlimpiadeView.as_view(), name='view'),
    # url (r'^soal$', views.ListTesOlimpiadeSoalView.as_view(), name='soal'),
    # url (r'^add_olimpiade$', views.AddOlimpiadeView.as_view(), name='add_olimpiade'),
]