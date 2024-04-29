# Modifique mais um vez a canção dos programadores, dessa vez, gerando a canção dos bons programadores, que resolvem 11 erros de cada vez e ao chegar a zero declaram que o software está estabilizado. Atenção para o exemplo a seguir, especialmente, os versos finais.
# 99 bugs no software, pegue onze deles e conserte...
# Tecle “Ctrl+F5”
# ...
# 11 bugs no software, pegue onze deles e conserte...
# Tecle “Ctrl+F5”
# Sem erros no software! Está estabilizado!

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