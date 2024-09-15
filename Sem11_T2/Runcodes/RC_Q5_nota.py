def main():    
    while True:
        nota = float(input().strip())
        if nota < 0 or nota > 10:
            print ('Nota inválida.')
        elif nota >= 8.5:
            print ('A')
            break
        elif nota >= 7.0:
            print ('B')
            break
        elif nota >= 5.0:
            print ('C')
            break
        elif nota >= 4:
            print ('D')
            break
        elif nota >= 0:
            print ('E')
            break

if __name__ == '__main__':
    main()