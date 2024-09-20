# Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ... ).

# Converter int(mês) para string(mês:
def nome_mes(mes):
    if mes == 1:
        return 'Janeiro'
    elif mes == 1:
        return 'Fevereiro'
    elif mes == 2:
        return 'Março'
    elif mes == 3:
        return 'AbrilL'
    elif mes == 4:
        return 'Maio'
    elif mes == 5:
        return 'Junho'
    elif mes == 6:
        return 'Julho'
    elif mes == 7:
        return 'Agosto'
    elif mes == 8:
        return 'Setembro'
    elif mes == 9:
        return 'Outubro'
    elif mes == 10:
        return 'Novembro'
    elif mes ==11:
        return 'Dezembro'
    
# Converter para °K:
def converte_kelvin():
    temp_mes=temperatura_mes()
    escala = temp_mes[1]
    temperatura = temp_mes[0][1]
    if escala == 'C':
        temperatura_k = temperatura + 273,15 
    elif escala == 'K':
        temperatura_k = (temperatura - 32) * 5/9 + 273,15
    else:
        temperatura_k = temperatura
    temperatura_k[2]=K
    return temperatura_k

#Receber a temperatura média de cada mês do ano (°C, °F, ou °K)
def temperatura_mes():
    # mes = int(input('Mês (informe em número): '))
    temperatura_mes = [O,O]
    for i in range (12):
        temperatura = float(input('Temperatura Média do Mês: '))
        escala = input('Escala (C, F ou K): ').upper()[0].strip()
        temperatura = converte_kelvin()
        temperatura_mes.append([temperatura] [escala]
    return temperatura_mes

# Calcular a média anual:
def temp_media_anual():
    temp_mensal = temperatura_mes()
    mes = temperatura_mes [0]
    # temperatura = temperatura_mes[1]
    soma = 0
    for i in range (12):
        soma += temperatura_mes[i][1]
    media = soma/12
    return media

# Retornar as temperaturas maiores que a média anual e respectivo mês:
def temp_maior_que_media():
    temperaturas_por_mes = []
    media_anual = temp_media_anual()

    for mes in range (12):
        if temperatura_mes[mes][1] > media_anual:
            mes = nome_mes(mes)
            temperaturas_por_mes.append(temperatura_mes())
    return f'{mes}: {temperaturas_por_mes[0]}{temperaturas_por_mes[1]}'

def main():
    print ("TEMPERATURA MÉDIA ANUAL")
    print (f'{temp_media_anual()}K')
    print ("TEMPERATURAS ACIMA DA MÉDIA ANUAL")
    print (temp_maior_que_media())

if __name__=='__main__':
    main()