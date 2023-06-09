import pygame
from ExplorationMode.SubArea.Obstacle import Obstacle

class Wall(Obstacle):
    def __init__(self, x, y, width, height, imgPath):

        super().__init__(x,y,imgPath)

        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    