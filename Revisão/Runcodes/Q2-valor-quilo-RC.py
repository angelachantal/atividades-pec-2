def preco(valor_kg, kg):
    preco = valor_kg * kg
    return preco   

def main():
    valor = float(input().strip())
    consumo = float(input().strip())
    total = preco(valor, consumo)
    
    print (f'{total:.2f}')
    
if __name__=='__main__':
    main()
