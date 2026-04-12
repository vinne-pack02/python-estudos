#PROGRESSÃO ARITMÉTICA
import time
print('='*7,'CALCULANDO TERMOS DE UMA PA', '='*7)
a1 = float(input('Digite o primeiro termo: '))
r = float(input('Digite a razão: '))
print('Calculando ...')
time.sleep(2)

for n in range(1,11):
    an = a1 + (n - 1)* r
    print(f'{n}º termo = {an}')
    print('§')
    time.sleep(0.15)
   
print('='*30)