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