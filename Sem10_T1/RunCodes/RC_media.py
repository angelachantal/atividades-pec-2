def sum(soma, numero):
    soma+=numero
    return (soma)

def main():
    soma = 0    
    for count in range(100):
        n = int(input('').strip())
        soma = sum(soma,n)
    media = soma/100
    print (f'{media:.2f}')
if __name__=='__main__':
    main()