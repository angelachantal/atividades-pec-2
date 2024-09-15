def versos(n):
    for count in range (0, 99, 11):
        n-=11
        print (f'{n} bugs no software, pegue onze deles e conserte...')
        print ('Tecle "Ctrl+F5"')

def main():
    n=110
    versos(n)
    print ('Sem erros no software! Está estabilizado!')
if __name__=='__main__':
    main()