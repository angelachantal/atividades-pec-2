#Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade de números pares e números ímpares contidos no mesmo.

def par_impar(n, pares, impares):
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    return (pares, impares)
def main():
    pares=0
    impares=0 
    for count in range(100):
        n=int(input('Informe um número: ').strip())
        pares, impares=(par_impar(n, pares, impares))
    print (pares)
    print (impares)
if __name__=='__main__':
    main()