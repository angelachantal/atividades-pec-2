# Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. 
# O programa # deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso.
# IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso. 

def esta_ordenada(lista):
    lista_ordenada = sorted(lista)
    if lista == lista_ordenada:
        return True
    else:
        return False
def main():
    lista=[]
    n = int(input('Quantos elementos deve conter a lista? '))
    for i in range (n):
        valor = input(f'Digite o {i+1}º elemento da lista: ').strip()
        lista.append(valor)

    if esta_ordenada(lista) == True:
        print ('LISTA ORDENADA')
    else:
        print ('LISTA NÃO ORDENADA')
        
if __name__=='__main__':
    main()