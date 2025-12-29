import main
import time
from datetime import datetime, timedelta

def contagem_regressiva():
    duracao = timedelta(seconds=4)
    fim = datetime.now() + duracao

    while True:
        tempo_restante = fim - datetime.now()
        segundos_restantes = int(tempo_restante.total_seconds())

        if segundos_restantes <= 0:
            break

        print(f"Saindo do sistema em: {segundos_restantes}...")
        time.sleep(1)

    print("Você saiu do sistema.")


Users = {
    "administrator": {
        "Login": "admin",
        "password": "admin123",
    }
}

def criar_usuarios():
    print("\n---- Verificar usuário ----")
    username = input("Digite o nome do usuario:  ")

    if username not in Users:
        print("Usuário não existe.")
        opcao = input("Deseja criar este usuário? (s/n): ").lower()

        if opcao != "s":
            return

        login = input("Digite o nome do novo usuário:  ")
        password = input("Digite a senha:  ")

        Users[username] = {
            "Login": login,        # 🔧 CORRIGIDO AQUI
            "password": password
        }

        print(f"Usuário '{username}' criado com sucesso")
    else:
        print("Erro: Usuário já existe")


def fazer_login():
    print("\n ---- LOGIN ----")
    login = input("Usuário:  ")
    password = input("Senha:  ")

    for user in Users.values():
        if user["Login"] == login and user["password"] == password:
            print(f"Login bem-sucedido! Bem-vindo, {login}!")
            return True, login

    print("Erro: Usuário ou senha incorretos!")
    return False, None


def listar_usuarios():
    print("\n---- USUÁRIOS CADASTRADOS ----")

    if not Users:
        print("Nenhum usuário cadastrado.")
    else:
        for username in Users:
            print(f"Usuário: {username}")
            print("-" * 30)



def menu_pricipal():
    while True:
        print("\n=== SISTEMA BANCARIOS ===")
        print("1. Fazer Login")
        print("2. Listar usuários")
        print("3. Criar novo usuário")
        print("4. sair")

        opcao = input("Escolha uma opção (1-4):  ")

        if opcao == '1':
            sucesso, usuario = fazer_login()

            if sucesso:
                main.main()   # 🚀 VAI PARA O main.py
            else:
                print("Tente novamente")

        elif opcao == '2':
            listar_usuarios()

        elif opcao == '3':
            criar_usuarios()

        else:
            break
menu_pricipal()