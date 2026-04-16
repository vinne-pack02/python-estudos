#TABUADA v3
from colorama import init, Fore, Back, Style
import time
init(autoreset=True)
print('='*7 , 'TABUADA DE MULTIPLICAÇÃO', '='*7)
time.sleep(1)
while True:
    resp = int(input('Digite 1 p/ iniciar ou 2 p/ encerrar: '))
    if resp == 1:
        print(Fore.LIGHTBLUE_EX + 'Iniciando ...')
        time.sleep(1)
        while True:
            print('='*30)
            print('Digite um número negativo para voltar.\nEx: -2')
            n = int(input('Quer ver a tabuada de qual valor? '))
            print('='*30)
            cont = 0
            if n < 0 :
                break
            while cont < 10:
                cont += 1
                soma = cont * n
                print(Fore.LIGHTYELLOW_EX + f'{n} x {cont} = {soma}')
    elif resp == 2:
        break
    else:
        if resp != 1 and resp != 2:
            print(Fore.LIGHTRED_EX + 'Solicitação errada')
            time.sleep(1)
print(Fore.LIGHTBLUE_EX + 'TABUADA ENCERRANDO ...')
time.sleep(1)
print('\nVolte sempre!\n')
