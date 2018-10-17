from django.conf.urls import url
from management.hasil_akhir import views

urlpatterns = [
    url (r'^$', views.ListMatrixView.as_view(), name='view'),
    url (r'^pembobotan$', views.ListPembobotanView.as_view(), name='pembobotan'),
    url (r'^rangking$', views.ListRangkingView.as_view(), name='rangking'),
    url (r'^nilai_awal$', views.ListMatrixAwalView.as_view(), name='nilai_awal'),

    # Report
    url (r'^reporttbl$', views.GeneratePDFtbl.as_view(), name='reporttbl'),
    url (r'^reportnilai_awal$', views.GeneratePDFnilai_awal.as_view(), name='reportnilai_awal'),
    url (r'^report_pembobotan$', views.GeneratePDFpembobotan.as_view(), name='report_pembobotan'),
    url (r'^report_rangking$', views.GeneratePDFrangking.as_view(), name='report_rangking'),

]