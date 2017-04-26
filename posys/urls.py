from django.conf.urls import patterns, url, include
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
    url(r'^$', 'views.home', name='home'),
                       # url(r'^posys/', include('posys.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       url(r'^academico/', include('academico.urls')),
                       url(r'^noticias/', include('noticias.urls')),
                       url(r'^contato/$', 'views.contato'),

                       url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       )
