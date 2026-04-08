#ANO BISSEXTO OU NÃO BISSEXTO EXERCÍIO 32
print('='*7,'ANO BISSEXTO', '='*7, '\n')

ano = int(input('digite um ano: \n'))

if ano % 4 == 0:
    print('\n{} é bissexto\n'.format(ano))
else:
    print('{} não é bissexto\n'.format(ano))
print('=' *30)



