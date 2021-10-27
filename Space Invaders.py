# Space Defender
# Developer: Ricky A. Segura

# Imports
import pygame, random
from sys import exit
from pygame import draw
from pygame import transform

from pygame.event import event_name

# Classes
class Missle():
  def __init__(self):
    #super(Missle, self).__init__()

    self.ordinance = pygame.Rect(50, 50, 50, 50)

    self.x = player_ship.get_width()/2
    self.y = ship_y
    self.color = pygame.Color("red")
  
  def update():
    pass

# Functions
def player_animation():
  # Animation
  player.y += player_speed_y
  player.x += player_speed_x
  
  # Logic for animation
  if player.top <= 0:
    player.top = 0
  if player.bottom >= screen_height:
    player.bottom = screen_height

  if player.left <= 0:
    player.left = 0
  if player.right >= screen_width:
    player.right = screen_width

def ship_animation():
  global ship_x, ship_y
  # Animation
  ship_x += ship_speed_x
  ship_y += ship_speed_y

  # Logic for animation
  if ship_x <= 0:
    ship_x = 0
  if ship_x + player_ship.get_width() >= screen_width:
    ship_x = screen_width - player_ship.get_width()
  
  if ship_y + player_ship.get_height() >= screen_height:
    ship_y = screen_height - player_ship.get_height()
  if ship_y <= 0:
    ship_y = 0

def reset_enemy():
  global enemy_speed_x, enemy_speed_y
  enemy.center = (random.choice(range(1, screen_width - 1)), enemy.height)
  enemy_speed_x *= random.choice([1, -1])

def enemy_animation():
  global player_score, enemy_speed_x, enemy_speed_y, player_width, player_height

  enemy.x += enemy_speed_x
  enemy.y += enemy_speed_y
  
  # Adding to score when eaten
  if enemy.colliderect(player):
    player_score += 50
    player.width += 4
    player.height += 4
    reset_enemy()

  # Prevent enemy from leaving the map
  if enemy.top <= 0:
    enemy_speed_y *= -1
  if enemy.bottom >= screen_height:
    player_score -= 35
    reset_enemy()
  if enemy.right >= screen_width or enemy.left <= 0:
    enemy_speed_x *= -1

# General Housekeeping
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 950
screen_height = 660
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Cosmic Defense - Defened The Empire")

# Load Icon
icon = pygame.image.load("../kondor/layers/background_3.png")
icon = pygame.transform.scale(icon, [32, 32])
pygame.display.set_icon(icon)

# Game Rectangles (in game objects)
player_width, player_height = 15, 15
player = pygame.Rect(200, 200, player_width, player_height)
enemy = pygame.Rect(300, 300, 10, 10)

# Visual Variables
#bg_color = pygame.Color("black")
background_0 = pygame.image.load("../kondor/layers/background_0.png")
background_0 = pygame.transform.scale(background_0, [screen.get_width(), screen.get_height()])

bg_height = screen.get_height()

space_background = pygame.image.load("../kondor/layers/parallax-space-backgound.png")
space_background = pygame.transform.scale(space_background, [screen.get_width(), screen.get_height()])

big_planet = pygame.image.load("../kondor/layers/parallax-space-big-planet.png")
big_planet = pygame.transform.scale(big_planet, [200, 200])

far_planets = pygame.image.load("../kondor/layers/parallax-space-far-planets.png")
far_planets = pygame.transform.scale(far_planets, [20, 20])

ring_planet = pygame.image.load("../kondor/layers/parallax-space-ring-planet.png")
ring_planet = pygame.transform.scale(ring_planet, [100, 200])

space_stars = pygame.image.load("../kondor/layers/parallax-space-stars.png")
space_stars = pygame.transform.scale(space_stars, [screen.get_width(), bg_height])

player_ship = pygame.image.load("../kondor/orangeship.png")
player_ship = pygame.transform.scale(player_ship, [40, 80])

# Characters
player_color = pygame.Color("cyan")
enemy_color = pygame.Color("red")

# Game Variables
score_limit = 2_500
losing_score = -100

# Player Variables
player_speed_x = 0
player_speed_y = 0
player_score = 0
agility = 5
health = 3

# Ship Variables
ship_x = 250
ship_speed_x = 0
ship_y = 250
ship_speed_y = 0
speed = 4

# Enemy Variables
enemy_speed_x, enemy_speed_y = 4, 4

# Text Variables
player_name = "Rico"
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Main Loop
running = True
while running:
  # Handling I/O
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    
    # Listening to the keyboard
    # When UP/DOWN btns are pressed (ACTION)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        ship_speed_y += speed
      if event.key == pygame.K_UP:
        ship_speed_y -= speed
    
    # When UP/DOWN btns are released (RESET)
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        ship_speed_y -= speed
      if event.key == pygame.K_UP:
        ship_speed_y += speed
    
    # When left/right btns are pressed (ACTION)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        ship_speed_x -= speed
        player_ship = transform.rotate(player_ship, 90)
      if event.key == pygame.K_RIGHT:
        ship_speed_x += speed
        player_ship = transform.rotate(player_ship, -90)

    # When left/right btns are released (RESET)
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        ship_speed_x += speed
        player_ship = transform.rotate(player_ship, -90)
      if event.key == pygame.K_RIGHT:
        ship_speed_x -= speed
        player_ship = transform.rotate(player_ship, 90)
  
  #enemy_animation()
  ship_animation()
  
  # Visuals
  screen.blit(space_background, [0, 0])
  screen.blit(space_stars, [0, 0])
  screen.blit(far_planets, [700, 200])
  screen.blit(ring_planet, [800, 150])
  screen.blit(big_planet, [350, 200])
  screen.blit(player_ship, [ship_x, ship_y])

  #pygame.draw.rect(screen, enemy_color, enemy)

  # Text
  player_text = game_font.render(f"Player:  {player_name}", False, [200, 200, 200])
  player_health = game_font.render(f"Health: {health}", False, [200, 200, 200])
  user_score = game_font.render(f"Score: {player_score}", False, [200, 200, 200])
  you_passed = game_font.render("You completed the game! All the Zoigs are defeated.", False, [200, 200, 200])
  you_failed = game_font.render("Too many Zoigs got through. You lost your homeworld!", False, [200, 200, 200])

  # Add text to screen
  screen.blit(player_text, [10, 10])
  screen.blit(user_score, [10, 50])
  screen.blit(player_health, [10, 90])

  # Game Complete Scene
  if player_score >= score_limit:
    screen.fill(pygame.Color("black"))
    screen.blit(you_passed, [screen_width/2 - you_passed.get_width()/2, screen_height/2 - you_passed.get_height()])
  
  if player_score <= losing_score:
    screen.fill(pygame.Color("black"))
    screen.blit(you_failed, [screen_width/2 - you_failed.get_width()/2, screen_height/2 - you_failed.get_height()])

  # Updating the window
  pygame.display.update()
  clock.tick(60)