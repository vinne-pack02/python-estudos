#TABUADA v2
import time
num = int(input('Dgite um número: '))
for c in range(1,11):
    m = c * num
    print(f'{num} x {c:2d} = {m:3d}')
    time.sleep(0.15)
    

