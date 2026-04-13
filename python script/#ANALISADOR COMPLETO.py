idademedia = 0
idadeh = 0
nomeh = ''
mulher20 = 0
for p in range(1,5):
    print(f'========{p}ª PESSOA')
    nome = str(input('NOME: ')).upper().strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper()
    idademedia += idade
    if p == 1 and sexo == 'M':
        idadeh = idade
        nomeh = nome
    if sexo == 'M' and idade > idadeh:
        idadeh = idade
        nomeh = nome
    if sexo == 'F'and idade < 20:
        mulher20 += 1
media = idademedia / 4
print(f'A media da idade do grupo foi de {media} anos')
print(f'O homem mais velho tem {idadeh} e se chama {nomeh}')
print(f'Ao total teve {mulher20} mulheres com menos de 20 anos')
    

