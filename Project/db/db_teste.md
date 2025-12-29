### 1. O Fluxo Padrão

1. **Importar** a biblioteca do banco.
2. **Criar a conexão** (passando host, usuário, senha, nome do banco).
3. **Criar um cursor** (o objeto que executa os comandos).
4. **Executar a query** SQL.
5. **Buscar os resultados** (fetch) ou **Confirmar a transação** (commit).
6. **Fechar** a conexão.

---

### 2. Exemplos Práticos

#### A. PostgreSQL (Recomendado: `psycopg2`)

O PostgreSQL é um dos bancos mais usados com Python.

1. Instale o driver:

```bash
pip install psycopg2-binary
```

2. Código de conexão:

```python
import psycopg2

try:
    # Conectar ao banco existente
    conexao = psycopg2.connect(
        host="localhost",
        database="nome_do_banco",
        user="seu_usuario",
        password="sua_senha"
    )

    cursor = conexao.cursor()

    # Executar uma consulta
    cursor.execute("SELECT * FROM sua_tabela LIMIT 5;")
    resultados = cursor.fetchall()

    for linha in resultados:
        print(linha)

except Exception as e:
    print(f"Erro ao conectar: {e}")
finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexão fechada.")
```

#### B. MySQL / MariaDB (Recomendado: `mysql-connector-python`)

1. Instale o driver:

```bash
pip install mysql-connector-python
```

2. Código de conexão:

```python
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_banco"
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM sua_tabela LIMIT 5")

for linha in cursor:
    print(linha)

conexao.close()
```

#### C. SQLite (Nativo)

Se o seu banco é um arquivo `.db` ou `.sqlite`, você não precisa instalar nada. A biblioteca já vem no Python.

```python
import sqlite3

# Conecta ao arquivo existente
conexao = sqlite3.connect('caminho/para/seu_banco.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM tabela_exemplo")
print(cursor.fetchall())

conexao.close()
```

---

### 3. A Abordagem Profissional: SQLAlchemy (ORM)

Em projetos reais e maiores, evitamos escrever SQL puro (`SELECT * FROM...`) dentro do código Python. Usamos um **ORM** (Object Relational Mapper), que transforma as tabelas do banco em objetos Python. O mais famoso é o **SQLAlchemy**.

* **Vantagem:** Funciona com quase qualquer banco de dados apenas mudando a "string de conexão".

1. Instale: `pip install sqlalchemy`
2. Exemplo:

```python
from sqlalchemy import create_engine, text

# String de conexão (Exemplo para PostgreSQL)
# Formato: dialect+driver://username:password@host:port/database
url_conexao = "postgresql+psycopg2://usuario:senha@localhost/meu_banco"

engine = create_engine(url_conexao)

# Conectar e executar
with engine.connect() as conexao:
    resultado = conexao.execute(text("SELECT * FROM usuarios"))
    for linha in resultado:
        print(linha)
```

---

### 4. Segurança (Importante)

**Nunca** escreva senhas diretamente no seu código (`hardcoding`), especialmente se for subir para o GitHub. Use variáveis de ambiente.

1. Crie um arquivo chamado `.env` na pasta do projeto:

```text
DB_USER=admin
DB_PASS=minhasenha123
```

2. Use a biblioteca `python-dotenv` para ler:

```python
import os
from dotenv import load_dotenv

load_dotenv() # Carrega o arquivo .env

usuario = os.getenv("DB_USER")
senha = os.getenv("DB_PASS")
# Agora use essas variáveis na sua conexão
```

---

### Resumo das Bibliotecas (Drivers)

| Banco de Dados       | Biblioteca Recomendada     | Comando de Instalação                |
| -------------------- | -------------------------- | -------------------------------------- |
| **PostgreSQL** | `psycopg2`               | `pip install psycopg2-binary`        |
| **MySQL**      | `mysql-connector-python` | `pip install mysql-connector-python` |
| **SQL Server** | `pyodbc`                 | `pip install pyodbc`                 |
| **Oracle**     | `oracledb`               | `pip install oracledb`               |
| **SQLite**     | `sqlite3`                | (Já vem instalado)                    |

---

**Qual é o banco de dados específico que você está tentando acessar (MySQL, Postgres, SQL Server, etc.)?** Assim posso te dar o código exato para a sua necessidade.
