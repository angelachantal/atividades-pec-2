# Escreva um programa que simula o valor (com duas casas decimais) da prestação de uma compra parcelada sem juros de 1x até 24x. O valor da compra é digitado pelo usuário. O valor da prestação sem juros, deve ser calculado como o valor da compra dividido pelo número de prestações de 1 até 24. O programa estará correto se o usuário informar o valor 1000 e o programa produzir o seguinte resultado:
# 1x de R$ 1000.00
# 2x de R$ 500.00
#...
# 24x de R$ 41.67

def parcelamento(valor, prestacoes):
    for count in range (24):
        prestacoes += 1
        parcela = valor/prestacoes
        print (f'{prestacoes}x de R$ {parcela:.2f}')

def main():
    valor = float(input('Valor da compra: ').strip())
    prestacoes = 0
    parcelamento(valor, prestacoes)

if __name__=='__main__':
    main()