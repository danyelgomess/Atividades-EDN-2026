# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

print("=== Análise de Números ===")

quantidade = int(input("Quantos números você deseja digitar? "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))

    if numero % 2 == 0:
        print("Número par.")
        pares += 1
    else:
        print("Número ímpar.")
        impares += 1

print("\n=== Resultado Final ===")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
