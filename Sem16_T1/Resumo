
# Concatenar elementos de uma lista em outra:
lista =[]
lista.extend([i])

# Gerar uma lista dinamicamente (Gerador):
anos = (ano for ano in range(1983, 2025)) #tupla
anos = [ano for ano in range(1983, 2025)] #lista

# Retornar valores gerados pelo gerador usando for:
for ano in anos:
    print (ano)

# Retornar valores gerados pelo gerador usando for:
next (anos)

# Array = lista onde os elementos simples são homogêneos
# Array unidimencional = vetor
    # Elemento é acessado por apenas um índice: vetor[i]
# Array bimendicional = matriz = conjunto de vetores
    # Elemento é acessado por dois índices: matriz [i], [ii]
# Array tridimenconal = conjunto de matrizes
# Array multidimencional
    # Elemento é acessado por três ou mais índices: array [i], [ii], [iii]

# Preenchendo uma matriz:
    # Cada elemento da matriz é uma lista do tipo vetor
    # Receber a quantidade de linhas e a quantidade de colunas
linhas = input()
colunas = input()

def preencher_matriz(linhas, colunas):
    matriz =[]
    for lin in range(linhas):
        linha =[] #vetor
        for col in range(colunas):
            linha.append(randint(0,50))
        matriz.append(linha)
