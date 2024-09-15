#Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação: A condição de saída do laço será a leitura do valor 0 (flag).

def main():
    soma = 0
    while True:
        numero = int(input('Digite um número inteiro: ').strip())
        if numero == 0: 
            break
        else:
            soma += numero
    print(soma)

if __name__=='__main__':
    main()