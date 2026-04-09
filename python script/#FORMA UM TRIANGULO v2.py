#FORMA UM TRIANGULO v2
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: ')) 
c = float(input('Digite a terceira reta: '))

if  a + b > c and a + c > b and b + c > a :  
    print('\nOs tres números FORMA UM TRIAGULO')
    if a==b==c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('OS tres númeram NÃO FORMAM UM TRIAGULO')
