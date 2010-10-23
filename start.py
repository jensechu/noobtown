import pygame, sys,os
from pygame.locals import *

pygame.init()

SCREEN_SIZE = (544, 429)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
pygame.display.set_caption('Pallet Town')
screen = pygame.display.get_surface()

#Load image files
pikachu_file = os.path.join("media", "pikachu_sprite.png")
pikachu_cursor = pygame.image.load(pikachu_file).convert_alpha()

background_file = os.path.join("media", "background_forest.png")
background_forest = pygame.image.load(background_file).convert()

#Load sound files
lavendar_music_file = os.path.join("media", "lavendar_music.mp3")
lavendar_music = pygame.mixer.music.load(lavendar_music_file)
pygame.mixer.music.play(1)




Fullscreen = False
x, y = 230, 340
move_x, move_y = 230, 340

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

        if event.type == KEYDOWN:
            #Toggles Fullscreen mode
            if event.key == K_f:
                Fullscreen = not Fullscreen #Sets Fullscreen to 'true' first
                if Fullscreen:
                    screen = pygame.display.set_mode((544, 429), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((544, 429), 0, 32)
            #Moves Pikachu around    
            if event.key == K_DOWN:
                move_y = +5
                y+= move_y
                  
            elif event.key == K_UP:
                move_y = -5
                y+= move_y
                
            elif event.key == K_LEFT:
                move_x = -5
                x+= move_x
                
            elif event.key == K_RIGHT:
                move_x = +5
                x+= move_x
            
            elif event.type == KEYUP:
                if event.key == K_DOWN:
                    move_y = 0
                    y+= move_y
                
                elif event.key == K_UP:
                    move_y == 0
                    y+= move_y
                
                elif event.key == K_LEFT:
                    move_x == 0
                    x+= move_x
                    
                elif event.key == K_RIGHT:
                    move_x == 0
                    x+= move_x
            
            
        print x, y
        screen.blit(background_forest, (0, 0))
        screen.blit(pikachu_cursor, (x,y))
            

        pygame.display.update()
        print event
