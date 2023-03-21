from fastapi import FastAPI
from typing import Union

from numpy.distutils.system_info import p
from pydantic import BaseModel

app = FastAPI()


# NÃO ESQUECER - Parametro de path é definido com {} dentro da definição da rota
# Parametro de query pode ser definido simplesmente ao adicionar o nome do parâmetro como argumento da função.
@app.get("/usuarios/{usuario_id}")
async def usuario_path(usuario_id: int):
    """
    Usando e retornando os parametros de path
    """
    return {"usuario_id": usuario_id}


@app.get("/usuarios/")
async def usuario_query(usuario_id: int, nome: str = None):
    """
    Usando e retornando os parametros de query
    """
    resposta = {"usuario_id": usuario_id}
    if nome:
        resposta["nome"] = nome
    return resposta


@app.get("/usuarios/{usuario_id_nome}")
async def usuario_path_query(usuario_id_nome: int, nome: str = None):
    """
    Usando e retornando os parametros de path e query
    """
    return{"usuario_id": usuario_id_nome, "nome": nome}


class Pessoa(BaseModel):
    nome: str
    idade: int
    altura: int


@app.post("/pessoas/{pessoa_id}")
async def pessoa_path_br(pessoa_id: int, pessoa: Pessoa):
    """
     Usando e retornando os parametros de path e o body request
    """
    return {"pessoa_id": pessoa_id, "pessoa": pessoa}


@app.post("/pessoas/")
async def pessoa_query_br(pessoa_id: int, pessoa: Pessoa):
    """
    Usando e retornando os parametros de query e o body request
    """
    return {"pessoa_id": pessoa_id, "pessoa": pessoa}


@app.post("/pessoas/{pessoa_id}")
async def pessoa_path_br_query(pessoa_id: int, pessoa: Pessoa):
    """
    Usando e retornando os parametros de path, body request e query
    """
    return {"pessoa_id": pessoa_id, "pessoa": pessoa}
