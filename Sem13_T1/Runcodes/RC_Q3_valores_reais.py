def inversa (lista, n):
    for i in range (n):
        numero = float(input('').strip())
        numero = float((f'{numero:.4f}'))
        lista.insert (0,numero)
    return lista

def notas (lista, n):
    if n == 0:
        return lista
    else:
        for i in range (n):
            nota = float(input('').strip())
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
        letra = input('')[0]
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
    n = int(input('').strip())

    lista =[]
    print (inversa (lista, n))

    lista2 =[]
    print (notas(lista2, n))
    print (media(lista2, n))

    lista3 =[]
    letras (lista3, n)

if __name__=='__main__':
    main()