#VALIDAÇÃO DE DADOS
from colorama import init, Fore, Back , Style
import time
init(autoreset=True)
r = ('M','F')
con = 0
while r != "M" and r != 'F':
    r = str(input('\nDigite o seu sexo [F/M]: ')).upper()
    if r != 'F' and r != 'M':
        print(Fore.LIGHTBLUE_EX + 'Analisando ...')
        time.sleep(0.8)
        print(Fore.RED + 'Sexo errado')
        print(f'Seu sexo é o que? {r}?')
        con += 1
        if con == 2:
            print(Fore.LIGHTYELLOW_EX +"\nEU TO ME ESTRESANDO JÁ CARA!")
    else:
        print(Fore.LIGHTBLUE_EX + 'Analisando ...')
        time.sleep(0.8)
        print(Fore.GREEN + '\nTUDO CERTO!\n')

