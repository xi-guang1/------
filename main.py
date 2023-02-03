

import lib.Beans as Beans
import lib.Zombies as Zombies
import lib.Plantes as Plantes
import math
import pygame as pg
import threading

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("植物大战僵尸")
icon = pg.image.load("images\screenshot1.jpg")
pg.display.set_icon(icon)
backgroung_img = pg.image.load("images\\background1.jpg")
SeedBank_img = pg.image.load("images\\SeedBank.png")
SeedPacket_Larger_img = pg.image.load("images\SeedPacket_Larger.png")

score = 0
sun = 0

class Player():
    def __init__(self,
                 X = 0,
                 Y = 0,
                 img = pg.image.load("images\plants\PeaShooter.png")) -> None:
        self.X = X
        self.Y = Y
        self.img = img
        self.bullet = Beans.sinBean

player = Plantes.PeaShooter()
Bean = []
Zombie = [Zombies.Zombie() for i in range(10)]

def distance(bx,by,ex,ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a+b*b)

def draw_SeedBank():
    screen.blit(SeedBank_img,(0,0))

def draw_img():
    screen.blit(backgroung_img,(-220,0))
    screen.blit(player.img,(50 + (player.X * 80),100 + (player.Y * 100)))

def draw_Beans(): 
    for a in Bean:
        for b in a:
            screen.blit(b.img,(b.x,b.y))

def draw_Zombie():
    for e in Zombie:
        screen.blit(e.img,(e.x,e.y))

font = pg.font.SysFont("宋体",30)
def draw_sun():
    sun_render = font.render(f"{sun}",True,(0,0,0))
    screen.blit(sun_render,(15,60))

def draw():
    while True:
        clock.tick(60)
        draw_sun()
        draw_img()
        draw_Beans()
        draw_Zombie()
        pg.display.update()

def logic():
    while True:
        clock.tick(150)
        for e in Zombie:
            e.x += e.speed
            if e.x < 0:
                e.reset()
        for a in Bean:
            for b in a:
                if b.hit(Zombie):
                    a.remove(b)
                b.move()
            # b.x += b.speed
            # b.y += math.sin(b.x)*100
            # 计算子弹位置
            # b.x += b.speed * math.cos(math.radians(b.angle))
            # b.y += b.speed * math.sin(math.radians(b.x))
            if b.x > 800:
                try:
                    Bean.remove(b)
                except:
                    break
                break

   
渲染 = threading.Thread(target=draw,name= "渲染")
逻辑 = threading.Thread(target=logic,name = "逻辑")
渲染.start()
逻辑.start()
while True:
    # clock.tick()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # 逻辑.exit()
            # 渲染.exit()
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT and player.X < 8:
                player.X += 1
            elif event.key == pg.K_LEFT and player.X > 0:
                player.X += -1
            elif event.key == pg.K_UP and player.Y > 0:
                player.Y += -1
            elif event.key == pg.K_DOWN and player.Y < 4:
                player.Y += 1
            elif event.key == pg.K_SPACE:
                player.Beans.append(player.bullet(player))
                if player.Beans not in Bean:
                    Bean.append(player.Beans)
            elif event.key == pg.K_1:
                player = Plantes.PeaShooter(player.X,player.Y)
            elif event.key == pg.K_2:
                player = Plantes.sinPeaShooter(player.X,player.Y)
    # show_sun()