from casos_de_uso import inserir_registro, ler_registro, atualizar_registro, deletar_registro
from fastapi import FastAPI
from entidades import Usuario

app = FastAPI()


@app.post("/usuario/registrar")
def inserir_registro_rota(usuario: Usuario):
    inserir_registro(usuario.nome, usuario.idade)
    return {"nome": usuario.nome, "idade": usuario.idade}


@app.get("/usuario/listar/{id_registro}")
def ler_registro_rota(id_registro: int):
    registro = ler_registro(id_registro)
    return registro


@app.post("/usuario/atualizar{id_registro}")  # tava colocando get, burro pra crl
def atualizar_registro_rota(id_registro: int, usuario: Usuario):
    atualizar_registro(id_registro, usuario.nome, usuario.idade)
    return {"nome": usuario.nome, "idade": usuario.idade}


@app.delete("/usuario/excluir/{id_registro}")
def excluir_registro_rota(id_registro: int):
    deletar_registro(id_registro)
    return {"id excluído": id_registro}
