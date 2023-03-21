from pandas_data_provider import PandasDataProvider


def inserir_registro(nome, idade):
    data_provider = PandasDataProvider()
    data_provider.inserir_registro(nome, idade)


def ler_registro(id_registro):
    data_provider = PandasDataProvider()
    registro = data_provider.ler_registro(id_registro)
    return registro


def excluir_registro(id_registro):
    data_provider = PandasDataProvider()
    data_provider.excluir_registro(id_registro)

