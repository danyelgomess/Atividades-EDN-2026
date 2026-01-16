# 4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

import requests

moeda = input("Digite a moeda (ex: USD, EUR): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        info = dados[chave]

        print("Valor atual:", info["bid"])
        print("Máxima:", info["high"])
        print("Mínima:", info["low"])
        print("Última atualização:", info["create_date"])

except requests.exceptions.RequestException:
    print("Erro ao consultar a moeda.")
