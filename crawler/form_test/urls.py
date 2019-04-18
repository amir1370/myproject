from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'contact/$', views.get_form, name= 'contact'),
    url(r'thanks/$', views.get_form),
]