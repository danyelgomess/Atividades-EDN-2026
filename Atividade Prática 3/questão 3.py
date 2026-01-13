# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

# Conversor de Temperatura

def converter_temperatura(valor, origem, destino):
    origem = origem.upper()
    destino = destino.upper()

    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5 / 9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        return None

    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9 / 5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return None


temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C, F ou K): ")
unidade_destino = input("Unidade de destino (C, F ou K): ")

resultado = converter_temperatura(temperatura, unidade_origem, unidade_destino)

if resultado is not None:
    print(f"Resultado: {resultado:.2f}°{unidade_destino.upper()}")
else:
    print("Unidade inválida. Use C, F ou K.")
