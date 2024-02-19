import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien

pygame.init()

#Constants for colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Initializes scores, lives, and bullet count
score = 0
lives = 3

#Create a window
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Space Invaders")

#Initializes sprites
ship = Ship(WHITE, 30, 25)
ship.rect.x = 350
ship.rect.y = 560
bullet = Bullet(WHITE, 4, 40)

#Initialize groups
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
all_aliens = pygame.sprite.Group()
a_bullet = []

all_sprites.add(ship)

#Initializes aliens
for i in range(10):
  alien = Alien(WHITE, 30, 30)
  alien.rect.x = 30 + i * 80
  alien.rect.y = 60
  all_sprites.add(alien)
  all_aliens.add(alien)

#Running variable
running = True

#Frames per second object
clock = pygame.time.Clock()

#Initiate Bullet Variables
  #Timer Variables
press_time = 0
time_tracker = [0,0,0]
waiting_time = 200
  #Bullet counter
bullet_count = 0

#------- Main Game Loop
while running:
  #--- Main Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  #Move paddle left and right
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    ship.move_left(5)

  if keys[pygame.K_RIGHT]:
    ship.move_right(-5)
  
  #Shoot bullet
  current_time = pygame.time.get_ticks()
  
  if keys[pygame.K_SPACE]:
    press_time = pygame.time.get_ticks()
    time_difference = current_time - time_tracker[-2]
    if current_time > time_tracker[-1] + waiting_time: #Waits for x seconds (waiting_time) to append the time the space key was pressed
      time_tracker.append(press_time)
      if time_difference > waiting_time: #Checks if x seconds (waiting_time) has passed since last press
        bullet_count += 1
        #if bullet_count <= 3:
        bullet = Bullet(WHITE, 10, 10)
        ship.update()
        bullet.rect.x = ship.rect.x
        bullet.rect.y = ship.rect.y
        all_bullets.add(bullet)
        all_sprites.add(bullet)
        all_bullets.draw(screen)

  # --- Game Logic | Physics
  all_sprites.update()

  if lives == 0:

    #Display game over
    font = pygame.font.Font(None, 74)
    text = font.render("GAME OVER!", 1, WHITE)
    screen.blit(text, (250, 300))
    pygame.display.flip()
    pygame.time.wait(3000) #Wait 3 seconds

    running = False

  #Collision of wall with aliens
  for alien in all_aliens:
    if alien.rect.x >= 790:
      alien.velocity[0] = -alien.velocity[0]
      alien.wall_bounce()

    if alien.rect.x <= 0:
      alien.velocity[0] = -alien.velocity[0]
      alien.wall_bounce()

  #Collision between bullet and aliens
  alien_collision_list = pygame.sprite.spritecollide(bullet, all_aliens, False)

  for alien in alien_collision_list:
    score += 10
    alien.kill()

    if len(all_aliens) == 0:
      font = pygame.font.Font(None, 74)
      text = font.render("Level Complete!", 1, WHITE)
      screen.blit(text, (250, 300))
      pygame.display.flip()
      pygame.time.wait(3000) #Wait 3 seconds

      running = False
  
  #Collision of Top Wall & Bullet
  for bullet in all_bullets:
    if bullet.rect.y >= 599:
      bullet.kill()
      print('ok')
      
  #--- Drawing Code
  #Black background
  screen.fill(BLACK)
  pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

  #Display score and lives
  font = pygame.font.Font(None, 34)
  small_font = pygame.font.Font(None, 18)

  text = font.render("Score: " + str(score), 1, WHITE)
  screen.blit(text, (20, 10))

  text = font.render("Lives: " + str(lives), 1, WHITE)
  screen.blit(text, (650, 10))

  #Draw our sprites
  all_sprites.draw(screen)

  # --- Updates screen with drawings
  pygame.display.flip()

  #--- Limit to 60 frames per second
  clock.tick(60)

#Exits the program
pygame.quit()