#Escreva um programa que, para um número indeterminado de pessoas: (a) leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag) e não deve ser considerada; (b) calcule e escreva o número de pessoas; (c) calcule e escreva a idade média do grupo; (d) calcule e escreva a menor idade e a maior idade.

def main():
    pessoa = 0
    soma = 0
    maior_idade = None
    menor_idade = None
    while True:
        idade = int(input('Digite sua idade, ou 0 (zero) para sair: '))
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
        
    print (f'Em um grupo de {pessoa} pessoas, a idade média é {media:.2f}. A maior idade é {maior_idade} anos, e a menor é {menor_idade} anos.')
    

if __name__ == '__main__':
    main()