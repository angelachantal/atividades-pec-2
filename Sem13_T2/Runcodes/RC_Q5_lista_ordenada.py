def criar_lista(n):
    lista = []
    for i in range (n):
        valor = input().strip()
        try:
            valor = int(valor)
            lista.append(valor)
        except ValueError:
            try: 
                valor=float(valor)
                lista.append(valor)
            except ValueError:
                lista.append(valor)
    return lista

def esta_ordenada(lista):
    lista_ordenada = sorted(lista)
    if lista == lista_ordenada:
        return True
    else:
        return False
def main():
    n = int(input())
    
    lista = criar_lista(n)

    if esta_ordenada(lista) == True:
        print ('LISTA ORDENADA')
    else:
        print ('LISTA NÃO ORDENADA')
        
if __name__=='__main__':
    main()