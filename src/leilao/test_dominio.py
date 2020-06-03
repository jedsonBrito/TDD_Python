from unittest import TestCase

from src.leilao.dominio import Leilao, Lance, Usuario, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        jedi = Usuario("Jedi")
        sith = Usuario("Sith")

        lance_do_sith = Lance(sith, 100)
        lance_do_jedi = Lance(jedi, 150)

        leilao_corruscant = Leilao("Celular")

        leilao_corruscant.lances.append(lance_do_sith)
        leilao_corruscant.lances.append(lance_do_jedi)


        avaliacao = Avaliador()
        avaliacao.avalia(leilao_corruscant)

        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado,avaliacao.menor_lance)
        self.assertEqual(maior_valor_esperado,avaliacao.maior_lance)

