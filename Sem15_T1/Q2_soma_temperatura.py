# Utilizando a definição de valor da temperatura com tupla da questão anterior, desenvolva uma função que soma duas temperaturas que podem estar em Celsius ou em Fahrenheit. Se as duas temperaturas estiverem na mesma escala, a resposta deve estar na mesma escala. Se as temperaturas estiverem em escalas diferentes, a resposta deve ser dada na escala da segunda temperatura. Considere até 4 (quatro) casas decimais.

def converte_temp (t1, t2):  #Conversão de escalas de temperatura.
    #variáveis auxiliares para guardar os valores das temperaturas, que correspondem ao elemento 0 de cada tupla.
    temp1 = t1[0]
    temp2 = t2[0]
    
    if t1[1] != t2[1]: # condicional para verificar se as escalas (elemento 1) são diferentes.
        if t2[1] == 'F': # se a primeira escala for Fahrenheit, o segundo valor será convertido para Fahrenheit.
            temp1 = (temp1 * (9/5)) + 32
        elif t2[1] == 'C': # se a primeira escala for Celsius, o segundo valor será convertido para Celsius.
            temp1 = (temp1 - 32) * (5/9)           
    return temp1, temp2

def soma_temp(t1, t2):
    temp1, escala1 = t1
    temp2, escala2 = t2

    if escala1 != escala2:
        temp1, temp2 = converte_temp(t1, t2)
        soma = temp1 + temp2
    else:
        soma = temp1 + temp2
    
    return (soma, escala2)

def main():
    #receber o valor da 1ª temperatura e guardar na tupla temp1.
    grau_1 = float(input('Temperatura 1: ').strip())
    escala_1 = input('Escala 1 - Celsius (C) ou Fahrenheit (F): ').upper()[0]
    temp1 = (grau_1 ,escala_1)
    
    #receber o valor da 2ª temperatura e guardar na tupla temp2.
    grau_2 = float(input('Temperatura 2: ').strip())
    escala_2 = input('Escala 2 - Celsius (C) ou Fahrenheit (F): ').upper()[0]
    temp2 = (grau_2 ,escala_2)

    #soma as temperaturas e retorna o resultado na escala da segunda temperatura
    print (soma_temp (temp1, temp2))   

if __name__=='__main__':
    main()