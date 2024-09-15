def sequencia_de_dez(n):
    sequencia=''
    for n in range(10,1001,10):
        if n!= 1000:
            sequencia += (f'{n}, ')
        else:
            sequencia += (f'{n}.')
    return (sequencia)

def main():
    n=0
    print(sequencia_de_dez(n))
if __name__=='__main__':
    main()