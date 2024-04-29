def par_impar(n, pares, impares):
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    return (pares, impares)
def main():
    pares=0
    impares=0 
    for count in range(100):
        n=int(input('').strip())
        pares, impares=(par_impar(n, pares, impares))
    print (pares)
    print (impares)
if __name__=='__main__':
    main()