#PALINDROMO
for c in range(0,2):
    frase = str(input('Digite uma frase: ')).strip() .upper()
    sem = frase.replace(' ','')
    inver = sem[::-1]
print(f'O inverso de {sem} é {inver}')
if inver == sem:
    print('é uma palíndromo')
else:
    print('não é um palíndromo')

