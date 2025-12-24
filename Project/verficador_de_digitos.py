numero_digitado = input("Digite 8 números: ")

if len(numero_digitado) == 8 and numero_digitado.isdigit():
    print("Exatamente 8 números válidos foram digitados.")
else:
    print("Entrada inválida. Certifique-se de digitar exatamente 8 caracteres numéricos.")

