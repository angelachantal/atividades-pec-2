def calc_media(n_inteiro):
    n_inicial = 0
    qtde = 0
    while n_inteiro != 0:
        n_inicial += n_inteiro
        qtde += 1
        n_inteiro = int(input().strip())
    return n_inicial/qtde

def main():
    n_inteiro = int(input().strip())
    media = calc_media(n_inteiro)
    print (f'{media:.2f}')

if __name__ == '__main__':
    main()