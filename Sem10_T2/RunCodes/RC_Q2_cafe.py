def versos():
    for n in range (99, 251):
        if n < 250:
            print (f'{n} bugs no software, pegue um deles e conserte...')
            print ('Tecle "Ctrl+F5"')
        else:
            print (f'{n} bugs no software, pegue um deles e conserte...')
            print ('Tecle "Ctrl+F5"')
            print ('Vamos fazer mais um café!')

def main():
    versos()
if __name__=='__main__':
    main()