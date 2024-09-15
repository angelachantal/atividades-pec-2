# Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: temperatura e escala.
# Crie uma função que recebe duas temperaturas e retorna a mais alta. 
# Caso as temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. 
# Faça a leitura de duas temperaturas, na forma temperatura e escala (t, e) separadamente, e mostre qual é a maior. Considere até 4 (quatro) casas decimais).
    
def converte_temp (t1, t2):   
    #Conversão de escalas de temperatura.
    if t1[1] != t2[1]:
        if t1[1] == 'F':
            t2[0] = (t2[0] * (9/5)) + 32
            t2[1] = 'F'
        elif t1[1] == 'C':
            t2[0] = (t2[0] - 32) * (5/9)
            t2 [1] = 'C'
    t2[0] = f'{t2[0]:.4}'
    t1[0] = f'{t1[0]:.4}'
    return t1, t2
 

def temp_mais_alta (t1, t2): 
    temp1 = t1
    temp2 = t2
    temperaturas = (t1, t2)
    
    converte_temp (t1, t2)
    if t1[1] > t2[1]:
        return temperaturas[0]
    else:
        return temperaturas[1]

def main(): 
    #receber o valor da 1ª temperatura e guardar na lista temp1.
    grau_1 = float(input('Temperatura 1: ').strip())
    escala_1 = input('Escala 1 - Celsius (C) ou Fahrenheit (F): ').upper()[0]
    temp1 = [grau_1 ,escala_1]
    
    #receber o valor da 1ª temperatura e guardar na lista temp2.
    grau_2 = float(input('Temperatura 2: ').strip())
    escala_2 = input('Escala 2 - Celsius (C) ou Fahrenheit (F): ').upper()[0]
    temp2 = [grau_2 ,escala_2]

    #compara as temperaturas e retorna a mais alta
    mais_alta = (temp_mais_alta (temp1, temp2))    
    
    print (mais_alta)

if __name__=='__main__':
    main()