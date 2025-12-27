# Mostrar data e hora de criação de usuarios 

Users = {
    "administrator": {
        "Login": "admin",
        "password": "admin123",
    }
}

def criarusuarios():
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
            "login": login,
            "password": password
        }

        print(f"Usuário '{username}' criado com sucesso")
    else:
        print("Erro: Usuário já existe")


def fazerlogin():
    print("\n ---- LOGIN ----")
    username=input("Usuário:  ")


