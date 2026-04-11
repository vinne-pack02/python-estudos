#CALCULANDO IMC 

peso = float(input('Digite quanto você pesa em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura * altura)
imc = round(imc, 2)

if imc < 18.5 :
    print('Você é abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Você está com o peso ideal')
elif 25 < imc <= 30:
    print('Você está com sobrepeso')
elif 30 < imc <= 40 :
    print('Você está com obesidade')
else:
    print('Você está com Obesidade mórbida')

print('Seu IMC deu {}'.format(imc))