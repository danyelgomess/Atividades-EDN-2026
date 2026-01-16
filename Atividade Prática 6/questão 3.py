# 3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

import requests

cep = input("Digite o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Logradouro:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])

except requests.exceptions.RequestException:
    print("Erro ao consultar o CEP.")
