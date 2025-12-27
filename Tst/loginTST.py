# Dicionário principal de usuários
# Formato: {username: {'password': senha, 'email': email, etc...}}
users = {
    "admin": {
        "password": "admin123",
        "email": "admin@exemplo.com"
    },
    "joao": {
        "password": "senha456",
        "email": "joao@email.com"
    }
}

def criar_usuario():
    """Cria um novo usuário"""
    print("\n--- CRIAR NOVO USUÁRIO ---")
    username = input("Digite o nome de usuário: ")
    
    # Verifica se o usuário já existe
    if username in users:
        print("Erro: Usuário já existe!")
        return
    
    password = input("Digite a senha: ")
    email = input("Digite o email: ")
    
    # Adiciona o novo usuário ao dicionário
    users[username] = {
        "password": password,
        "email": email
    }
    
    print(f"Usuário '{username}' criado com sucesso!")

def fazer_login():
    """Realiza o login de um usuário"""
    print("\n--- LOGIN ---")
    username = input("Usuário: ")
    password = input("Senha: ")
    
    # Verifica se o usuário existe e se a senha está correta
    if username in users and users[username]["password"] == password:
        print(f"Login bem-sucedido! Bem-vindo, {username}!")
        return True, username
    else:
        print("Erro: Usuário ou senha incorretos!")
        return False, None

def listar_usuarios():
    """Lista todos os usuários cadastrados"""
    print("\n--- USUÁRIOS CADASTRADOS ---")
    if not users:
        print("Nenhum usuário cadastrado.")
    else:
        for username, info in users.items():
            print(f"Usuário: {username}")
            print(f"  Email: {info['email']}")
            print("-" * 30)

def menu_principal():
    """Menu interativo do sistema"""
    while True:
        print("\n=== SISTEMA DE LOGIN ===")
        print("1. Criar novo usuário")
        print("2. Fazer login")
        print("3. Listar usuários")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            sucesso, usuario = fazer_login()
            if sucesso:
                # Aqui você pode adicionar o que acontece após login
                print(f"\nAcesso concedido para {usuario}!")
                # Exemplo: menu_logado(usuario)
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Iniciar o sistema
if __name__ == "__main__":
    menu_principal()    