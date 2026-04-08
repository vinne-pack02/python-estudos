#SEPARANDO DIGITOS DE UM NUMERO EXERCÍCIO 23
print('=' *7, 'SEPARADOR DE NUMEROS', '='*7)

num = input('\nDigite 1 numero entre 0 e 9999; ')

a = num[0:4]

mil = a[0]
cen = a[1]
dez = a[2]
uni = a[3]

print("\nUNIDADE: {}". format(uni))
print('DEZENA: {}'.format(dez))
print('CENTENA: {}'.format(cen))
print('MILHAR: {}\n'.format(mil))
