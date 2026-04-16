#MAIOR E MENOR VALORES
cont = soma = maior = menor = 0
per = ''
while per != 'N':
    num = int(input('Digite um número: '))
    per = str(input('Você quer continuar [S/N]: \n')).strip() .upper()
    cont +=1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    while per != 'S' and per != 'N':
        print('Digite apenas S p/ SIM e N p/ NÃO: ')
        per = str(input('Você quer continuar [S/N]: ')).strip() .upper()  
media = soma / cont
print(f'Você dígitou {cont} diferentes, a soma entre eles deu {soma}')             
print(f'A media entre os números digitados foi {media}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')

    