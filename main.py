

import lib.Beans
import math
import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("植物大战僵尸")
icon = pg.image.load("images\screenshot1.jpg")
pg.display.set_icon(icon)
backgroung_img = pg.image.load("images\\background1.jpg")
SeedBank_img = pg.image.load("images\\SeedBank.png")
SeedPacket_Larger_img = pg.image.load("images\SeedPacket_Larger.png")

PeaShooter_img = pg.image.load("images\plants\PeaShooter.png")

score = 0
sun = 0

class Player():
    def __init__(self,X = 0,Y = 0) -> None:
        self.X = X
        self.Y = Y

player = Player()

class Bean():
    def __init__(self):
        self.img = pg.image.load("images\plants\ProjectilePea.png")
        self.x = 50 + (player.X * 80) + 25
        self.y = 100 + (player.Y * 100) + 10
        self.speed = 3
        # self.angle = 45
    #子弹击中检测
    def hit(self):
        global score,sun
        for e in Zombies:
            if(self.x >=e.x and self.y >= e.y and self.y <= e.y + 145):
                Beans.remove(self)
                e.reset()
                score += 1
                print(score)
                s = random.randint(1,10)
                if s == 5:
                    sun += 50
                break

Beans = []

class Zombie():
    def __init__(self):
        self.img = pg.image.load("images\Zombies\Zombie.png")
        self.x = 800
        self.y = random.randint(0,4) * 100 + 55
        self.step = -0.25
    def reset(self):#被射中时恢复位置
        self.x = 800
        self.y = random.randint(0,4) * 100 + 55
Zombies = []
for i in range(10):
    Zombies.append(Zombie())
# print(Zombies)

def distance(bx,by,ex,ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a+b*b)

def show_img():
    screen.blit(backgroung_img,(-220,0))
    screen.blit(SeedBank_img,(0,0))
    screen.blit(PeaShooter_img,(50 + (player.X * 80),100 + (player.Y * 100)))

def show_Beans(): 
    for b in Beans:
        screen.blit(b.img,(b.x,b.y))
        b.hit()
        b.x += b.speed
        # b.y += math.sin(b.x)*100
        # 计算子弹位置
        # b.x += b.speed * math.cos(math.radians(b.angle))
        b.y += b.speed * math.sin(math.radians(b.x))
        if b.x > 800:
            try:
                Beans.remove(b)
            except:
                break
            break


def show_Zombie():
    for e in Zombies:
        screen.blit(e.img,(e.x,e.y))
        e.x += e.step
        if e.x < 0:
            e.reset()

font = pg.font.SysFont("",30)
def show_sun():
    sun_render = font.render(str(sun),True,(0,0,0))
    screen.blit(sun_render,(15,60))

while True:
    for event in pg.event.get():
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
                Beans.append(Bean())
    show_img()
    show_Beans()
    show_Zombie()
    show_sun()
    pg.display.update()