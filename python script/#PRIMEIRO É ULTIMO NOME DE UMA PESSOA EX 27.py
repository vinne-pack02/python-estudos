#PRIMEIRO É ULTIMO NOME DE UMA PESSOA EXE 27
print('\n', '=' *7 ,'PRIMEIRO E ÚLTIMO NOME', '=' *7)
nome = input('Digite o seu nome completo: ').strip()

part = nome.upper().split()
a1 = part[0]
a2 = part[-1]

print('\nO primeiro nome:   ', a1 , '\n')
print('O segundo nome:    ', a2 ,'\n')
print('='*30 , '\n')