#RADAR ELETRONICO EXERCÍCIO 29
print('='*7, 'RADAR ELETRONICO', '='*7)
km = int(input('Digite a velocidade atingida no radar: '))
limit = 80
if km > limit :
    ext = km - limit
    pag = float(ext * 7)
    print('\nOpa! MULTADO\n')
    print('Ultrapassou o limite permitido de 80 km')
    print('voce passou {} km a mais do permitido'. format(ext))
    print('\no valor da multa será de R${:.2f}\n'.format(pag))

else:
    print('\nTudo certo, voce está no limite permitido de velocidade\n')
print('='*30)