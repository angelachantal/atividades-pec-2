# Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de
# um número 0 (zero). 
# O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos anteriores da lista original.
# IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna uma lista com a soma cumulativa. Por exemplo:

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
        numero = float(input('Digite um número real: ').strip())
        if numero == 0:
            break
        else:
            reais.append(numero)
    print(soma_cumulativa(reais))

if __name__=='__main__':
    main()
