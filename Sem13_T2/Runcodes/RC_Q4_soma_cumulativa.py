def soma_cumulativa(lista):
    lista_soma_cumulativa=[]
    soma = 0
    for numero in lista:
        soma += numero
        lista_soma_cumulativa.append(soma)
    return lista_soma_cumulativa

def main():
    reais =[]
    while True:
        numero = int(input().strip())
        if numero == 0:
            break
        else:
            reais.append(numero)
    print(soma_cumulativa(reais))

if __name__=='__main__':
    main()
