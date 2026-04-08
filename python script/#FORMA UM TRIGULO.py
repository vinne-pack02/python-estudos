#FORMA UM TRIANGULO
print('='*7 , 'FORMA UM TRIAGULO?', '='*7,'\n')
a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))

if  a + b > c and a + c > b and b + c > a :  
    print('\nOs tres números FORMA UM TRIAGULO')
else:
    print('OS tres númeram NÃO FORMAM UM TRIAGULO')

if a == b == c :
    print('\nTriagulo equilatero')
print('\n','='*30)
