from unittest import TestCase

from src.leilao.dominio import Leilao, Lance, Usuario, Avaliador


class TestAvaliador(TestCase):

    def setUp(self) -> None:
        self.jedi = Usuario("Jedi")
        self.sith = Usuario("Sith")
        self.lance_do_sith = Lance(self.sith, 100)
        self.lance_do_jedi = Lance(self.jedi, 150)
        self.leilao_corruscant = Leilao("Celular")
        self.avaliacao = Avaliador()


    def test_deve_retorna_o_maior_ou_menor_valor_de_um_lance_quando_adcionador_em_ordem_crescente(self):

        self.leilao_corruscant.lances.append(self.lance_do_sith)
        self.leilao_corruscant.lances.append(self.lance_do_jedi)

        self.avaliacao.avalia(self.leilao_corruscant)

        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado,self.avaliacao.menor_lance)
        self.assertEqual(maior_valor_esperado,self.avaliacao.maior_lance)


    def test_deve_retorna_o_maior_ou_menor_valor_de_um_lance_quando_adcionador_em_ordem_decrescente(self):

        self.leilao_corruscant.lances.append(self.lance_do_jedi)
        self.leilao_corruscant.lances.append(self.lance_do_sith)

        self.avaliacao.avalia(self.leilao_corruscant)

        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado,self.avaliacao.menor_lance)
        self.assertEqual(maior_valor_esperado,self.avaliacao.maior_lance)

    def teste_deve_retornar_valor_menor_e_maior_para_leilao_com_apenas_um_lance(self):

        self.leilao_corruscant.lances.append(self.lance_do_jedi)
        self.avaliacao.avalia(self.leilao_corruscant)
        self.assertEqual(150.0, self.avaliacao.menor_lance)

    def teste_deve_retornar_valor_menor_e_maior_para_leilao_com_tres_lances(self):
        mando = Usuario("Mandaloriano")

        lance_do_mando = Lance(mando, 200)

        self.leilao_corruscant.lances.append(self.lance_do_jedi)
        self.leilao_corruscant.lances.append(self.lance_do_sith)
        self.leilao_corruscant.lances.append(lance_do_mando)

        self.avaliacao.avalia(self.leilao_corruscant)

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, self.avaliacao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.avaliacao.maior_lance)
