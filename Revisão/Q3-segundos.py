#03. Escreva um algoritmo/programa que calcule e exiba o número de segundos em um minuto, em uma hora e em um dia.

def main():
    segundos = 1
    seg_minutos = int(segundos * 60)
    seg_horas = int(seg_minutos * 60)
    seg_dia = int(seg_horas * 24)
    
    print (f'Número de segundos em um minuto: {seg_minutos}.\nNúmero de segundos em uma hora: {seg_horas}.\nNúmero de segundos em um dia: {seg_dia}.')

if __name__ == '__main__':
    main()