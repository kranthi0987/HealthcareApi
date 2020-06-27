from django.conf.urls import url
from django.urls import path

from apps.patients import views

urlpatterns = [
    path('patient/list/', views.patients_list),
    url(r'^patient/(?P<pk>[0-9]+)$', views.patient_detail),
    path('patientlog/list/', views.patientslog_list),
    url(r'^patientlog/(?P<pk>[0-9]+)$', views.patientslog_detail),
    # url(r'^products/$', views.product_list),
    #     url(r'^products/(?P<pk>[0-9]+)$', views.product_detail),
]
