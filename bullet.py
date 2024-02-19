import pygame
from random import randint

BLACK = (0, 0, 0)

class Bullet(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()

    #Pass in parameters
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    #Draw rect
    pygame.draw.rect(self.image, color, [0, 0, width, height])

    #Gets velocity
    self.velocity = [6, 6]

    #Fetch rect
    self.rect = self.image.get_rect()
    
  def update(self):
    self.rect.y -= self.velocity[1]