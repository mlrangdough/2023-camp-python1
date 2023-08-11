import pygame
import random

pygame.init()

screen_width =400
screen_height = 300

screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("[하찮은 게임]")
background=pygame.image.load("C:\\Users\\저스트필\\Desktop\\태식짱은 브딱이\\배켱.jpg")

#캐릭터 불러오기

character=pygame.image.load("C:\\Users\\저스트필\\Desktop\\태식짱은 브딱이\\사진2(창민).png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos =(screen_width/2)-(character_width/2)
character_y_pos =screen_height-character_height

enemy = pygame.image.load("C:\\Users\\저스트필\\Desktop\\태식짱은 브딱이\\사진1(창민).png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos =random.randint(0,screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 30
to_x =0
character_speed=5
#폰트 정의
game_font=pygame.font.Font(None,40)
#총 시간
total_time =30
#시작 시간
start_ticks=pygame.time.get_ticks()
#이벤트 루프
clock = pygame.time.Clock()
running = True
while running:
    dt=clock.tick(201)
    #타이머 집어 넣기
    elapsed_time =(pygame.time.get_ticks()-start_ticks)/1000
    timer = game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))
    screen.blit(timer,(10,10))
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

    #가로의 경계값 설정(캐릭터)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width - character_width

    #세로의 경계값 설정(캐릭터)
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

# 충돌 체크
    if character_rect.colliderect(enemy_rect):      # rectangle 기준으로 충돌 여부 확인.
        print("충돌했어요")
        running = False

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    enemy_y_pos+= enemy_speed
    
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width-enemy_width)


    pygame.display.update()

pygame.time.delay(1500)

#pygame 종료
pygame.quit()