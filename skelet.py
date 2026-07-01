import random
import pgzrun
msg=""
WIDTH=600
HEIGHT=600
Skelett = Actor("skeleton")
def draw():
    try:
        screen.color = screen.fill("black")
        Skelett.draw()
    except Exception as e:
        print(f"Error occurred: {e}")
def update():
    if keyboard.left:
        Skelett.x -= 10
    if keyboard.right:
        Skelett.x += 10
    if keyboard.up:
        Skelett.y -= 10
    if keyboard.down:
        Skelett.y += 10
pgzrun.go()