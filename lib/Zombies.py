import pygame as pg
import random

class Zombie():
    def __init__(self):
        self.img = pg.image.load("images\Zombies\Zombie.png")
        self.x = 800
        self.y = random.randint(0,4) * 100 + 55
        self.speed = -0.25
    def reset(self):#被射中时恢复位置
        self.x = 800
        self.y = random.randint(0,4) * 100 + 55