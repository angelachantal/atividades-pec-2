def main():
    while True:
        menu = int(input(
    '''OPÇÕES:        
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM
''').strip())
        if menu == 1:
            print ('1 - Olá. Como vai?')
        elif menu == 2:
            print ('2 - Vamos estudar mais.')
        elif menu == 3:
            print ('3 - Meus Parabéns!')
        elif menu == 0:
            print ('0 - Fim de serviço.')
            break
        else:
            print('Opção inválida.')
        
if __name__ == '__main__':
    main()