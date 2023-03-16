import pygame
from ExplorationMode.Player import Player

pygame.init()

screen = pygame.display.set_mode((800,600))
screenRectangle = screen.get_rect()
bg_color = ('#639c7a')
screen.fill(bg_color)

playerGroup = pygame.sprite.Group()
player = Player('','male','','',screen,0)
player.rect.left = 80
player.rect.top = 50
player.rect.height = 360
player.rect.width = 260
player.image = pygame.transform.scale(player.image,(260,360))
playerGroup.add(player)
playerGroup.draw(screen)

font = pygame.font.SysFont('Times',20)
font2 = pygame.font.SysFont('Times',30)

light_skin = pygame.Rect(550,200,50,50)
medium_skin = pygame.Rect(610,200,50,50)
dark_skin = pygame.Rect(670,200,50,50)

skin_text = font.render('Please Choose Your Skin Tone:',True, (0,0,0))
skin_rect = skin_text.get_rect()
skin_rect.center = (630,170)
screen.blit(skin_text,skin_rect)

blonde_hair = pygame.Rect(550,320,50,50)
brown_hair = pygame.Rect(610,320,50,50)
black_hair = pygame.Rect(670,320,50,50)

hair_text = font.render('Please Choose Your Hair Colour:',True, (0,0,0))
hair_rect = hair_text.get_rect()
hair_rect.center = (630,290)
screen.blit(hair_text,hair_rect)

male_text = font2.render('Male',True, (225,225,225))
male_rect = male_text.get_rect()
male_rect.center = (550,110)
screen.blit(male_text,male_rect)

female_text = font2.render('Female',True, (225,225,225))
female_rect = female_text.get_rect()
female_rect.center = (690,110)
screen.blit(female_text,female_rect)

gender_text = font.render('Please Select Your Gender: ',True, (0,0,0))
gender_rect = gender_text.get_rect()
gender_rect.center = (630,50)
screen.blit(gender_text,gender_rect)

    # Draw the rectangles
pygame.draw.rect(screen, '#f1e3d0', light_skin)
pygame.draw.rect(screen, '#9b7e64', medium_skin)
pygame.draw.rect(screen, '#4b3009', dark_skin)
pygame.draw.rect(screen, '#c0a648', blonde_hair)
pygame.draw.rect(screen, '#7f580e', brown_hair)
pygame.draw.rect(screen, '#0f0b02', black_hair)

button_surface = font.render("Finish",True,(255,255,255))
button_rect = button_surface.get_rect()
button_rect.x = 700
button_rect.y = 700
    
screen.blit(button_surface,button_rect)
pygame.display.update()

male = True

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a rectangle was clicked
            if male_rect.collidepoint(event.pos):
                male = True
                print('Male chosen!')
            elif female_rect.collidepoint(event.pos):
                male = False
                print('Female chosen!')
            if light_skin.collidepoint(event.pos):
                # set player's skin to light
                player.update_skin('light')
                print('Light skin chosen!')
            elif medium_skin.collidepoint(event.pos):
                # set player's skin to medium
                player.update_skin('medium')
                print('Medium skin chosen!')
            elif dark_skin.collidepoint(event.pos):
                # set player's skin to dark
                player.update_skin('dark')
                print('Dark skin chosen!')
            elif blonde_hair.collidepoint(event.pos):
                # set player's hair to blonde
                player.update_hair('blonde')
                print('Blonde hair chosen!')
            elif brown_hair.collidepoint(event.pos):
                # set player's hair to brown
                player.update_hair('brown')
                print('Brown hair chosen!')
            elif black_hair.collidepoint(event.pos):
                # set player's hair to black
                player.update_hair('black')
                print('Black hair chosen!')
        
    # Update the screen
    playerGroup.draw(screen)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
