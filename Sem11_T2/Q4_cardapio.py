#O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.
# CÓDIGO PRODUTO PREÇO (R$)
#H Hamburger 5.50
#C Cheeseburger 6.80
#M Misto Quente 4.50
#A Americano 7.00
#Q Queijo Prato 4.00
#X PARA TOTAL DA CONTA
#Escreva um programa que leia o código de vários itens comprados por um freguês e acumule o total da compra. Ao finalizar com “X”, exiba o total a pagar.
# Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção inválida.”.
# Enquanto o código não for 'X' o programa deve continuar lendo os itens.
# Dica: Use upper() para ignorar a diferenças entre maiúscula e minúsculas; Use [0] para garantir que apenas o primeiro caractere digitado seja considerado. Por exemplo: codigo = input('Código: ').upper()[0]

def main():
    print('Digite a letra correspondente ao produto desejado:')
    total = 0
    while True:
        produto = input(
'''CÓDIGO   PRODUTO         PREÇO (R$)
H        Hamburger       5,50
C        Cheeseburger    6,80
M        Misto Quente    4,50
A        Americano       7,00
Q        Queijo Prato    4,00
X        PARA TOTAL DA CONTA
''').upper()[0]
        if produto == 'H':
            total += 5.50
        elif produto == 'C':
            total += 6.80
        elif produto == 'M':
            total += 4.50
        elif produto == 'A':
            total += 7.00
        elif produto == 'Q':
            total += 4.00
        elif produto == 'X':
            print (f'R$ {total:.2f}')
            break
            
        else:
            print('Opção inválida.)')

if __name__ == '__main__':
    main()