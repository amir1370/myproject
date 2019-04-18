from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'vehicles/$', views.car_list)
]
