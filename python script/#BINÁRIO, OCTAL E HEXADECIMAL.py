#BINÁRIO, OCTAL E HEXADECIMAL
num = int(input('Digite um número: '))
print('''Escolha uma opção
1 para BINÁRIO:
2 para OCTAL:
3 para HEXADECIMAL:''')
esc = int(input('Digite a opção de conversão escolhida:'))
if esc == 1 :
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif esc == 2 :
    print('{} covertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif esc == 3 :
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção ivalida!')