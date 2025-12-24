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



money=[]

def ALL():
    total=0

    for n in money:
        total+=n
    return total


def AddMoney():#Adiciona o dinheiro ao sua conta
    addmn=int(input("Digite aqui a sua quantia em dinheiro "))
    print(f"Você acaba de colocar uma nova quantia em dinheiro {addmn}")
    money.append(addmn)



def consult_money():#Faz consulta da sua quantia bancaria 
    total = ALL()

    if total == 0:
        print(f"Sua conta está zerada: R${total:.2f}")
    else:
        print(f"Saldo total: R${total:.2f}")


def transfer_balance():#Faz uma transferencia de dinheiro
    print("\n")
    print("O máximo de números são 8")

    total = sum(money)
    numero_digitado = input("Digite o número da conta para a transferência: ")
    debito_saldo = int(input("Quanto você deseja enviar? "))

    if total == 0:
        print(f"Você não pode fazer a transferência porque sua conta está zerada R$:{money}")

    elif debito_saldo > total:
        print("Saldo insuficiente")

    elif len(numero_digitado) == 8 and numero_digitado.isdigit():
        novo_saldo = total - debito_saldo
        money.clear()
        money.append(novo_saldo)

        print("Transferência feita com sucesso")
        print("Saldo atual:", novo_saldo)

    else:
        print("Algo deu errado, TENTE NOVAMENTE")



while True:
    print('\n')
    print("|-------------------------------------|")
    print('| ==================================  |')
    print('| ======= Sitema de Bancario =======  |')
    print('| ==================================  |')
    print("|-------------------------------------|")
    print('\n')
    print("1.Implementar dinheiro a conta ")
    print("2.Ver saldo atual")
    print("3.Transferir dinheiro")
    
    #print("4.")
    print("0.Sair do Sistema")
    print('\n')

    opcao=input('Digite a opção desejada  ')

    if opcao == '1':
        AddMoney()
    elif opcao == '2':
        consult_money()
    elif opcao == '3':
        transfer_balance()
    elif opcao == '0':
        contagem_regressiva()
        break  

    