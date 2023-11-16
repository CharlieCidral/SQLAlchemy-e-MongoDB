from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import joinedload
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# SQLAlchemy: Define a base class for declarative class definitions
Base = declarative_base()

# SQLAlchemy: Define Cliente class for the 'clientes' table
class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9), unique=True)
    endereco = Column(String(12))
    contas = relationship('Conta', backref='cliente')

# SQLAlchemy: Define Conta class for the 'contas' table
class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero_conta = Column(Integer)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey('clientes.id'))

# Parte 1 – Implementando um Banco de Dados SQL com SQLAlchemy
engine = create_engine('sqlite:///banco.db') # SQLAlchemy: Criando SQLite engine
Base.metadata.create_all(engine) # SQLAlchemy: Criando tabelas

Session = sessionmaker(bind=engine) # SQLAlchemy: Criando a session factory
session = Session() # SQLAlchemy: Criando a session

stmt_join = select(Cliente.nome, Conta.saldo).join_from(Conta, Cliente)

with engine.connect() as connection:
    results = connection.execute(stmt_join).fetchall()
    for result in results:
        print(result)

# SQLAlchemy: Adicionando um Cliente e Conta ao banco de dados
cliente1 = Cliente(nome='João', cpf='123456789', endereco='Rua 123')
conta1 = Conta(tipo='Poupança', agencia='001', numero_conta=12345, id_cliente=cliente1.id)

session.add(cliente1)
session.add(conta1)
session.commit()

# SQLAlchemy: Consultar e imprimir Cliente com Contas usando joinedload
clientes = session.query(Cliente).options(joinedload(Cliente.contas)).all()
for cliente in clientes:
    print(cliente.nome)

for cliente in clientes:
    print(cliente.nome)
    for conta in cliente.contas:
        print(conta.numero_conta)

# Parte 2 – Implementando um Banco de Dados NoSQL com Pymongo
load_dotenv() # Carregar variáveis de ambiente do arquivo .env

uri = os.getenv('MONGO_URI') # Obter o URI do MongoDB a partir de variáveis de ambiente
bank = os.getenv('bank') # Obter o nome do banco de dados MongoDB de variáveis de ambiente

print("MONGO_URI:", os.getenv("MONGO_URI"))
print("bank:", os.getenv("bank"))

# Crie um novo cliente e conecte-se ao servidor
client = MongoClient(uri, server_api=ServerApi('1'))
db = client[bank]

# Enviar um ping para confirmar uma conexão bem-sucedida
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.bank  # substitua "bank" pelo nome do seu banco de dados
bank = db.bank # Pymongo: Insira um documento na coleção 'bank'

cliente = {
    'nome': 'João',
    'cpf': '123456789',
    'endereco': 'Rua 123',
    'contas': [
        {
            'numero_conta': '12345',
            'agencia': '001',
            'tipo': 'Poupança'
        }
    ]
}

bank.insert_one(cliente)

# Pymongo: Consultar e imprimir documentos da coleção 'bank'
clientes = bank.find({})
for cliente in clientes:
    print(f"Nome: {cliente['nome']}")
    print(f"CPF: {cliente['cpf']}")
    print(f"Endereço: {cliente['endereco']}")
    for conta in cliente['contas']:
        print(f"Conta: {conta['numero_conta']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Tipo: {conta['tipo']}")

# Pymongo: Consulta e impressão de documentos com 'contas.saldo' maior que 500
contas = bank.find({'contas.saldo': {'$gt': 500}})
for conta in contas:
    print(conta['contas'])
