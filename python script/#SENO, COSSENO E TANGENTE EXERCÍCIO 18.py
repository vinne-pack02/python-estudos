#SENO, COSSENO E TANGENTE EXERCÍCIO 18
import math
print('='*7,"CALCULANDO O SENO, COSSENO E TANGENTE", '='*7)

grau = int(input('digite o grau; '))
seno = math.sin(math.radians(grau))
coss = math.cos(math.radians(grau))
tan = math.tan(math.radians(grau))

print('\nO seno é {:.4f}\nO cosseno é {:.4f}\nA tangente é {:.4f}'.format(seno,coss,tan))