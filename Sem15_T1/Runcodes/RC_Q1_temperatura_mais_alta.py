   
def converte_temp (t1, t2):   
    if t1[1] != t2[1]:
        if t1[1] == 'F':
            t2[0] = (t2[0] * (9/5)) + 32
            t2[1] = 'F'
        elif t1[1] == 'C':
            t2[0] = (t2[0] - 32) * (5/9)
            t2 [1] = 'C'
    return t1, t2

def temperatura (t1, t2):
    temperaturas = (t1, t2)
    return temperaturas

def temp_mais_alta (t1, t2): 
   
    converte_temp (t1, t2)
    
    if t1[1] > t2[1]:
        return t1
    else:
        return t2

def main(): 
    grau_1 = float(input().strip())
    escala_1 = input().upper()[0]
    temp1 = [grau_1 ,escala_1]
    
    grau_2 = float(input().strip())
    escala_2 = input().upper()[0]
    temp2 = [grau_2 ,escala_2]

    temperaturas = temperatura (temp1, temp2)

    mais_alta = (temp_mais_alta (temp1, temp2))    
    
    print (mais_alta)

if __name__=='__main__':
    main()