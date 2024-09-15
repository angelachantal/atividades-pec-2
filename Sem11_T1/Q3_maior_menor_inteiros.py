#Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos (excluindo o zero). Dica: use repetição com teste no final

def maior_menor(n_inteiro):
    maior = n_inteiro
    menor = n_inteiro
    if n_inteiro <=0:
        print ('O número deve ser maior que zero.')
    else:
        while n_inteiro != 0:
            if n_inteiro > maior and n_inteiro > menor:
                maior = n_inteiro
            elif n_inteiro < maior and n_inteiro < menor:
                menor = n_inteiro
            n_inteiro = int(input('Digite outro número inteiro positivo: ').strip())
        return (f'Maior número: {maior}\nMenor número: {menor}')

def main():
    n_inteiro = int(input('Digite um número inteiro positivo: ').strip())

    print (f'{maior_menor(n_inteiro)}')
    
if __name__ == '__main__':
    main()