from django.conf.urls import url
from scrumpy import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^proyectos/$', views.lista_proyectos),
    url(r'^proyecto/(?P<pk>[0-9]+)/$', views.proyecto),
]
