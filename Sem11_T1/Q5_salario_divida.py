#Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. Pedro também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. Considerando que a situação se refere ao mês de outubro do ano de 2016, faça um programa leia o valor do salário e o valor da dívida e calcula, simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com o cartão de crédito será superior ao seu próprio salário. Represente os meses como inteiros de 1 a 12.
#Dica: Controle essas quatro variáveis:
# “dívida” que aumenta todo mês;
# “salário” que aumenta apenas se o número do mês for 3 (março);
# “mês” que é incrementado sempre, mas que retorna a 1 quando passar de 12;
# “ano” que só é incrementado quando o mês retornar a 1.
#Por exemplo: Considerando que o salário inicial é de R$ 2.000,00 e o valor da dívida é R$ 100,00 o valor da dívida irá superar o salário em setembro de 2018 (9/2018)

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
    return (f'Considerando que o salário inicial é de R$ {salario:.2f} e o valor da dívida é R$ {divida:.2f} o valor da dívida irá superar o salário em {mes}/{ano})')


def main():
    salario_inicial = float(input('Salário Inicial: '))
    divida_inicial = float(input('Dívida Inicial: '))

    print(salario_e_divida(salario_inicial, divida_inicial))

if __name__ =='__main__':
    main()