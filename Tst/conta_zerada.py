# money = []  # Quantia de dinheiro atual 

# def consult_money():
#     # Calcula o total da lista
#     total = sum(money) if money else 0
    
#     print(f"Sua quantia de dinheiro é R$ {total:.2f}")
    
#     if total == 0:
#         print(f"Sua conta está zerada: R$ {total:.2f}")

# # Teste
# consult_money()




money = []  

def consult_money():

    total = sum(money) 
    
    print(f"Sua quantia de dinheiro é R$ {total:.2f}")
    
    if total == 0:
        print(f"Sua conta está zerada: R$ {total:.2f}")

# Teste
consult_money()