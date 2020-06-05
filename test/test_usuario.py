from src.leilao.dominio import Usuario, Leilao

import pytest

from src.leilao.exception import LanceInvalido


@pytest.fixture()
def mando():
    return Usuario("Mandaloriano",100)

@pytest.fixture()
def leilao():
    return Leilao("Cidades")

def teste_para_ver_comportamento_da_carteira_do_usuario(mando, leilao):

    mando.propoeLance(leilao, 50)

    assert mando.carteira == 50


def teste_para_permitir_lance_igual_ao_valor_na_carteira(mando, leilao):

    mando.propoeLance(leilao, 100)

    assert mando.carteira == 0

def teste_nao_para_permitir_lance_maior_que_o_valor_na_carteira(mando, leilao):

    with pytest.raises(LanceInvalido):

        corruscont = Leilao("Cidades")

        mando.propoeLance(leilao, 200)

        assert mando.carteira == 100

