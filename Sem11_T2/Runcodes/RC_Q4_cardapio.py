def main():
    total = 0
    while True:
        produto = input(
'''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA
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
            print (f'{total:.2f}')
            break
        else:
            print(f'Opção inválida.')

if __name__ == '__main__':
    main()