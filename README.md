# Projeto de Banco de Dados com SQLAlchemy e PyMongo

Este projeto demonstra como usar SQLAlchemy para interagir com um banco de dados SQLite e PyMongo para interagir com um banco de dados MongoDB.

## Requisitos

- Python 3.6+
- SQLAlchemy
- PyMongo
- SQLite
- MongoDB

## Configuração

1. Clone este repositório para a sua máquina local.
2. Instale as dependências necessárias com o comando `pip install -r requirements.txt`.
3. Crie um arquivo `.env` no diretório raiz do projeto e adicione as seguintes variáveis de ambiente:

```bash
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority
DB_NAME=<dbname>
```

Substitua <username>, <password> e <dbname> pelas suas credenciais do MongoDB Atlas.

## Execução
Para executar o projeto, use o comando python main.py no diretório raiz do projeto.

## Contribuição
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a licença MIT.

