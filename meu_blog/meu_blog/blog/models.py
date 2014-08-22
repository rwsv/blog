from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
# from django.contrib.sites.models import Site


class Artigo(models.Model):
    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(
        default=datetime.now,
        blank=True
    )
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse(
                'meu_blog.blog.views.artigo',
                kwargs={'slug': self.slug}
                )


class Site(models.Model):
    pass

# SIGNALS
from django.db.models import signals
from utils.signals_comuns import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Artigo)
