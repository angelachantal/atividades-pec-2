def somar(lista, numero):
    soma = 0
    for numero in lista:
        soma += numero
    print (f'{soma}')

def multiplicacar(lista, numero):
    produto = 1
    for numero in lista:
        produto *= numero
    print (f'{produto}')

def main():
    inteiros =[]
    for numero in range (10):
        numero = int(input('').strip())
        inteiros.append(numero)
    print (inteiros)
    somar(inteiros, numero)
    multiplicacar(inteiros, numero)

if __name__=='__main__':
    main()