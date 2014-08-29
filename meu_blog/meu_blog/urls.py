from django.conf.urls import patterns, include, url
from django.conf import settings
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
    (r'^artigo/(?P<slug>[\w_-]+)/$', 'meu_blog.blog.views.artigo'),

    (r'^media/(.*)$', 'django.views.static.serve',
                      {'document_root': settings.MEDIA_ROOT}),
    (r'^contato/$', 'views.contato'),
    (r'^comments/', include('django_comments.urls')),
    (r'^galeria/', include('galeria.urls')),
    (r'^contas/', include('contas.urls')),
    (r'^entrar/$',
      'django.contrib.auth.views.login',
     {'template_name': 'entrar.html'}, 'entrar'),
    (r'^sair/$',
      'django.contrib.auth.views.logout',
     {'template_name': 'sair.html'}, 'sair'),
    (r'^registrar/$', 'views.registrar', {}, 'registrar'),
    (r'^todos_os_usuarios/$', 'views.todos_os_usuarios', {}, 'todos_os_usuarios'),
    (r'^mudar_senha/$',
        'django.contrib.auth.views.password_change',
       {'template_name': 'mudar_senha.html'},
        'mudar_senha'),
    (r'^mudar_senha/concluido/$',
        'django.contrib.auth.views.password_change_done',
       {'template_name': 'mudar_senha_concluido.html'},
        'mudar_senha_concluido'),
    )
