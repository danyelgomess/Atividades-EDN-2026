# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

print("=== Registro de Notas dos Alunos ===")
num_alunos = int(input("Digite o número de alunos na turma: "))
notas = []

for i in range(num_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
media = sum(notas) / num_alunos
print(f"A média da turma é: {media:.2f}")
