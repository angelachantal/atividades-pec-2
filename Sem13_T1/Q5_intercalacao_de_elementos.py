#Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, cujos elementos sejam a intercalação dos elementos de A e B.

def intercalar (listaA, listaB):
    listaC =[]
    for i in range (25):
        listaC.append(listaA[i])
        listaC.append(listaB[i])
    return listaC

def main():
    listaA = []
    listaB = []

    for i in range (25):
        numeroA = int(input(f'Insira o {i+1}º número da Lista A: ').strip())
        listaA.append(numeroA)
    print (listaA)

    for i in range (25):
        numeroB = int(input(f'Insira o {i+1}º número da Lista B: ').strip())
        listaB.append(numeroB)
    print (listaB)
    
    print (intercalar(listaA, listaB))

if __name__=='__main__':
    main()