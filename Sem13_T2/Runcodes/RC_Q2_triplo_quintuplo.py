def triplo_quintuplo (lista):
    lista_triplo_quintuplo =[]
    for i in range (100):
        if i%2 ==0:
            numero = 3* lista[i]
        else:
            numero = 5* lista[i]
        lista_triplo_quintuplo.append(numero)
    return lista_triplo_quintuplo

def main():
    lista =[]
    for i in range (100):
        numero = int(input().strip())
        lista.append(numero)
        lista.sort()
    print (triplo_quintuplo(lista))

if __name__ == '__main__':
    main()