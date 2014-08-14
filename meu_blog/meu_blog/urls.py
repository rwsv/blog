from django.conf.urls import patterns, include, url
from django.views.generic.dates import ArchiveIndexView

from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo
from blog.feeds import UltimosArtigos

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'meu_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$', ArchiveIndexView.as_view(**{'queryset': Artigo.objects.all(), 'date_field': 'publicacao'})),

    url(r'^admin/', include(admin.site.urls)),

    (r'^rss/ultimos/$', UltimosArtigos()),
    (r'^artigo/(?P<artigo_id>\d+)/$', 'meu_blog.blog.views.artigo'),
)
