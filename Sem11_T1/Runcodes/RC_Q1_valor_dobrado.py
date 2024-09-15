def dobro (vl_inicial, tx_juros):
    tempo = 0
    vl_final = vl_inicial
    while vl_final < (2*vl_inicial):
        vl_juros = (vl_final*tx_juros)/100
        tempo+=1
        vl_final += vl_juros
    return tempo


def main():
    deposito_inicial = float(input().strip())
    tx_juros_aa = float(input().strip())

    print(f'{dobro(deposito_inicial, tx_juros_aa)}')

if __name__ == '__main__':
    main()