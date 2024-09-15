def salario_e_divida(salario, divida):
    mes = 10
    ano = 2016
    salario_atual = salario
    divida_atual = divida

    while divida_atual <= salario_atual:
        divida_atual += (divida_atual*15/100)
        mes+=1
        if mes == 3:
            salario_atual += (salario_atual*5/100)
        if mes > 12:
            mes=1
            ano+=1
    return (f'{mes}/{ano}')


def main():
    salario_inicial = float(input())
    divida_inicial = float(input())

    print(salario_e_divida(salario_inicial, divida_inicial))

if __name__ =='__main__':
    main()