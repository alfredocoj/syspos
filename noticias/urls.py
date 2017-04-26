from django.conf.urls import patterns, url, include

from noticias.models import Artigo

from noticias.feeds import UltimosArtigos

urlpatterns = patterns('',
                       url(r'^$', 'noticias.views.home', name='home'),
                       #url(r'^$', 'django.views.generic.date_based.archive_index',{'queryset': Artigo.objects.all(),'date_field': 'publicacao'}),
	url(r'^rss/ultimos/$', UltimosArtigos()),
                       url(r'^artigos/(?P<artigos_id>\d+)/$', 'noticias.views.ver_artigos'),
                       url(r'^artigos/', 'noticias.views.listar_artigos'),
                       )
