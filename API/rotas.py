from casos_de_uso import inserir_registro, ler_registro, excluir_registro
from fastapi import FastAPI
from entidades import Usuario

app = FastAPI()


@app.post("/usuario/registrar")
def inserir_registro_rota(usuario: Usuario):
    inserir_registro(usuario.nome, usuario.idade)
    return {"nome": usuario.nome, "idade": usuario.idade}


@app.get("/usuario/listar/{id_registro}")
async def ler_registro_rota(id_registro: int):
    registro = ler_registro(id_registro)
    return registro


@app.delete("/usuario/excluir/{id_registro}")
def excluir_registro_rota(id_registro: int):
    excluir_registro(id_registro)
    return {"id excluído": id_registro, }
