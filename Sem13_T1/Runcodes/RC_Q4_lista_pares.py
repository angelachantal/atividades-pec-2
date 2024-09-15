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
        numero = int(input(f''))
        inteiros.append(numero)
    print (inteiros)
    print (pares(inteiros))
    print (impares(inteiros))
if __name__=='__main__':
    main()