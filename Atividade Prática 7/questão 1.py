# 1- Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV.
# Para isso:

# * Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
# * Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
# * Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
# * Confirme a gravação exibindo uma mensagem com o nome do arquivo.
# * Trate possíveis erros de escrita de arquivo.

#  Dica: Use `csv.writer()` para escrever os dados linha por linha.

import csv


pessoas = [
    ["Nome", "Idade", "Cidade"],  # cabeçalhos
    ["Ana", 25, "São Paulo"],
    ["Bruno", 30, "Rio de Janeiro"],
    ["Carla", 22, "Belo Horizonte"]
]

nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")

try:
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(pessoas)

    print(f" Arquivo '{nome_arquivo}' criado com sucesso!")

except Exception as erro:
    print(" Erro ao escrever no arquivo:", erro)