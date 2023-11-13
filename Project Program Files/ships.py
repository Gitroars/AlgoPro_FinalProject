import pygame
from laser import Laser

#Reference : https://github.com/clear-code-projects/Space-invaders/blob/main/code/player.py
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,constraint,speed):
        super().__init__()
        #Object Body
        self.image = pygame.image.load("PNG/playerShip1_red.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        #Boundary Limit
        self.max_x_constraint = constraint
        # Laser Reloading
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600
        #Laser Group
        self.lasers = pygame.sprite.Group()
        #Audio
        self.laser_sound = pygame.mixer.Sound("SFX/sfx_laser2.ogg")
        self.laser_sound.set_volume(0.5)
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed #move right
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed #move left
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks() #mark the time
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True
    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,-8,self.rect.bottom))
        self.laser_sound.play()
    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()

