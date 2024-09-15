#Escreva um programa que mostre todos os números inteiros de 1 a 50 (um por linha).

def inteiros(n):
    for count in range(50):
        n += 1
        print(n)

def main():
    n=0
    inteiros(n)
if __name__=='__main__':
    main()
