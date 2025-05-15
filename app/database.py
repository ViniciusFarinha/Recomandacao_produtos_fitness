# Config do banco (SQLAlchemy)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


class Conexao:
    def __init__(self, usuario, senha, servidor, database):
        self.usuario = usuario
        self.senha = senha
        self.servidor = servidor
        self.database = database



Conexao = Conexao('root', 'Bobin%4001', 'localhost:3306', 'banco_projeto_recomendacao')


# Conexão com o banco de dados
DATABASE_URL = "mysql+pymysql://{usuario}:{senha}@{servidor}/{database}".format(
    usuario=Conexao.usuario,
    senha=Conexao.senha,
    servidor=Conexao.servidor,
    database=Conexao.database
)

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_recycle=3600)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()