from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)

class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    numero_conta = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer)

