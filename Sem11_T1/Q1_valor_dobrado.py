#Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre em quantos anos o valor acumulado será o dobro do valor inicial.

#Função cria variável vl_final correspondente à soma do deposito_inicial ao valor dos juros (vl_juros), ano a ano. Função encerra quando o valor for o dobro.
def dobro (vl_inicial, tx_juros):
    tempo = 0
    vl_final = vl_inicial
    while vl_final < (2*vl_inicial):       
        vl_juros = (vl_final*tx_juros)/100
        tempo+=1
        vl_final += vl_juros
    return tempo

def main():
    #Receber o valor informado pelo usuário para a variável deposito_inicial.
    deposito_inicial = float(input('Valor inicial da Poupança: R$ ').strip())
    
    #Receber o valor informado pelo usuário para a variáel tx_juros_aa.
    tx_juros_aa = float(input('Taxa de Juros ao Ano (%): ').strip())

    print(f'R${deposito_inicial:.2f} rendendo {tx_juros_aa:.2f}% ao ano irá dobrar em {dobro(deposito_inicial, tx_juros_aa)} anos.')


if __name__ == '__main__':
    main()