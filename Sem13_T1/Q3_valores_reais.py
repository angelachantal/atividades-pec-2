#3. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
#a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais.
#b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. Se n = 0, imprima “SEM NOTAS”.
#c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
#Dica: certifique-se de ler apenas um caractere com input()[0]

def inversa (lista, n):
    for i in range (n):
        numero = float(input('Digite um número real: ').strip())
        numero = float((f'{numero:.4f}'))
        lista.insert (0,numero)
    return lista

def notas (lista, n):
    if n == 0:
        return lista
    else:
        for i in range (n):
            nota = float(input(f'Digite a Nota {i+1}: ').strip())
            lista.append(nota)
    return lista
        
def media (lista2, n):
    if n == 0:
        return ('SEM NOTAS')
    else:
        soma = 0
        for i in range(n):
            soma += lista2[i]
        media = soma/n
        return (f'{media:.1f}')

def letras (lista, n):
    for i in range (n):
        letra = input('Digite uma letra: ')[0]
        lista.append(letra)
    vogal(lista)
    consoante (lista)

def vogal(lista):
    vogal=0
    for i in lista:
        if i in 'aeiouAEIOU':
            vogal+=1
    print (vogal)
    
def consoante(lista):
    consoantes=[]
    for letra in lista:
        if letra in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            consoantes.append(letra)
    print(consoantes)    

def main():
    n = int(input('Quantos elementos tem a lista que deseja criar? ').strip())

    lista =[]
    print (inversa (lista, n))

    lista2 =[]
    print (notas(lista2, n))
    print (media(lista2, n))

    lista3 =[]
    letras (lista3, n)

if __name__=='__main__':
    main()