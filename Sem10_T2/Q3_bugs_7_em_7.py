# Modifique a canção dos programadores novamente para aumentar os bugs de 7 em 7, iniciando em 99 e parando em 250 ou antes.

def versos():
    for n in range (99, 251, 7):
        print (f'{n} bugs no software, pegue sete deles e conserte...')
        print ('Tecle "Ctrl+F5"')

def main():
    versos()
    print ('Vamos fazer mais um café!')
if __name__=='__main__':
    main()