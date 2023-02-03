import pygame as pg
import math

class Bean():
    def __init__(self,player):
        self.img = pg.image.load("images\plants\ProjectilePea.png")
        self.x = 50 + (player.X * 80) + 25
        self.y = 100 + (player.Y * 100) + 10
        self.speed = 3
        self.angle = 0
    #子弹击中检测
    def hit(self,Zombies):
        for e in Zombies:
            if(self.x >=e.x and self.y >= e.y and self.y <= e.y + 145):
                e.reset()
                return True
                # score += 1
                # print(score)
                # s = random.randint(1,10)
                # if s == 5:
                #     sun += 50
                # break
        return False
    def move(self):
        self.x += self.speed


class sinBean(Bean):
    def __init__(self, player):
        super().__init__(player)
    def move(self):
        self.x += self.speed
        self.y += self.speed * math.sin(math.radians(self.x))


class bombBean(Bean):
    def __init__(self, player):
        super().__init__(player)