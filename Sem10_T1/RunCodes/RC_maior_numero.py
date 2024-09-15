def n_maior(maior, n):
    if n > maior:
        maior = n
    else:
        maior = maior
    return maior
def main():
    maior = 0
    for count in range(100):
        n=int(input('').strip())
        maior = n_maior(maior, n)
    print (maior)    

if __name__=='__main__':
    main() 