def adicionar_item(lista_a_preencher):
  """
  Solicita um item ao usuário e o adiciona à lista fornecida.
  """
  # 1. Solicita o input dentro da função
  item = input("Por favor, digite o item que deseja adicionar: ")

  # 2. Usa o método .append() para adicionar o item à lista
  lista_a_preencher.append(item)

  # 3. Retorna a lista modificada para que possa ser usada fora da função
  return lista_a_preencher

# --- Execução do Programa ---

# 1. Define uma lista vazia
minha_lista = []
lista_atualizada = adicionar_item(minha_lista)

print(f"Lista antes da função: {minha_lista}")
print("---")

# 2. Chama a função, passando a lista vazia

print("---")
print(f"Lista após a função: {lista_atualizada}")