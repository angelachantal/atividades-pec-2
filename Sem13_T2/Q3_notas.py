# Escreva um programa que leia a nota de 50 alunos. 
# Mostre uma lista apenas com os índices dos alunos que têm nota maior ou igual a 6 (seis).

def alunos_na_media(notas):
    lista_media=[]
    for i in range (50):
        if notas[i] >= 6:
            lista_media.append(i)
    return lista_media

def main():
    notas=[]

    for i in range (50):
        nota_aluno = float(input(f'Nota do aluno nº {i}: '))
        notas.append(nota_aluno)

    print (alunos_na_media(notas))

if __name__=='__main__':
    main()

