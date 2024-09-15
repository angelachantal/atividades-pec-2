def troco(pr, pg):
    if pg >= pr:
        troco = pg-pr
        return (f'{troco:.2f}')
    else:
        return 'Pagamento Insuficiente'

def main():
    preco = float(input().strip())
    pagamento = float(input().strip())
    tr = troco(preco, pagamento)
    
    print (tr)

if __name__ == '__main__':
    main()