#JOKENPÔ
import random
print('=' *7,"JOKENÔ GAME", '='*7)
opçoes = ['pedra','papel','tesoura']
jogador = input('\nEscolha entre PEDRA, PAPEL e TESOURA: ').strip().lower()
pc = random.choice(opçoes)
print('O PC ecolheu {}'.format(pc))
if pc == jogador :
    print('EMPATE\n')
elif (jogador == "pedra" and pc == 'tesoura') or \
     (jogador == 'papel' and pc == 'pedra') or \
     (jogador == "tesoura" and pc == "papel"):
    print('VOCÊ GANHOU!\n')
else:
    print('VOCÊ PERDEU, talvez na proxima\n')