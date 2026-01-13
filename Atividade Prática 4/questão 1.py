# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).


print("=== Calculadora Básica ===")
print("Operações disponíveis:")
print("+  Soma")
print("-  Subtração")
print("*  Multiplicação")
print("/  Divisão")

operacao = input("Escolha a operação (+, -, *, /): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    print("Operação inválida!")
