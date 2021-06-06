from trabalhandoDatas import DatasFuturas

class JuncaoDataEValores:
    def __init__(self, valor_apartamento, valor_chale, quantidade_de_dias):
        self.__valor_apartamento = valor_apartamento
        self.__valor_chale = valor_chale
        self.__quantidade_de_dias = quantidade_de_dias
        self.__quantidade_dias_usados = 0
        self.__lista_juncao = list()
        self.__lista_valores_apartamento = list()
        self.__lista_valores_chale = list()

    def __puxando_valores(self):
        self.gerando_datas = DatasFuturas(self.__quantidade_de_dias)
        self.datas = self.gerando_datas.datas_Futuras
        self.__quantidade_dias_usados = len(self.datas)

    def __gerando_lista_repetidos(self):
        self.__puxando_valores()
        for g in range(self.__quantidade_dias_usados):
            self.__lista_valores_apartamento.append(self.__valor_apartamento)
            self.__lista_valores_chale.append(self.__valor_chale)

    def juncao_por_tuplas(self):
        self.__puxando_valores()
        self.__gerando_lista_repetidos()
        for i in range(self.__quantidade_dias_usados):
            lista_temporaria = [self.datas[i], self.__lista_valores_apartamento[i], self.__lista_valores_chale[i]]
            self.__lista_juncao.append(lista_temporaria)

    @property
    def quantidade(self):
        return self.__quantidade_dias_usados

    @property
    def lista_de_valores_apartamento(self):
        return self.__lista_valores_apartamento

    @property
    def lista_de_valores_chale(self):
        return self.__lista_valores_chale

    @property
    def datas_coletadas(self):
        return self.datas

    @property
    def lista_juncao(self):
        return self.__lista_juncao


"""dadosParateste = JuncaoDataEValores(100, 50, 10)
dadosParateste.juncao_por_tuplas()
dados = dadosParateste.lista_juncao
print(dados)
"""