import pygame
from GameObject import GameObject

class Arrow(GameObject):
    def __init__(self, damage, direction, speed, x, y, imgPath, enemy):
        super().__init__(x,y,imgPath)
        self.damage = damage
        self.direction = direction
        self.speed = speed
        self.xPos = x
        self.yPos = y
        self.targetEnemy = enemy

    def update(self):
        self.move()
        self.registerCollision()

    def move(self):
        self.xPos += self.direction[0] * self.speed
        self.yPos += self.direction[1] * self.speed
        self.rect.x = self.xPos
        self.rect.y = self.yPos

    def registerCollision(self):
        if pygame.sprite.collide_rect(self, self.targetEnemy):
            self.targetEnemy.inflictDamage(self.damage)
            self.kill()