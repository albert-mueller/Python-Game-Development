from random import randint
import sys
import pgzrun
HEIGHT=700
WIDTH=700
Bienen=Actor("biene")
Margarita=Actor("margarita")
Bienen.pos=100,50
Margarita.pos=30,10
Punkten=0
Game_over=False
def draw():
    screen.blit("wald", (0,0))
    Bienen.draw()
    Margarita.draw()
    screen.draw.text("score:" + str(Punkten),(600,600))
def update():
    global Punkten
    if keyboard.left:
        Bienen.x-=5
    if keyboard.right:
        Bienen.x+=5
    if keyboard.up:
        Bienen.y-=5
    if keyboard.down:
        Bienen.y+=5
    if Bienen.colliderect(Margarita):
        Punkten=Punkten+1
        Margarita_beliebiges_Platzieren()

def Margarita_beliebiges_Platzieren():
    Margarita.x=randint(100,600)
    Margarita.y=randint(100,600)
pgzrun.go()
