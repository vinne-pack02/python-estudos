#IMPAR DIVISIVEL POR 3
import time
contador = 0
for c in range(1,501,2):
    if c % 3 == 0 :
        print(f'{c:4d}', end='')
        contador += 1
        time.sleep(0.15)
print('teve ao total {} números impares divisivel por 3'.format(contador))
