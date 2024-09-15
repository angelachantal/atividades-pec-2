def converte_temp (t1, t2):
    temp1 = t1[0]
    temp2 = t2[0]
    
    if t1[1] != t2[1]:
        if t2[1] == 'F':
            temp1 = (temp1 * (9/5)) + 32
        elif t2[1] == 'C':
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
    grau_1 = float(input().strip())
    escala_1 = input().upper()[0]
    temp1 = (grau_1 ,escala_1)
    
    grau_2 = float(input().strip())
    escala_2 = input().upper()[0]
    temp2 = (grau_2 ,escala_2)

    print (soma_temp (temp1, temp2))   

if __name__=='__main__':
    main()