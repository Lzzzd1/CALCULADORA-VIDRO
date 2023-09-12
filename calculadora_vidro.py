# Solicita ao usuário os valores da área, altura e valor do vidro
area = float(input("Informe a área do vidro em metros quadrados: "))
altura = float(input("Informe a altura do vidro em metros: "))
valor_vidro = float(input("Informe o valor do vidro por metro quadrado: "))

# Calcula o valor do vidro
valor_total = area * altura * valor_vidro

# Exibe o resultado
print(f"O valor total do vidro é R$ {valor_total:.2f}")

# Aguarda que o usuário pressione Enter para fechar o executável
input("Pressione Enter para fechar o programa...")
 