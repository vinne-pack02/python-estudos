#JOGO DE ADIVINHAÇÃO v2
from colorama import init, Fore, Back, Style
import time
import random
init(autoreset=True)

pc = random.randint(0,10)
jogador = 0
erro = 0
acerto = 0
print('='*7,'JOGO DE ADIVINHAÇÃO v3','='*7)
print('O PC iré escolher 1 numero entre 0 a 10.\nTente adivinhar')
while  jogador != pc:
    print(Fore.LIGHTBLUE_EX + 'Escolhendo ...')
    time.sleep(1)
    jogador = int(input('Digite um numero: '))
    if jogador == pc :
        acerto += 1
        print(Fore.GREEN + 'PARABÉNS!')
    if jogador != pc:
        erro += 1
        print(Fore.RED + 'ERROU!')
tentativa = erro + acerto
print(f'Você acertou na {tentativa}ª tentativa')
if erro > 1:
    print(f'Você teve {erro} ERROS')
else:
    print(f'Você teve {erro} ERRO')