# Leia um mês e uma população. Mostre as cidades com população maior que o valor lido fazem aniversário no mês informado.
# Veja o exemplo para o mês com valor 4 e 50000 para a população:
# CIDADES COM MAIS DE 50000 HABITANTES E ANIVERSÁRIO EM ABRIL:
# Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril.
# Itacoatiara(AM) tem 84676 habitantes e faz aniversário em 25 de abril.
# Araci(BA) tem 51912 habitantes e faz aniversário em 7 de abril.
# Fortaleza(CE) tem 2431415 habitantes e faz aniversário em 13 de abril.

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

def populacao_maior (mes, pop):
    cidades = carrega_cidades()

    for i in range (len(cidades)):
        municipio = cidades[i]
        if municipio[5] > pop and municipio[4]==mes:
            mes_extenso = nome_mes(mes).lower()
            print(f'{municipio[2]}({municipio[0]}) tem {municipio[5]} habitantes e faz aniversário em {municipio[3]} de {mes_extenso}.')

def main():
    mes = int(input('Mês: '))
    mes_extenso = nome_mes(mes)
    populacao = int(input('População: '))

    print (f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {mes_extenso}:')
    populacao_maior(mes, populacao)


if __name__=='__main__':
    main()