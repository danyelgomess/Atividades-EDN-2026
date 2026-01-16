# 2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.

import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)

except requests.exceptions.RequestException:
    print("Erro ao conectar na API.")
    print("\nUsuário fictício gerado com sucesso!\n")
    

