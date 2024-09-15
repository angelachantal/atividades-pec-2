def maior_menor(n_inteiro):
    maior = n_inteiro
    menor = n_inteiro
    if n_inteiro <=0:
        print ()
    else:
        while n_inteiro != 0:
            if n_inteiro > maior and n_inteiro > menor:
                maior = n_inteiro
            elif n_inteiro < maior and n_inteiro < menor:
                menor = n_inteiro
            n_inteiro = int(input().strip())
        return (f'{maior}\n{menor}')

def main():
    n_inteiro = int(input().strip())

    print (f'{maior_menor(n_inteiro)}')
    
if __name__ == '__main__':
    main()