# Entry point do FastAPI

# app/main.py (temporário, só para criar o banco)
from fastapi import FastAPI
from app.database import Base, engine
from app.models import user

app = FastAPI()

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)
