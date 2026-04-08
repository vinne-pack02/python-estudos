#MAIOR E MENOR VALORES
print('='*7 ,'maióRrR E menóRrR MEU NOBRE', '='*7 ,'\n' )
a = int(input('Digite um número: '))
b = int(input('Agora mais um número: '))
c = int(input('Ultimo número: '))

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a < b and a < c:
    menor = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a > b and a > c:
    maior = a
     
    print('o menor valor digitado  foi {}\n'.format(maior))
    print('o menor valor digitado  foi {}\n'.format(menor))

 #print('='*7, 'SOBROU NADA PRO BETA', '=', *7)


    
