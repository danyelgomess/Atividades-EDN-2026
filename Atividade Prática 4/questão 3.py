# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.

print("=== Verificação de Segurança de Senha ===")
senha = input("Digite a senha para verificação: ")

tem_numero = False

for char in senha:
    if char.isdigit():
        tem_numero = True
        break  

if len(senha) >= 8 and tem_numero:
    print("Senha segura.")
else:
    print("Senha insegura. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")


