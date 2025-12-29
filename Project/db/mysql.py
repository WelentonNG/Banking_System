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