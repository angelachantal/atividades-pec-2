def main():
    pessoa = 0
    soma = 0
    maior_idade = None
    menor_idade = None
    while True:
        idade = int(input())
        if idade == 0: 
            break
        else:
            pessoa +=1
            soma += idade
            media = soma/pessoa
            if maior_idade is None or idade > maior_idade:
                maior_idade = idade
            if menor_idade is None or idade < menor_idade and idade !=0:
                menor_idade = idade
        
    print (f'{pessoa}')
    print (f'{media:.2f}')
    print (f'{menor_idade}')
    print (f'{maior_idade}')
    
    

if __name__ == '__main__':
    main()