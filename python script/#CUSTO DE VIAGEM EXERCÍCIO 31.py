#CUSTO DE VIAGEM
print('\n','=' *7, 'CALCULANDO O VALOR DA PASSAGEM', '=' *7)

km = int(input('\nQuantos km será a viagem? ')) 
pag1 = 200

if km <= pag1:
    pag2 = (km * 0.5)

    print('sua viagem tem {}km'.format(km))
    print('voce vai pagar R${:.2f}'.format(pag2))

else:
    km > pag1
    pag3 = (km * 0.45)

    print('sua viagem tem {}km'.format(km))
    print('voce vai pagar R${:.2f} \n'.format(pag3))

print('=' *30 , '\n')


