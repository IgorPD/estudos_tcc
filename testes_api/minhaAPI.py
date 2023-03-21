from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

# Instancia o objeto "app" que será utilizado para definir as rotas da API
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool] = None  # pode aceitar mais de um tipo de entrada


# É uma anotação que especifica que esta função será chamada quando uma requisição HTTP do tipo GET for feita na rota
# raiz ("/")
@app.get("/")
def read_root():
    return {"Hello": "World"}


'''
Essa parte do código cria uma rota que responde a requisições HTTP do tipo GET no endpoint /items/{item_id}.
A função read_item é associada a essa rota. Ela aceita dois parâmetros de entrada, item_id e q.
O parâmetro item_id é passado como parte da URL, por exemplo, se a requisição for feita para o endpoint /items/42, o valor 42 será atribuído a item_id. O tipo de item_id é inteiro.
O parâmetro q é opcional e é passado como um parâmetro de consulta na URL, por exemplo, se a requisição for feita para o endpoint /items/42?q=test, o valor test será atribuído a q.
O tipo de q é uma união de string ou nulo, ou seja, ele pode ser uma string ou não ser passado na requisição.
A função retorna um dicionário com as chaves "item_id" e "q", onde o valor de "item_id" é o valor passado para item_id e o valor de "q" é o valor passado para q.
'''


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# será executada quando o cliente enviar uma requisição PUT para o endpoint /items/{item_id}
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # item_id é um parâmetro de URL que será passado na URL da requisição
    # item é um objeto do tipo Item que será extraído dos dados da requisição
    return {"item_name": item.name, "item_id": item_id}
