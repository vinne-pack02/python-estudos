#GERENCIADOR DE PAGAMENTOS

produto = float(input('Qual o valor do produto:R$ '))
print('='*7,'FORMA DE PAGAMENTO','='*7)
print("""DIGITE 1 PARA DINHEIRO:
DIGITE 2 PARA DEBITO:
DIGITE 3 PARA CRTÃO DE CREDITO 2X:
DIGITE 4 PARA CARTÃO DE CREDITO 3X:""""")

pag = int(input('Digite a forma de pagamento desejada: '))

if pag == 1 :
    des = produto - (produto * 0.1)
    v = 'Você teve um desconto de 10%'   
elif pag == 2 :
    des = produto - (produto * 0.05)
    v = 'Você teve um desconto de 5%'  
elif pag == 3 :
    des = produto
    v = 'valor normal'
elif pag == 4 :
    des = produto + (produto * 0.20)
    v = 'Você teve um juros de 20% sob o valor do produto'

print('O valor do produto é R$ {:.2f}'.format(produto))
print(v)
print('valor final a pagar R$ {:.2f}'.format(des))






    
