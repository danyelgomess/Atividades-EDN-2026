# 3- Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON.
# Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo.
# Para isso:

# * Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
# * Solicite ao usuário o nome do arquivo JSON.
# * Salve os dados no arquivo usando o módulo `json`.
# * Após salvar, leia o mesmo arquivo e imprima os dados carregados.
# * Trate possíveis erros como ausência do arquivo ou problemas na escrita.

 # Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.



import json  

# Dicionário com dados da pessoa
pessoa = {
    "nome": "Danyel",
    "idade": 20,
    "cidade": "São Paulo"
}

nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")

try:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

    print("Dados salvos com sucesso!")

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    print("Dados lidos do arquivo:")
    print(dados)

except FileNotFoundError:
    print("Arquivo não encontrado.")

except Exception as erro:
    print("Erro:", erro)
