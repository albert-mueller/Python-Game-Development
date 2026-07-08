import random
import pgzrun
import sys
msg=""
WIDTH=600
HEIGHT=600
Skelett = Actor("skeleton")
def draw():
    try:
        screen.color = screen.fill("black")
        Skelett.draw()
        screen.draw.text(msg, (100,100), color="white")
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(3)
def update():
    if keyboard.left:
        Skelett.x -= 10
    if keyboard.right:
        Skelett.x += 10
    if keyboard.up:
        Skelett.y -= 10
    if keyboard.down:
        Skelett.y += 10
    
def place_skeleton():
    Skelett.x=random.randint(80,520)
    Skelett.y=random.randint(100,500)

def on_mouse_down(pos):
    global msg
    if Skelett.collidepoint(pos):
        place_skeleton()
        msg=("Good shot")
    else:
        msg=("Bad shot")

pgzrun.go()
