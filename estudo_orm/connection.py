from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# configuracões
# "dialeto+driver://usuariobanco:senhabanco@localdobanco:portabanco/nomebanco"
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)  # uma sessão baseada nas conexões do banco de dados
session = Session()


# Entidades
class Filmes(Base):
    __tablename__ = "filmes"  # Essa entidades está se relacionado com a tabela filmes

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):  # apresenta os prints de uma maneira mais legivel
        return f"Filme [titulo={self.titulo}, genero={self.genero}, ano = {self.ano}]"


# SQL

# Insert
data_insert = Filmes(titulo="lango", genero="Aventura", ano=2023)
session.add(data_insert)
session.commit()

# Select
# data = session.query(Filmes).all()
print(data_insert)

session.close()
