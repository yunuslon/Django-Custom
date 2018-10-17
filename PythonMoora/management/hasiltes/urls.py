
from django.conf.urls import url
from management.hasiltes import views

urlpatterns = [
    url (r'^$', views.ListHasilTesView.as_view(), name='view'),
    

]