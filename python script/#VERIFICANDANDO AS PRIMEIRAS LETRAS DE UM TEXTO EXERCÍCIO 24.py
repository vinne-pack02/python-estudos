#VERIFICANDANDO AS PRIMEIRAS LETRAS DE UM TEXTO EXERCÍCIO 24

city = input('Qual é o nome da sua cidade? ')

str = city.split()[0]
a1 = 'santo' in str 

print('será que sua cidade começa com santo?\n{}'.format(a1) )
