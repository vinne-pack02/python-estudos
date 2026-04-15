#RINHA DE BOT
from colorama import init, Fore, Back, Style
import time
import random
init(autoreset=True)
print('='*7,'RINHA DE BOTS', '='*7)
time.sleep(0.5)
print(Fore.LIGHTCYAN_EX +'iniciando ...')
time.sleep(2)
print('GO!')
time.sleep(0.1)
tent = 0
while True:
    pc1 = random.randint(0,100)
    pc2 = random.randint(0,100)
    if pc1 == pc2:
        print(Fore.GREEN + f'PC1 = {pc1} ', end='')
        print(Fore.GREEN + f'PC2 = {pc2}')
        break
    else: 
        print(Fore.LIGHTYELLOW_EX + f'PC1 = {pc1} ', end='')
        print(Fore.LIGHTBLUE_EX + f'PC2 = {pc2}')
        tent += 1
        #time.sleep(0.1)
    
print(f'\nForam {tent + 1} tentativas\n')
