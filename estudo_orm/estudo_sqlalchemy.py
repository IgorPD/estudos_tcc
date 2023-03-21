from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# conectando ao banco de dados
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres", echo=True)

# declarando mapeamento
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # obrigatorio

    id = Column(Integer, primary_key=True)  # obrigatorio
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)


    '''def __repr__(self):  # adicionado posteriormente
        return "<User{name={}, fullname={}, age={}}>".format(
            self.name, self.fullname, self.age)'''


# criar a tabela no banco de dados
Base.metadata.create_all(engine)

# criar instancias da classe
# user = User(name='Lucas', fullname='Lucas Teste', age=24)
'''session.add_all([
    User(name='Lucas', fullname='Lucas Teste', age=24),
    User(name='Leonardo', fullname='Leonardo TTeste', age=900)
])'''

# criar sessão
Session = sessionmaker(bind=engine)
session = Session()

# adicionar objetos(Insert)
# session.add(user)  # Adiciona na memória
# session.commit()   # Comita para o banco

# Consultar objetor(SELECT)
# query_user = session.query(User).filter_by(name="Lucas").first()
'''for instance in session.query(User).all():
    print(instance.id, instance.name, instance.age)'''


'''for instance in session.query(User).filter(User.id == 4).all():
    print(instance.id, instance.name, instance.age)
    '''

# Modificar objetos(UPDATE)


# Deletar objetos(DELETE)
user = session.query(User).filter_by(name="Lucas").first
session.delete(user)
session.commit()

