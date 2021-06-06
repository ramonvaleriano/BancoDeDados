from datetime import datetime, timedelta


class DatasFuturas:
    def __init__(self, quantidade):
        self.__hoje = datetime.now().date()
        self.__quantidade = quantidade
        self.__listaDatasFuturas = list()

    def criandoDatasFurutas(self):

        self.__listaDatasFuturas.append(self.__hoje)

        numero_de_dias = self.__quantidade
        for giro in range(numero_de_dias):
            novo_dia = timedelta(1) + self.__listaDatasFuturas[-1]
            self.__listaDatasFuturas.append(novo_dia)

    def conversaoData(self):
        self.criandoDatasFurutas()
        lista_temporaria = list()
        for data in self.__listaDatasFuturas:
            lista_temporaria.append(data.strftime('%Y-%m-%d'))
        self.__listaDatasFuturas = lista_temporaria[:]

    @property
    def hoje(self):
        return self.__hoje

    @property
    def datas_Futuras(self):
        self.conversaoData()
        return self.__listaDatasFuturas
