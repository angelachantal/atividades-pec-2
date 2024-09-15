#Faça um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).

def duracao (segundos):
    hh = segundos//3600
    mm = (segundos%3600)//60
    ss = (segundos%3600)%60
    return f'{hh:02}:{mm:02}:{ss:02}'

def main():
    segundos = int(input('Duração do evento em segundos: ').strip())
    
    print (f'Duração do evento: {duracao(segundos)}')

if __name__=='__main__':
    main()