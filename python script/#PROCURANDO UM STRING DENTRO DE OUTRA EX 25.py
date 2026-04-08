#PROCURANDO UM STRING DENTRO DE OUTRA EXER 25
print('=' *7, 'É SILVA OU NÃO É', '=' *7,'\n')
nome = input('Digiteo seu nome completo? ')
a1 = 'silva' in nome
print('\nO teste de DNA deu {} pra silva\n '.format(a1))
print('    ', '=' *7, '{}'.format(a1), '='*7, '\n')