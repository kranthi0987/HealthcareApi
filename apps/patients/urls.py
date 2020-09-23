from django.conf.urls import url
from django.urls import path

from apps.patients import views

urlpatterns = [
    path('patient/list/', views.patients_list),
    path('patient/listbyid/', views.patient_list_byid),
    path('patient/count/', views.patient_count),
    url(r'^patient/(?P<pk>[0-9]+)$', views.patient_detail),
    path('patientlog/add/', views.patientslog_post_byid),
    path('patientlog/listbyid/', views.patientslog_list_byid),
    url(r'^patientlog/(?P<pk>[0-9]+)$', views.patientslog_detail),
    # url(r'^products/$', views.product_list),
    #     url(r'^products/(?P<pk>[0-9]+)$', views.product_detail),
]