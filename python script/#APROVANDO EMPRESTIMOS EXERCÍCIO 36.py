#APROVANDO EMPRESTIMOS
print('='*7,'APROVANDO EMPRÉSTIMO', '='*7, '\n')
cvalor = int(input('Qual é o valor da casa? R$ '))
salario = int(input('Qual é o seu sálario? R$ '))
anos = int(input('Quantos anos você deseja pagar? '))

parcela = anos *12 
pag = cvalor / parcela
porc = (pag / salario) *100

if porc <= 30 :

    print('='*7,'FINANCIAMENTO APROVADO', '='*7,)
    print('\nParabéns emprestimo aprovado!\nVocê vai pagar {} parcelas de R$ {:.2f} durante {} anos'.format(parcela , pag , anos))
    print('Porcentagem de parcela por salario é {:.2f}%\n'.format(porc))
    

elif porc > 30 :

    print('='*7,'FINANCIAMENTO NÃO APROVADO', '='*7,)
    print("""\nInfelismente seu emprestimo não foi aprovado!
Você excedeu o limite de 30% do salario.
Porcentagem em parcelas do seu salario deu {:.2f}%\n""".format(porc))

print('='*40)






