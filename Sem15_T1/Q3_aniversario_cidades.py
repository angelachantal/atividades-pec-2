# Leia um dia e um mês como números inteiros distintos e informe as cidades que fazem aniversário nessa data.
# Veja o exemplo para o dia 9 e mês 2:
# CIDADES QUE FAZEM ANIVERSÁRIO EM 9 DE FEVEREIRO:
# São Miguel do Passa Quatro(GO)
# Centralina(MG)
# Itaporanga(PB)

def nome_mes(mes):
    if mes == 1:
        return 'JANEIRO'
    elif mes == 2:
        return 'FEVEREIRO'
    elif mes == 3:
        return 'MARÇO'
    elif mes == 4:
        return 'ABRIL'
    elif mes == 5:
        return 'MAIO'
    elif mes == 6:
        return 'JUNHO'
    elif mes == 7:
        return 'JULHO'
    elif mes == 8:
        return 'AGOSTO'
    elif mes == 9:
        return 'SETEMBRO'
    elif mes == 10:
        return 'OUTUBRO'
    elif mes == 11:
        return 'NOVEMBRO'
    elif mes ==12:
        return 'DEZEMBRO'
        
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def aniversario(dia, mes):
    cidades = carrega_cidades()
   # aniversario_cidades = cidades [0], cidades [2], cidades[3], cidades[4]
    for i in range (len(cidades)):
        municipio = cidades[i]
        if dia == municipio[3] and mes == municipio[4]:
            print (f'{municipio[2]}({municipio[0]})')
        
def main():
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    mes_extenso = nome_mes(mes)
    
    print (f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes_extenso}:')
    aniversario(dia, mes)

if __name__ == '__main__':
    main()