#O custo ao consumidor, de um carro novo, é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro e escrever o custo final ao consumidor.

def custo_consumidor (custo_fabrica):
    percentual = custo_fabrica*0.28
    imposto = custo_fabrica*0.45
    return (custo_fabrica + percentual + imposto)
    

def main():
    custo_fabrica = float(input('Custo de Fábrica: ').strip())
    print (f'Custo ao consumidor: R${custo_consumidor(custo_fabrica):.2f}')

if __name__ == '__main__':
    main()