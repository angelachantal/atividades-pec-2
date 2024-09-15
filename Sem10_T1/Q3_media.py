#Escreva um programa que leia um conjunto de 100 números inteiros e exiba o valor médio dos mesmos (com duas casas decimais).

def sum(soma, numero):
    soma+=numero
    return (soma)

def main():
    soma = 0    
    for count in range(100):
        n = int(input('Digite um número: ').strip())
        soma = sum(soma,n)
    media = soma/100
    print (f'{media:.2f}')
if __name__=='__main__':
    main()