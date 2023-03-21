from pydantic import BaseModel


class Usuario(BaseModel):
    nome: str
    idade: int
