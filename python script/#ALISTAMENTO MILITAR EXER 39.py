#ALISTAMENTO MILITAR 
from datetime import date

print('='*7 ,'ALISTAMENTO MILITAR', '='*7)
ano = int(input('Digite o ano que você nasceu guerreiro: '))
atual = date.today().year
idade = atual - ano
temp = (18 - idade) 
pas = (18 - idade) - temp * 2

if idade == 18:
    print('\njá está da hora de se alistar guerreiro.')
    print('Busque uma junta militar mais proximas\n')
    print('='*7,'PROCURE UMA JUNTA MILITAR AGORA', '='*7)

elif idade < 18:
    time = atual + temp
    print('\nopa! ainda está muito jovem guerreiro')
    print('Procure uma junta militar daqui a {} ano\n'.format(temp))
    print('Ano de alistamento certo {}\n'.format(time))
    print('='*7,'POCURE UMA JUNTA NOS PROXIMOS {} ANOS'.format(temp), '='*7,'\n')

else :
    time = atual - pas 
    print('\nVocê já passou da hora de se alistar.')
    print('Você deveria ter se alistado a {} anos atrás'.format(pas))
    print('Ano de alistamento certo {}\n'.format(time))
    print('='*7,'VOCÊ SE ATRASOU {} ANOS PARA SE ALISTAR'.format(pas), '='*7,'\n')
