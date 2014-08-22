from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Artigo, Site 

# Create your tests here.

class TesteMordomo(TestCase):
    def setUp(self):
        self.atigo, novo = Artigo.objects.get_or_create(
                username='admin'
                )

        self.site, novo = Pessoa.objects.get_or_create(
                usuario=self.usuario, nome='Maria Anita',
                )
        
    def tearDown(self):
        pass

    def testUmMaisUm(self):
        self.assertEquals(1 + 1, 2)

    def testObjetosCriados(self):
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(Pessoa.objects.count(), 1)
        self.assertEquals(Historico.objects.count(), 1)
