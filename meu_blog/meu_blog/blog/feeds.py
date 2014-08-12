from django.contrib.syndication.views import Feed
from meu_blog.blog.models import Artigo


class UltimosArtigos(Feed):
    title = 'Ultimos artigos do blog do Ramon'
    link = '/'

    def items(self):
        return Artigo.objects.all()

'''    def item_link(self, artigo):
        return '/artigo/%d/' % artigo.id '''
