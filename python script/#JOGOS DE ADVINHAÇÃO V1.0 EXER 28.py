#JOGOS DE ADVINHAÇÃO V1.0 EXER 28
import random
print('\n', '='*7, 'JOGO DE ADIVINHAÇÃO V1.0', '='*7)
print("""
Irei escolher um número entre 0 e 5.
      
será que vocé acerta qual será?
""")
numero = int(input('Digite o número escolhido: '))
a1 = random.randint(0, 5)

if numero == a1:
    print('o número foi {}\n \nWow, Você é foda meu nobre\n'.format(a1))

else:
    print('o número foi {}\nQue pena, tente na proxima\n'.format(a1))

print('=' *7 , 'FIM DE JOGO', '=' *7)    