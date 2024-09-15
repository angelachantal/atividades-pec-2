def multiplica_constante(lista):
    multiplicador = int(input().strip())
    produto =[]
    for numero in lista:
        numero *= multiplicador
        produto.append(numero)
    return produto

def main():
    inteiros =[]
    while True:
        numero = int(input().strip())
        if numero == 0:
            break
        else:
            inteiros.append(numero)
    print (multiplica_constante(inteiros))

if __name__=='__main__':
    main()
