def um_a_n (lista, numero):
    for i in range (numero):         
        lista[i] = i+1
    return lista
    
def inteiros (lista, numero):
    for i in range (numero):
        lista[i] = int(input('').strip())
    lista_inversa = lista[::-1]
    return lista

def inversa (lista, numero):
    for i in range (numero):
        lista[i] = int(input('').strip())
    lista_inversa = lista[::-1]
    return lista_inversa

def main():
    lista = []
    numero = int(input(''))

    for i in range (numero):         
        lista.append(0)

    print (lista)
    print (um_a_n(lista, numero))
    print (inteiros(lista, numero))
    print (inversa(lista, numero))

if __name__=='__main__':
    main()