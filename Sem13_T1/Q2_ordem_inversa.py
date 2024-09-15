#Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
#a) preencha com 0 (zero) e imprima a lista;
#b) preencha com os números de 1 a n e imprima a lista;
#c) preencha com valores inteiros lidos pelo teclado e imprima a lista;
#d) preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert para sempre incluir os elementos no início da lista;


def um_a_n (lista, numero):
    for i in range (numero):         
        lista[i] = i+1
    return lista
    
def inteiros (lista, numero):
    for i in range (numero):
        lista[i] = int(input('Digite um número inteiro: ').strip())
    return lista

def inversa (lista, numero):
    for i in range (numero):
        lista[i] = int(input('Digite um número inteiro: ').strip())
    lista_inversa = lista[::-1]
    return lista_inversa

def main():
    lista = []
    numero = int(input('Quantos elementos deve ter a lista? '))
    
    for i in range (numero):         
        lista.append(0)

    print (lista)
    print (um_a_n(lista, numero))
    print (inteiros(lista, numero))
    print (inversa(lista, numero))

if __name__=='__main__':
    main()