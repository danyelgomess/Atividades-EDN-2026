# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime
def calcular_dias_vivo(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    data_atual = datetime.now()
    dias_vivo = (data_atual - data_nascimento).days
    return dias_vivo

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias_vivo = calcular_dias_vivo(data_nascimento)
print(f"Você está vivo há {dias_vivo} dias.")
