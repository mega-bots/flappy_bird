import pygame
import random
from sys import exit
import time
pygame.init()
location = "/home/prabhas/Desktop/projects/"
screen = pygame.display.set_mode((800,400))  #Sets the window size (width,height)
pygame.display.set_caption("GAMING")  #Sets the window title
clock = pygame.time.Clock() #This is used for FPS

image_surface = pygame.image.load(f"{location}/sprites/background-night.png")
ground_surface = pygame.image.load(f"{location}/sprites/base.png") 
bluebird_up_surface = pygame.image.load(f"{location}/sprites/bluebird-upflap.png")
bluebird_mid_surface = pygame.image.load(f"{location}/sprites/bluebird-midflap.png")
bluebird_down_surface = pygame.image.load(f"{location}/sprites/bluebird-downflap.png")
bluebird_up_rect = bluebird_up_surface.get_rect(topleft = (300,150))
bluebird_mid_rect = bluebird_mid_surface.get_rect(topleft = (300,150))
bluebird_down_rect = bluebird_down_surface.get_rect(topleft = (300,150))


jumpsound = pygame.mixer.Sound(f"{location}/audio/wing.wav")
hitsound = pygame.mixer.Sound(f"{location}/audio/hit.wav")
pointsound = pygame.mixer.Sound(f"{location}/audio/point.wav")


starting_page = pygame.image.load(f"{location}/sprites/message.png")
ending_page = pygame.image.load(f"{location}/sprites/gameover.png")
pipe_surface = pygame.image.load(f"{location}/sprites/pipe-green.png")


pipe_rect1 = pipe_surface.get_rect(midtop = (800,250))
pipe_rect2 = pipe_surface.get_rect(midbottom = (800,105))

pipe_rect3 = pipe_surface.get_rect(midtop = (800,250))
pipe_rect4 = pipe_surface.get_rect(midbottom = (800,105))




val = 1

fps = 27

gravity = 0

speed = 8

second = 0
start = 0

score = 0
text_font = pygame.font.Font(None,75)#generating font
text_surface = text_font.render(str(score),False,'Black')#rendering the font over the screen

while 1:
    for event in pygame.event.get():  #Inorder to be able to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    screen.blit(pygame.transform.scale(starting_page,(600,400)),(100,0))
    pygame.display.update() 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        break
while 1:
    generate_obstacle = random.randint(-185,95)
    for event in pygame.event.get():  #Inorder to be able to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #To exit perfectly from the code
    if second==49:
        start=1
    second+=1
    second%=50
    screen.blit(pygame.transform.scale(image_surface,(800,400)),(0,0)) #rescaling
    screen.blit(pygame.transform.scale(ground_surface,(800,100)),(0,325))
    # screen.blit(text_surface,((150,50)))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        gravity-=12
        gravity = max(gravity,-15)
        jumpsound.play()
    else:
        gravity+=2.25
    if val<fps//3:
        screen.blit(pygame.transform.scale(bluebird_up_surface,(50,50)),bluebird_up_rect)
    elif val<2*(fps//3):
        screen.blit(pygame.transform.scale(bluebird_mid_surface,(50,50)),bluebird_mid_rect)
    else:
        screen.blit(pygame.transform.scale(bluebird_down_surface,(50,50)),bluebird_down_rect)
    val+=1
    val%=fps
    if pipe_rect1.left<=-20:
        pipe_rect1.left = 805
        pipe_rect2.left = 805
        pipe_rect1.top = 250-generate_obstacle
        pipe_rect2.bottom = 105-generate_obstacle
        score = str(int(score)+1)
        text_surface = text_font.render(score,False,'Black')#rendering the font over the screen
        pointsound.play()
    if pipe_rect3.left<=-20:
        pipe_rect3.left = 805
        pipe_rect4.left = 805
        pipe_rect3.top = 250-generate_obstacle
        pipe_rect4.bottom = 105-generate_obstacle
        score = str(int(score)+1)
        text_surface = text_font.render(score,False,'Black')#rendering the font over the screen
        pointsound.play()
    if start:
        screen.blit(pipe_surface,pipe_rect3)
        screen.blit(pygame.transform.flip(pipe_surface,False,True),pipe_rect4)    
        if not (bluebird_up_rect.colliderect(pipe_rect3) or bluebird_mid_rect.colliderect(pipe_rect3) or bluebird_down_rect.colliderect(pipe_rect3) or bluebird_up_rect.colliderect(pipe_rect4) or bluebird_mid_rect.colliderect(pipe_rect4) or bluebird_down_rect.colliderect(pipe_rect4) or bluebird_down_rect.y>400 or bluebird_down_rect.y<=-60):
            pipe_rect3.left-=speed
            pipe_rect4.left-=speed   
        else: 
          print("GAME OVER") 
          hitsound.play()
          print(score)
          time.sleep(1)
          break          
    screen.blit(pipe_surface,pipe_rect1)
    screen.blit(pygame.transform.flip(pipe_surface,False,True),pipe_rect2)
    bluebird_up_rect.y+=gravity
    bluebird_mid_rect.y+=gravity
    bluebird_down_rect.y+=gravity
    if not (bluebird_up_rect.colliderect(pipe_rect1) or bluebird_mid_rect.colliderect(pipe_rect1) or bluebird_down_rect.colliderect(pipe_rect1) or bluebird_up_rect.colliderect(pipe_rect2) or bluebird_mid_rect.colliderect(pipe_rect2) or bluebird_down_rect.colliderect(pipe_rect2) or bluebird_down_rect.y>400 or bluebird_down_rect.y<=-60):
      pipe_rect1.left-=speed
      pipe_rect2.left-=speed
    else: 
        print("GAME OVER") 
        print(score)
        hitsound.play()
        time.sleep(1)
        break
     
    screen.blit(text_surface,((150,50)))

    pygame.display.update() 
    clock.tick(fps) #Tells the while loop not to run more than 60 times ie to maintain 60FPS
while 1:
    for event in pygame.event.get():  #Inorder to be able to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    screen.blit(pygame.transform.scale(ending_page,(400,200)),(200,100))
    pygame.display.update() 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        break
