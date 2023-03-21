from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import Column, Integer, String

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres", echo=True)

conn = engine.connect()
session = Session(engine)


class Base(DeclarativeBase):
    pass  # pass' é usado aqui para evitar um erro de sintaxe, mas não tem nenhum efeito real no código. Ele simplesmente indica que a classe 'Base' é uma classe vazia que não adiciona nada à classe 'DeclarativeBase'


class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, name="id")
    nome = Column(String(100), name="nome")
    idade = Column(Integer, name="idade")

    def __repr__(self):
        return f"[Usuario id = {self.id}, nome = {self.nome}, idade = {self.idade}]"

''' 
    não estava criando uma classe para separar as reponsabilidades, separando a lógica do banco com "UsuarioDataProvider"
    da classe "usuario" que representa a estrutura de dados do objeto do modelo de usuário. anotação completa no NOTION
'''


class UsuarioDataProvider:
    def __init__(self):
        pass

    def inserir_registro(self, nome, idade):
        usuario = Usuario(nome=nome, idade=idade)
        session.add(usuario)
        session.commit()

    def ler_registro(self, id_registro):
        usuario = session.get(Usuario, id_registro)
        if usuario:
            return f"id = {usuario.id}, nome = {usuario.nome}, idade = {usuario.idade}"
        else:
            return None

    def atualizar_registro(self, id_registro, nome, idade):
        usuario = session.get(Usuario, id_registro)
        if usuario:
            usuario.nome = nome
            usuario.idade = idade
            session.commit()
            return True
        else:
            return False

    def deletar_registro(self, id_registro):
        usuario = session.get(Usuario, id_registro)
        if usuario:
            session.delete(usuario)
            session.commit()
            return True
        else:
            return False


# provider = UsuarioDataProvider()
# provider.atualizar_registro(2, "igorr", 250)
'''provider.inserir_registro(nome="igor", idade="25")
provider.ler_registro(1)
provider.deletar_registro(8)'''

session.close()
