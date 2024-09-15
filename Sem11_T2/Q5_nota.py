#Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem “Nota inválida.” caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar uma nota válida, o aluno deve ver seu conceito, segundo a tabela:
# Conceito A - Nota >= 8,5. 
# Conceiro B - Nota >= 7,0 
# Conceiro C - Nota >= 5,0 
# Conceito D - Nota >= 4 
# Conceito E - Nota >= 0

def main():    
    while True:
        nota = float(input('Nota: ').strip())
        if nota < 0 or nota > 10:
            print ('Nota inválida.')
        elif nota >= 8.5:
            print ('Conceito A')
            break
        elif nota >= 7.0:
            print ('Conceito B')
            break
        elif nota >= 5.0:
            print ('Conceito C')
            break
        elif nota >= 4:
            print ('Conceito D')
            break
        elif nota >= 0:
            print ('Conceito E')
            break

if __name__ == '__main__':
    main()