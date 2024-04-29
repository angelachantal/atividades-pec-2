def parcelamento(valor, prestacoes):
    for count in range (24):
        prestacoes += 1
        parcela = valor/prestacoes
        print (f'{prestacoes}x de R$ {parcela:.2f}')

def main():
    valor = float(input('').strip())
    prestacoes = 0
    parcelamento(valor, prestacoes)

if __name__=='__main__':
    main()