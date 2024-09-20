# Fazer um programa para ler uma matriz n x m de números inteiros. Os valores de n e m são inteiros, positivos e  devem ser informados pelo usuário, calcular e armazenar em uma tupla para mostrar, respectivamente: 

def vetor(m):
    vetor = []
    for i in range(m):
        valor = int(input())
        vetor.append(valor)
    return vetor

def matriz(n,m):
    matriz = []
    for i in range (n):
        linha = vetor(m)
        matriz.append(linha)
    return matriz

# a) a soma dos elementos da primeira linha 
def soma_lin_1 (n, ler_matriz):
    soma = 0
    # ler_matriz = ler_matriz
    for i in range (n):
        valor = ler_matriz[0][i]
        soma += valor
    return soma

# b) a soma dos elementos da última coluna 
def soma_ultima_col(n,m, ler_matriz):
    soma = 0
    # ler_matriz = matriz(n,m,)
    for i in range (n):
        valor = ler_matriz[i][-1]
        soma += valor
    return soma

# c) a média de todos os elementos 
def media(n,m, ler_matriz):
    soma = 0
    # ler_matriz = matriz(n,m, ler_matriz)
    for n in range (n):
        for m in range (m):
            valor = ler_matriz[n][m]
            soma += valor
    media = soma/(n*m)
    return media

# d) o menor elemento 
def menor(n,m, ler_matriz):
    menor = ler_matriz[0] [0]
    for n in range(n):
        for m in range(n):
            if ler_matriz[n][m] < menor:
                menor = ler_matriz[n][m]
    return menor

# e) o maior elemento 
def maior(n,m, ler_matriz):
    maior = ler_matriz[0] [0]
    for n in range(n):
        for m in range(n):
            if ler_matriz[n][m] > maior:
                maior = ler_matriz[n][m]
    return maior

def main():
    n = int(input())
    m = int(input())
    ler_matriz = matriz(n,m)
    tupla = (soma_lin_1(n, ler_matriz), soma_ultima_col(n,m, ler_matriz), media(n,m, ler_matriz), menor(n,m, ler_matriz), maior(n,m, ler_matriz))
    print (tupla)
if __name__=='__main__':
    main()