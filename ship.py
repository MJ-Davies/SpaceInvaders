import pygame
BLACK = (0, 0, 0)

class Ship(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()

    #Pass in parameters
    self.width = width
    self.height = height
    self.image = pygame.Surface([self.width, self.height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    #Draw our ship
    pygame.draw.rect(self.image, color, [0, 0, width, height])

    #Fetch the rect object
    self.rect = self.image.get_rect()

  #Ship movement
  def move_left(self, pixels):
    self.rect.x -= pixels
    #Check if we're off screen
    if self.rect.x < 0:
      self.rect.x = 0
  
  def move_right(self, pixels):
    self.rect.x -= pixels
    #Check if we're off screen
    if self.rect.x > 770:
      self.rect.x = 770