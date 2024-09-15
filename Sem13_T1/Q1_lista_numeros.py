#Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.
def somar(lista, numero):
    soma = 0
    for numero in lista:
        soma += numero
    print (f'Soma: {soma}')

def multiplicacar(lista, numero):
    produto = 1
    for numero in lista:
        produto *= numero
    print (f'Produto: {produto}')

def main():
    inteiros =[]
    for numero in range (10):
        numero = int(input('Digite um número inteiro: ').strip())
        inteiros.append(numero)
    print (inteiros)
    somar(inteiros, numero)
    multiplicacar(inteiros, numero)

if __name__=='__main__':
    main()