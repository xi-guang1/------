import pygame as pg
import lib.Beans as Beans


class PeaShooter():
    def __init__(self,
                 X = 0,
                 Y = 0) -> None:
        self.X = X
        self.Y = Y
        self.img = pg.image.load("images\plants\PeaShooter.png")
        self.bullet = Beans.Bean
        self.Beans = []

class sinPeaShooter(PeaShooter):
    def __init__(self, X = 0, Y = 0) -> None:
        super().__init__(X, Y)
        self.bullet = Beans.sinBean