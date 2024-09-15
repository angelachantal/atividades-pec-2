def invertido (numero):
    numero_invertido = 0
    while numero != 0:
        digito = numero%10
        numero_invertido = (numero_invertido*10)+digito
        numero = numero//10
    return numero_invertido


def main():
    numero = int(input())

    print (invertido(numero))

if __name__ =='__main__':
    main()