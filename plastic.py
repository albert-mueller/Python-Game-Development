import random
import pgzrun

WIDTH=600
HEIGHT=600
levels=5
start_speed=10
non_recycled_items=["bag", "battery", "chips", "bottle"]
game_over=False
game_complete=False
current_level=1
items=[]
animations=[]
def draw():
    global items, current_level.game_over,game_complete
    screen.clear()
    screen.blit("bground", (0,0)) # to display the image on the screen
def update():
    global items
    if len(items)==0:
        items=make_items(current_level)

        