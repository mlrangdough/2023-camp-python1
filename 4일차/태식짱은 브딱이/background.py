import pygame

pygame.init()

screen_width = 480
screen_height = 640

screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("[하찮은 게임]")
background=pygame.image.lode("[그림위치]")

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    pygame.display.update()
#pygame 종료
pygame.quit()