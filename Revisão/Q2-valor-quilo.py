#Escreva um algoritmo/programa que receba o valor do quilo de um produto e a quantidade de quilos consumida desse produto. Calcule e exiba o valor final a ser pago.

def preco(valor_kg, kg):
    preco = valor_kg * kg
    return preco   

def main():
    valor = float(input('Preço do kg: R$ ').strip())
    consumo = float(input('Peso: ').strip())
    total = preco(valor, consumo)
    
    print (f'Total a pagar: R$ {total:.2f}')
    
if __name__=='__main__':
    main()
