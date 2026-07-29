import pgzrun
import random
import time
WIDTH=800
HEIGHT=800
Sateliten=[]
lines=[]
next_satelite=0
total_satelites=10
def create_satelite():    
    for i in range(total_satelites):
        DieSateliten=Actor("satelit")
        DieSateliten.pos=random.randint(50,750), random.randint(50,750)
        Sateliten.append(DieSateliten)
def draw():
    screen.fill("red")
    number=1
    for i in Sateliten:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+20))
        i.draw()
        number+=1
    for i in lines:
        screen.draw.line(i[0],i[1],"green")

def update():
    pass
def on_mouse_down(pos):
    global next_satelite,lines
    if next_satelite<total_satelites:
        if Sateliten[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((Sateliten[next_satelite-1].pos,Sateliten[next_satelite].pos))
            next_satelite+=1
        else:
            lines=[]
            next_satelite=0
create_satelite()
pgzrun.go()