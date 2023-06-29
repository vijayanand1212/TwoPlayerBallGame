import random

import pygame
from win32gui import SetWindowPos
from Slider import Slider
from Ball import Ball

Left = input("Enter Left Side player:").capitalize()
Right = input("Enter Right Side Player:").capitalize()
while Left ==Right:
    print("Enter a different name...")
    Right = input("Enter Right Side Player:").capitalize()

no_lose = int(input("Enter No of wins..:"))
while no_lose> 20 or no_lose<=0:
    print("Enter Below or equal to 20 and greater than 0")
    no_lose = int(input("Enter No of wins..:"))

left_win = 0
right_win = 0
move_of = 0

active = False
# Pygame Init
pygame.init()
SCREEN_SIZE = (900,700)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
SetWindowPos(pygame.display.get_wm_info()['window'], -1, 400,20, 0, 0, 1)
SOUND = pygame.mixer.Sound('./sound.wav')
pygame.mixer.music.load('./music.mp3')
pygame.mixer.music.play(-1)
# Essentials
running = True
lastWon = 0

Slide_R=None
Slide_L = None
ball = None
def make_new_game():
    global Slide_R,Slide_L,ball,move_of
    rect_l = pygame.Rect(20,315,10,70)
    Slide_L = Slider(-1,rect_l,10)
    rect_r = pygame.Rect(870,315,10,70)
    Slide_R = Slider(1,rect_r,10)
    Ball_R = pygame.Rect(450-10,350-10,20,20)
    ball = Ball(10,Ball_R,0,0)
    move_of = 0
MOVE_SPEED = 20
MOVE_SPACE = [10,690]


def draw_slides(slide,screen):
    for i in slide:
        pygame.draw.rect(screen, (255,255,255), i.rect)
def draw_balls(ball):
    pygame.draw.circle(screen, (255, 255, 255), ball.centre_pos,ball.radius)
    # pygame.draw.rect(screen, (255, 255, 255), Ball_R,2)

def draw_text(display_surface,text,side):
    font = pygame.font.Font('./DeliciousHandrawn-Regular.ttf', 25)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(text, True, (255,255,255), (0,0,0))
    textRect = text.get_rect()
    if side ==-1:
        textRect.top = 650
        textRect.left = 10
    else:
        textRect.top = 650
        textRect.left = 900 - textRect.width - 5
    display_surface.blit(text, textRect)

def draw_names(name,side,display_surface):
    font = pygame.font.Font('./DeliciousHandrawn-Regular.ttf', 25)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(name, True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    if side == -1:
        textRect.top = 20
        textRect.left = 450 - textRect.width - 10
    else:
        textRect.top = 20
        textRect.left = 460
    display_surface.blit(text, textRect)

def start_text(display_surface,flag):
    font = pygame.font.Font('./DeliciousHandrawn-Regular.ttf', 35)

    # create a text surface object,
    # on which text is drawn on it.

    if flag == 0:
        text = font.render("Press SPACE button to Start", True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.top = SCREEN_SIZE[1]/2 - textRect.height/2 - 100
    else:
        text = font.render(f"Last Match Winner-->{Left if lastWon ==-1 else Right}", True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.top = SCREEN_SIZE[1]/2 - textRect.height/2 +100

    textRect.left = SCREEN_SIZE[0]/2 - textRect.width/2

    display_surface.blit(text, textRect)

def draw_score(number,side,display_surface):
    font = pygame.font.Font('./DeliciousHandrawn-Regular.ttf', 25)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(f'Score:{number}/{no_lose}', True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    if side == -1:
        textRect.top = 20
        textRect.left = 20
    else:
        textRect.top = 20
        textRect.left = 800
    display_surface.blit(text, textRect)

def clamp_move():
    global Slide_R,Slide_L
    key_object = pygame.key.get_pressed()

    if key_object[pygame.K_w]:
        Slide_L.rect.top -= MOVE_SPEED
    elif key_object[pygame.K_s]:
        Slide_L.rect.top += MOVE_SPEED

    if key_object[pygame.K_UP]:
        Slide_R.rect.top -= MOVE_SPEED
    elif key_object[pygame.K_DOWN]:
        Slide_R.rect.top += MOVE_SPEED

    if Slide_L.rect.top <= 5:
        Slide_L.rect.top = 5
    if Slide_L.rect.top + 75 >= SCREEN_SIZE[1]:
        Slide_L.rect.top = SCREEN_SIZE[1] - 75

    if Slide_R.rect.top <= 5:
        Slide_R.rect.top = 5
    if Slide_R.rect.top + 75 >= SCREEN_SIZE[1]:
        Slide_R.rect.top = SCREEN_SIZE[1] - 75

make_new_game()
while running:


    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_object = pygame.key.get_pressed()
    if active == False:
        start_text(screen,0)
        if lastWon !=0:
            start_text(screen,1)
        draw_text(screen, 'Move with W and S', -1)
        draw_text(screen, 'Move with Up and Down', 1)
        if key_object[pygame.K_SPACE]:
            dirs = [-1,1]
            active = True
            x = random.choice(dirs)
            ball.x_v = x * random.randint(6,8)
            ball.y_v =  random.choice(dirs) * random.randint(2,4)
            move_of = x
    
    if active == True:
        if key_object[pygame.K_w]:
            Slide_L.clamp_move(-1,MOVE_SPACE)
        elif key_object[pygame.K_s]:
            Slide_L.clamp_move(+1, MOVE_SPACE)

        if key_object[pygame.K_UP]:
            Slide_R.clamp_move(-1,MOVE_SPACE)
        elif key_object[pygame.K_DOWN]:
            Slide_R.clamp_move(+1, MOVE_SPACE)

    # Moving
    ball.make_move(move_of)
    # Collision
    collide = ball.collision_detect([Slide_R,Slide_L])
    if collide !=None:
        move_of =  -collide
        pygame.mixer.Sound.play(SOUND)
    # Drawing
    draw_slides([Slide_L,Slide_R],screen)
    draw_balls(ball)



    win = ball.check_win()
    if win == -1:
        active = False
        make_new_game()
        print(f"{Left} 🏆")
        win = None
        left_win +=1
        lastWon = -1
        if left_win == no_lose:
            print(f"🏆🏆🏆🏆 {Left} 🏆🏆🏆🏆")
            break
    if win == 1:
        active = False
        make_new_game()

        print(f"{Right} 🏆")
        win = None
        right_win +=1
        lastWon = 1
        if right_win == no_lose:
            print(f"🏆🏆🏆🏆 {Right} 🏆🏆🏆🏆")
            break
    pygame.draw.line(screen,(255,255,255),(450,0),(450,700))



    draw_names(Left,-1,screen)
    draw_names(Right,1,screen)
    draw_score(left_win,-1,screen)
    draw_score(right_win,1,screen)

    pygame.display.update()