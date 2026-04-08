#ANALISADOR DE TEXTO EXERCÍCIO 22
print('=' *7, 'ANALIZADOR DE TEXTO', '=' *7)
name = input('\ndigite seu nome completo; ')

masc = name.upper()
mine = name.lower()
how = name.replace(" ", '')
a1 = name.split()[0]

print('\nO nome em maiusculo; \n{}'.format(masc))
print('\nO nome em minusculo; \n{}'.format(mine))
print('\nO mome tem ao total {} letras'.format(len(how)))
print('\nO primeiro nome é {} e tem {} letras\n'.format(a1, len(a1))) 