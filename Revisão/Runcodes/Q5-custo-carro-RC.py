def custo_consumidor (custo_fabrica):
    percentual = custo_fabrica*0.28
    imposto = custo_fabrica*0.45
    return (custo_fabrica + percentual + imposto)
    

def main():
    custo_fabrica = float(input().strip())
    print (f'R$ {custo_consumidor(custo_fabrica):.2f}')

if __name__ == '__main__':
    main()