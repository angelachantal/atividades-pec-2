from turtle import *

color("purple")
pensize(5)
speed(3)

def forma (lado, angulo):
    for count in range (lado):
        forward (100)
        right(angulo)
        
def main():
    lado = 10
    angulo = 360/lado
    forma(lado, angulo)

if __name__=="__main__":
    main()
    
    
        
   
    
    