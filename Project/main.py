def main():
    import time
    from datetime import datetime, timedelta

    money = []

    def ALL():
        total = 0
        for n in money:
            total += n
        return total

    def AddMoney():
        addmn = int(input("Digite aqui a sua quantia em dinheiro "))
        print(f"Você acaba de colocar {addmn}")
        money.append(addmn)

    def consult_money():
        total = ALL()
        print(f"Saldo total: R${total:.2f}")

    def transfer_balance():
        total = sum(money)
        numero = input("Digite o número da conta: ")
        debito = int(input("Quanto deseja enviar? "))

        if debito > total:
            print("Saldo insuficiente")
        else:
            money.clear()
            money.append(total - debito)
            print("Transferência feita")

    while True:
        print("\n=== SISTEMA BANCÁRIO ===")
        print("1. Adicionar dinheiro")
        print("2. Ver saldo")
        print("3. Transferir")
        print("0. Sair")

        opcao = input("> ")

        if opcao == '1':
            AddMoney()
        elif opcao == '2':
            consult_money()
        elif opcao == '3':
            transfer_balance()
        elif opcao == '0':
            break
