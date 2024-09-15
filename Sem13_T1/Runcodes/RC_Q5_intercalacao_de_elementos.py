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
        numeroA = int(input(f'').strip())
        listaA.append(numeroA)
    print (listaA)

    for i in range (25):
        numeroB = int(input(f'').strip())
        listaB.append(numeroB)
    print (listaB)
    
    print (intercalar(listaA, listaB))

if __name__=='__main__':
    main()