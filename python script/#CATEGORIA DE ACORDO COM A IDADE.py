#CATEGORIA DE ACORDO COM A IDADE
idade = float(input('Qual é a sua idade: '))

if idade <= 9:
    print('Categoria MIRIM')

elif  10 <= idade <= 14:
    print('Categoria INFANTIL')

elif 15 <= idade <=19:
    print('Categoria JUNIOR')

elif idade == 20:
    print('Categoria SÊNIOR')
    
else:
    print('Categoria MASTER')
