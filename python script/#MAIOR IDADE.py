#MAIOR IDADE
from datetime import date
atual = date.today().year
tmaior = 0
tmenor  = 0 
for pessoa in range(1,8):
    nasc = int(input(f'Em Que ano a {pessoa}ª nasceu? '))
    idade = atual - nasc
    if idade >= 21 :
        tmaior  += 1
    else:
        tmenor += 1
print(f'Ao todo tivemos {tmaior} maior de idade')
print(f'Ao todo tivemos {tmenor} menor de idade')
