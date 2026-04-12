#SOMANDO PARES
import time
soma = 0
for c in range(1,1000):
    print(c)
    time.sleep(0.5)
    #num = int(input(f'Digite o {c}º número: '))
    if c % 2 == 0:
        soma += c
print(f'a soma dos número PARES é igual a {soma}')

