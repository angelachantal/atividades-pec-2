# Modifique a canção dos programadores do exercício anterior para incluir o refrão: Tecle “Ctrl+F5”. Termine a canção com “Vamos fazer mais um café!”.
# 99 bugs no software, pegue um deles e conserte...
# Tecle “Ctrl+F5”
# ...
# 250 bugs no software, pegue um deles e conserte...
# Tecle “Ctrl+F5”
# Vamos fazer mais um café!
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