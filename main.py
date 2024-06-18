import pygame, os

# from pygame.event import post


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
FPS = 60
clock = pygame.time.Clock()



class Soldier(pygame.sprite.Sprite):
  def __init__(self, char_type, x_pos, y_pos, scale):
    pygame.sprite.Sprite.__init__(self)
    
    self.char_type = char_type
    self.animation_list = []
    self.frame_index = 0
    self.action = 0
    self.flip = False
    animation_types = ['idle', 'run', 'jump']
    for animation in animation_types:
      temp_list = []
      num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}'))
      for i in range(num_of_frames):
        img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png')
        img = pygame.transform.scale(img, (100, 100))
        temp_list.append(img)
      self.animation_list.append(temp_list)
      
    self.image = self.animation_list[self.action][self.frame_index]
    self.rect = self.image.get_rect()
    self.rect.center = (x_pos, y_pos)
    
  def draw(self):
    screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
      
player = Soldier('player',200, 540, 5)
  
def draw_background():
  screen.fill('gray')
  pygame.draw.line(screen, 'brown', (0,600), (1280, 600))
  
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  draw_background()
  player.draw()
  
  
  
          
          
  pygame.display.update()
pygame.quit()