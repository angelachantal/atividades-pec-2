#Escreva um algoritmo/programa que receba o valor do preço de produto e o valor pago pelo cliente. Calcule e exiba o valor do troco a ser dado.

def troco(pr, pg):
    if pg >= pr:
        troco = pg-pr
        return (f'Troco: R$ {troco:.2f}')
    else:
        return 'Pagamento Insuficiente'

def main():
    preco = float(input('Preço do produto: R$ ').strip())
    pagamento = float(input('Valor pago: R$ ').strip())
    tr = troco(preco, pagamento)
    
    print (tr)

if __name__ == '__main__':
    main()