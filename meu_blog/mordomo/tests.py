"""
Criar um comando para verificar se estah tudo ok na pagina
principal do site e enviar um e-mail caso algum erro foi
encontrado.

    >>> from mordomo.models import verificar_pagina_inicial
Simulando status 200 - estado ok

    >>> def status_code_ok(url):
    ...    return 200

    >>> verificar_pagina_inicial(
    ... funcao_status_code=status_code_ok
    ... )
    True

    >>> from django.core import mail
    >>> len(mail.outbox)
    0

Simulando status 500 - estado de erro que envia e-mail

    >>> def status_code_500(url):
    ...    return 500

    >>> verificar_pagina_inicial(
    ... funcao_status_code=status_code_500
    ... )
    True

    >>> len(mail.outbox)
    1
"""
import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from contas.models import Pessoa, Historico, ContaPagar, \
        CONTA_STATUS_APAGAR, CONTA_STATUS_PAGO

# Create your tests here.


class TesteMordomo(TestCase):
    def setUp(self):
        self.usuario, novo = User.objects.get_or_create(
                username='admin'
                )
        self.pessoa, novo = Pessoa.objects.get_or_create(
                usuario=self.usuario, nome='Maria Anita',
                )
        self.historico, novo = Historico.objects.get_or_create(
                usuario=self.usuario, descricao='Agua',
                )

    def tearDown(self):
        pass

    def test_um_mais_um(self):
        self.assertEquals(1 + 1, 2)

    def test_objetos_criados(self):
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(Pessoa.objects.count(), 1)
        self.assertEquals(Historico.objects.count(), 1)

    def test_contas_pendentes(self):
        from mordomo.models import obter_contas_pendentes, \
                enviar_contas_pendentes

        for numero in range(-50, 50):
            if numero % 2:
                novo_status = CONTA_STATUS_APAGAR
            else:
                novo_status = CONTA_STATUS_PAGO

            nova_data = datetime.date.today() + \
                    datetime.timedelta(days=numero)

            novo_valor = numero + 70

            ContaPagar.objects.create(
                    usuario=self.usuario,
                    pessoa=self.pessoa,
                    historico=self.historico,
                    data_vencimento=nova_data,
                    valor=novo_valor,
                    status=novo_status,
                    )

        self.assertEquals(ContaPagar.objects.count(), 100)

        contas_pendentes = obter_contas_pendentes(
                usuario=self.usuario,
                prazo_dias=10,
                )

        self.assertEquals(contas_pendentes.count(), 30)

        enviar_contas_pendentes(
                usuario=self.usuario,
                prazo_dias=10,
                )

        from django.core import mail
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(
                mail.outbox[0].subject, 'Contas a pagar e receber'
                )
