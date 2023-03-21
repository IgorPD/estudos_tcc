from postgres_data_provider import UsuarioDataProvider


def inserir_registro(nome, idade):
    data_provider = UsuarioDataProvider()
    data_provider.inserir_registro(nome, idade)


def ler_registro(id_registro):
    data_provider = UsuarioDataProvider()
    registro = data_provider.ler_registro(id_registro)
    return registro


def atualizar_registro(id_registro, nome, idade):
    data_provider = UsuarioDataProvider()
    data_provider.atualizar_registro(id_registro, nome, idade)


def deletar_registro(id_registro):
    data_provider = UsuarioDataProvider()
    data_provider.deletar_registro(id_registro)

