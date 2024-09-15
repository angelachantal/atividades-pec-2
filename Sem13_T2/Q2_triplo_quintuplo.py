#Escreva um programa que leia uma lista com 100 números. 
# Ao término da leitura o programa deve fazer a ordenação dos números lidos. 
# Após a ordenação, crie uma lista onde os elementos de índice par são multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
# DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.

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
        numero = int(input(f'Digite o {i+1}º número: ').strip())
        lista.append(numero)
        lista.sort()
    print (triplo_quintuplo(lista))

if __name__ == '__main__':
    main()