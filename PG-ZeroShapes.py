import pgzrun
WIDTH=600
HEIGHT=600
def draw():
    screen.fill("red")
    screen.draw.line((50,50),(500,500),"black")
    screen.draw.circle((100,100),50,"white")
    screen.draw.filled_circle((300,100),60,"dark blue")
    screen.draw.rect(Rect((50,50),(500,500)),"green")
pgzrun.go()