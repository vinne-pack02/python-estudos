#CATETOS E HIOTENUSA EXERCÍCIO 17
import math
print('=' *7 , 'CALCULANDO A HIPOTENUSA', '=' *7)

cat = float(input('digite a cateto adijacente; '))
op = float(input('digite o cateto oposto; '))
hypo = math.hypot(cat,op)

print('=' *30,'\no valor da hipotenusa é igual a {}'.format(hypo))
print('\n|' *4,'thank u ;)', '\n|' *3)