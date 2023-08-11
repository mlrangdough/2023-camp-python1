import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640

screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("[하찮은 게임]")
background=pygame.image.load("C:\\Users\\저스트필\\Desktop\\보낼거\\배켱.png")

#캐릭터 불러오기

character=pygame.image.load("C:\\Users\\저스트필\Desktop\\보낼거\\제목 없음.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos =(screen_width/2)-(character_width/2)
character_y_pos =screen_height-character_height

enemy = pygame.image.load("C:\\Users\\저스트필\\Desktop\\보낼거\\adad.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos =random.randint(0,screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 30
to_x =0
character_speed=5
#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x-=character_speed
            elif event.key==pygame.K_RIGHT:
                to_x+=character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    character_x_pos += to_x
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    pygame.display.update()

#pygame 종료
pygame.quit()