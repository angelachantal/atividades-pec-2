def duracao (segundos):
    hh = segundos//3600
    mm = (segundos%3600)//60
    ss = (segundos%3600)%60
    return f'{hh:02}:{mm:02}:{ss:02}'

def main():
    segundos = int(input().strip())
    
    print (f'{duracao(segundos)}')

if __name__=='__main__':
    main()