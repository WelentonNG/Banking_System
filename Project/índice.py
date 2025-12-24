arquivos = ['relatorio.pdf', 'foto.jpg', 'planilha.xls']

# 1. Pede o número ao usuário
# O input() sempre retorna texto, então usamos int() para virar número
entrada = input("Digite o número do arquivo (1 a 3): ")
numero_digitado = int(entrada)

# 2. Faz a conversão (Humano para Computador)
indice = numero_digitado - 1

# 3. Verifica se o número é válido para evitar erro
if 0 <= indice < len(arquivos):
    print(f"Arquivo encontrado: {arquivos[indice]}")
else:
    print("Erro: Número inválido ou arquivo não existe.")