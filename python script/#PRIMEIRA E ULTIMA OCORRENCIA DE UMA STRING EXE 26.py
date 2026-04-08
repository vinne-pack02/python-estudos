#PRIMEIRA E ULTIMA OCORRENCIA DE UMA STRING EXE 26
print('\n','=' *7,'ACHANDO A LETRA "A"', '='*7,'\n')
frase = input('Digite uma frase; ').strip()

a1 = frase.lower().count('a')
prima = frase.lower().find('a') +1
segun = frase.lower().rfind('a') +1

print('\ncontem', a1,'letras "a"')
print('primeira posição', prima)
print('segunda posição', segun ,'\n')
