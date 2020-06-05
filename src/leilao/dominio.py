from src.leilao.exception import LanceInvalido


class Usuario:

    def __init__(self, nome,carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoeLance(self, leilao, valor):
        if(not self._valor_e_valido(valor)):
            raise LanceInvalido("Valor maior que o valor da carteira")
        lance = Lance(self,valor)
        leilao.efetuaLance(lance)
        self.__carteira -= valor

    def _valor_e_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao: str):
        self.__descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def efetuaLance(self, lance: Lance):
        if( self._lance_e_valido(lance)):

            if(not self._tem_lances()):
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def _usuario_diferentes(self, lance):
        if( self.__lances[-1].usuario.nome != lance.usuario):
            return True
        else:
            raise LanceInvalido("Os usuário são o mesmo!")

    def _valor_maior_que_lance_anterior(self, lance):
        if( lance.valor > self.__lances[-1].valor):
            return True
        else:
            raise LanceInvalido("O valor do lance é menor que o anterior.")

    def _lance_e_valido(self, lance):
        return not self._tem_lances() or \
               (self._usuario_diferentes(lance) and self._valor_maior_que_lance_anterior(lance))