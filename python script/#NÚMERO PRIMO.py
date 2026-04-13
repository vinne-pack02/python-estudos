from colorama import init, Fore, Back, Style
init(autoreset=True)

num = int(input("Digite um número inteiro: "))
tot = 0 
for c in range(1 , num + 1):
    if num % c == 0:
        print(Fore.RED + f'{c} ', end='')
        tot += 1 
    else:
        print(Fore.YELLOW + f'{c} ', end='')

print(f'\no úmero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('é por isso ele é primo')
else:
    print('é por isso ele não é primo')