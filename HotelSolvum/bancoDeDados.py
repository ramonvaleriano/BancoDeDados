import sqlite3

from datasComValores import JuncaoDataEValores

class BancoDeDadosHotel:
    def __init__(self, valor_apartamento, valor_chale, quantidade_de_dias):
        self.__valor_apartamento = valor_apartamento
        self.__valor_chale = valor_chale
        self.__quantidade_de_dias = quantidade_de_dias

    def criando_banco_de_dados(self):
        dados_a_serem_arquivados = JuncaoDataEValores(self.__valor_apartamento, self.__valor_chale, self.__quantidade_de_dias)
        dados_a_serem_arquivados.juncao_por_tuplas()
        dados = dados_a_serem_arquivados.lista_juncao
        print(dados)

        conexao = sqlite3.connect('hotel.db')
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute("""create table orcamento(
                          id integer primary key autoincrement,
                          data text,
                          apartamento real,
                          chale real
                          )""")
        cursor.executemany("insert into orcamento(data, apartamento, chale) values(?,?,?)", dados)
        conexao.commit()
        cursor.close()
        conexao.close()

    def consultando_banco_de_dados(self):
        conexao = sqlite3.connect('hotel.db')
        conexao.row_factory = sqlite3.Row
        print('%3s %-12s %4s %4s' %('id', 'Data', 'Apartamento', 'Chalé'))
        print('='*37)
        for linha in conexao.execute("select * from orcamento order by data"):
            print(f'{linha["id"]:3d} {linha["data"]:12s} {linha["apartamento"]:-10.2f}  {linha["chale"]:-6.2f}')
        conexao.close()

instDados = BancoDeDadosHotel(180, 140, 378)
#instDados.criando_banco_de_dados()
instDados.consultando_banco_de_dados()




