#Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

def pares(inteiro):
    par =[]
    for numero in inteiro:
        if numero % 2 == 0:
            par.append(numero)
    return par

def impares(inteiro):
    impar =[]
    for numero in inteiro:
        if numero % 2 != 0:
            impar.append(numero)
    return impar

def main():
    inteiros =[]
    for i in range (20):
        numero = int(input(f'Digite o {i+1}º número: '))
        inteiros.append(numero)
    print (inteiros)
    print (pares(inteiros))
    print (impares(inteiros))
if __name__=='__main__':
    main()