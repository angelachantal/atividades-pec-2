#Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos (excluindo o zero). Dica: use repetição com teste no final 

def calc_media(n_inteiro):
    n_inicial = 0
    qtde = 0
    while n_inteiro != 0:
        n_inicial += n_inteiro
        qtde += 1
        n_inteiro = int(input('Digite outro número inteiro positivo: ').strip())
    return n_inicial/qtde

def main():
    n_inteiro = int(input('Digite um número inteiro positivo: ').strip())
    media = calc_media(n_inteiro)
    print (f'A média dos números é {media:.2f}.')

if __name__ == '__main__':
    main()