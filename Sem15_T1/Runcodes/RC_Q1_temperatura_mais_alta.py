def converte_temp (t1, t2):  
    temp1 = t1[0]
    temp2 = t2[0]
    
    if t1[1] != t2[1]: 
        if t1[1] == 'F': 
            temp2 = (temp2 * (9/5)) + 32
        elif t1[1] == 'C': 
            temp2 = (temp2 - 32) * (5/9)           
    return temp1, temp2
 

def temp_mais_alta (t1, t2):
    temp1, temp2 = converte_temp (t1, t2) 

    if temp1 > temp2:
        return t1
    else:
        return t2

def main(): 
    grau_1 = float(input().strip())
    escala_1 = input().upper()[0]
    temp1 = (grau_1, escala_1)
    
    grau_2 = float(input().strip())
    escala_2 = input().upper()[0]
    temp2 = (grau_2 ,escala_2)

    mais_alta = (temp_mais_alta (temp1, temp2))    
    
    print (mais_alta)

if __name__=='__main__':
    main()