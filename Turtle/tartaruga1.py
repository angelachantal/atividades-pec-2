#Programa que faz uma tartaruga se mover pela tela.

#Importar toda a biblioteca turtle:
from turtle import *

#Definir que o robô tenha a forma de uma tartaruga:  
shape ('turtle')

#Definir a velocidade de 1 (mais lento) a 11 (mais rápido):
speed (1)

#Definir a cor e largura da linha:
pensize(8)
color('red')


#Indicar a direção para a qual a tartaruga deve andar (para frente/forward, para trás/backward) e virar (esquerda/left; direita/right); e quando levantar ou baixar a caneta (penup e pendown):
forward(100)
right(90)
forward(100)
right(90)
penup()
forward(50)
pendown()
forward(100)
left(45)
forward(200)

#Encerra.
done()
