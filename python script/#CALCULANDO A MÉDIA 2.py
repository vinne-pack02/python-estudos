#CALCULANDO A MÉDIA
not1 = float(input('Digite a primeira nota: '))
not2 = float(input('Digite a segunda nota: '))
med = (not1 + not2) / 2
if med < 5.0 :
    print('REPROVADO!')
    print('Sua media foi {}'.format(med))
elif 5.0 <= med <= 6.9 :
    print('RECUPERAÇÃO!')
    print('Sua média {}'.format(med))
else:
    print('APROVADO!')
    print('Sua média foi {}'.format(med))
    