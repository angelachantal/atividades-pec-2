# Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura de um número 0 (zero). 
# Depois, leia um valor inteiro constante. 
# O programa deve mostrar uma nova lista onde cada valor da lista original é a multiplicado pelo valor da constante.
# IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e o valor da constante e retorna uma nova lista com os elementos multiplicados.

def multiplica_constante(lista):
    multiplicador = int(input('Valor da constante: ').strip())
    produto =[]
    for numero in lista:
        numero *= multiplicador
        produto.append(numero)
    return produto

def main():
    inteiros =[]
    while True:
        numero = int(input('Digite um número inteiro: ').strip())
        if numero == 0:
            break
        else:
            inteiros.append(numero)
    print (multiplica_constante(inteiros))

if __name__=='__main__':
    main()
