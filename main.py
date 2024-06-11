import pygame

# from pygame.event import post


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

def draw_background():
  screen.fill('gray')
  pygame.draw.line(screen, 'brown', (0,600), (1280, 600))
  
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  draw_background()

          
          
  pygame.display.update()
pygame.quit()