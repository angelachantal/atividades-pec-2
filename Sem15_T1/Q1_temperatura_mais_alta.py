# Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: temperatura e escala.
# Crie uma função que recebe duas temperaturas e retorna a mais alta. 
# Caso as temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. 
# Faça a leitura de duas temperaturas, na forma temperatura e escala (t, e) separadamente, e mostre qual é a maior. Considere até 4 (quatro) casas decimais).


def converte_temp (t1, t2):  #Conversão de escalas de temperatura.
    # variáveis auxiliares para guardar os valores das temperaturas, que correspondem ao elemento 0 de cada tupla.
    temp1 = t1[0]
    temp2 = t2[0]
    
    if t1[1] != t2[1]: # condicional para verificar se as escalas (elemento 1) são diferentes.
        if t1[1] == 'F': # se a primeira escala for Fahrenheit, o segundo valor será convertido para Fahrenheit.
            temp2 = (temp2 * (9/5)) + 32
        elif t1[1] == 'C': # se a primeira escala for Celsius, o segundo valor será convertido para Celsius.
            temp2 = (temp2 - 32) * (5/9)           
    return temp1, temp2
 

def temp_mais_alta (t1, t2):
    temp1, temp2 = converte_temp (t1, t2) #as variáveis auxiliares recebem os valores retornados pela função converte_temp
     
    if temp1 > temp2: #retorna a tupla à qual está relacionada o valor maior
        return t1
    else:
        return t2

def main(): 
    #receber o valor da 1ª temperatura e guardar na tupla temp1.
    grau_1 = float(input('Temperatura 1: ').strip())
    escala_1 = input('Escala 1 - Celsius (C) ou Fahrenheit (F): ').upper()[0]
    temp1 = (grau_1 ,escala_1)
    
    #receber o valor da 2ª temperatura e guardar na tupla temp2.
    grau_2 = float(input('Temperatura 2: ').strip())
    escala_2 = input('Escala 2 - Celsius (C) ou Fahrenheit (F): ').upper()[0]
    temp2 = (grau_2 ,escala_2)

    #compara as temperaturas e retorna a mais alta
    mais_alta = (temp_mais_alta (temp1, temp2))    
    
    print (mais_alta)

if __name__=='__main__':
    main()