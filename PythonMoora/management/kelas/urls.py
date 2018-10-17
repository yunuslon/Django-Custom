
from django.conf.urls import url
from management.kelas import views

urlpatterns = [
    url (r'^$', views.ListKelasView.as_view(), name='view'),
   

]