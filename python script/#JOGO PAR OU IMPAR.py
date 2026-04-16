#JOGO PAR OU IMPAR
from colorama import init, Fore, Back, Style
import random
init(autoreset=True)
print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*30)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    esc = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('='*30)
    pc = random.randint(0,10)
    soma = pc + jogador
    print(f'Voce jogou {jogador} e p PC {pc}. Total de {soma}')
    print('='*30)
    if soma % 2 == 0:
        print(Fore.LIGHTYELLOW_EX + 'PAR')
        if esc == 'P':
            print('Você',Fore.LIGHTGREEN_EX + 'GANHOU')
            cont += 1
        else:
            print('Você',Fore.LIGHTRED_EX + 'PERDEU')
            break
    else:
        print(Fore.LIGHTWHITE_EX +'ÍMPAR')
        if esc == 'I':
            print('Você',Fore.LIGHTGREEN_EX + 'GANHOU')
            cont += 1
        else:
            print('Você',Fore.LIGHTRED_EX + 'PERDEU')
            break
print(f'Você venceu {cont} vezes')
