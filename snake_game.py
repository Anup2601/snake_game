import pygame
import random
pygame.init()
# colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
# creting window
screen_width=900
screen_hight=600
gamewindow=pygame.display.set_mode((screen_width,screen_hight))

bgimg=pygame.image.load("snake_back.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_hight)).convert_alpha()

# game title
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
pygame.display.set_caption("snakegame")
pygame.display.update()

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,snk_list,snake_size):
    # print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color ,[x,y,snake_size,snake_size])
# def welcome():
#     exit_game=False
#     while not exit_game:
#         gamewindow.fill(white)
#         text_screen("Welcome to Snake Game Developed by Anup Mishra",red,250,250)
#         text_screen("Press Space Bar to Play",red,230,290)
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 exit_game=True
#             if event.type==pygame.KEYDOWN:
#                 if event.key==pygame.K_SPACE:
#                     gameloop()

    # pygame.display.update()
    # clock.tick(60)
def gameloop():
    # game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x=0
    velocity_y=0
    snk_list = []
    snk_length = 1
    with open("highscore.txt","r") as f:
        highscore=f.read()

    food_x = random.randint(20, screen_width / 1.5)
    food_y = random.randint(20, screen_hight / 1.5)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps= 60
    # game loop
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            text_screen("Game Over ! Press Enter to continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                          gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 10
                food_x = random.randint(20, screen_width / 1.5)
                food_y = random.randint(20, screen_hight / 1.5)
                snk_length += 5
                if score>int(highscore):
                    highscore=score

            gamewindow.fill(white)
            text_screen("score: " + str(score) + '  High score: '+str(highscore), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_hight:
                game_over = True

            plot_snake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()