#SORTEANDO UM ITEM NA LISTA EERCÍCIO 19
import random
print('=' *7,'SORTEIO DE NOMES', '=' *7)
a1 = input('\ndigite o nome do aluno 1; ')
a2 = input('digite o nome do aluno 2; ')
a3 = input('digite o nome do aluno 3; ')
a4 = input('digite o nome do aluno 4; ')

alunos = [a1, a2, a3, a4]

esc= random.choice(alunos)

print('\n o escolido foi {}\n'.format(esc))         

 