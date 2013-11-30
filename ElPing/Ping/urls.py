from django.conf.urls import patterns, url

from Ping import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='Ping'),
    url(r'^Busqueda/$', views.Busqueda, name='Busqueda'),
)
