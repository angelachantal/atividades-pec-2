from turtle import *

color("brown")
pensize(3)
speed(3)

def teto (lado): 
    #Desenhar triângulo.
    for count in range (3):
        forward (lado)
        left(120)

def paredes (lado):
    #Desenhar quadrado.
    for count in range (4):
        forward (lado)
        left (270)
        
def main():
    lado = 100
    teto(lado)
    paredes(lado)

if __name__=="__main__":
    main()
    
    
        
   
    
    