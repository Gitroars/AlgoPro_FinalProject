import pygame
#Reference : https://github.com/clear-code-projects/Space-invaders/blob/main/code/laser.py
class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,screen_height):
        super().__init__()
        self.image = pygame.image.load('PNG/Lasers/laserGreen13.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.height_y_constraint = screen_height


    def destroy(self):
        if self.rect.y <= 0 or self.rect.y >= self.height_y_constraint:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()