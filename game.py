import pygame as pg

pg.init()

screen_width = 800
screen_height = 600

display = pg.display.set_mode((screen_width, screen_height))
# display.fill('pink', (0, 0, screen_width, screen_height))
pg.display.set_caption('Космическое вторжение')
icon_img = pg.image.load('resources/img/ufo.png')
pg.display.set_icon(icon_img)

background_img = pg.image.load('resources/img/background.png')

# шрифт для букв
sysfont = pg.font.SysFont('arial', 40)
text_img = sysfont.render('Score: 123', True, 'red')
# display.blit(text_img, (100, 200))

'''
font = pg.font.Font('resources/font/04B_19__.TTF', 48)
game_over_img = font.render('Game Over', True, 'white')
w = game_over_img.get_width()
h = game_over_img.get_height()
x = screen_width/2 - w/2
y = screen_height/2 - h/2
display.blit(game_over_img, (x, y))
'''

# player
player_img = pg.image.load('resources/img/player.png')
player_width = player_img.get_width()
player_height = player_img.get_height()
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height
player_velocity = 1
player_dx = 0

# пуля
bullet_img = pg.image.load('resources/img/bullet.png')
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()
bullet_x = 0
bullet_y = 0
bullet_dy = -2
bullet_visible = False  # есть пуля в игре True, или её нет False

# enemy
enemy_img = pg.image.load('resources/img/enemy.png')
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()
enemy_x = player_x
enemy_y = 0
enemy_dx = 0
enemy_dy = 1

import random
def enemy_create():
    global enemy_x, enemy_y
    enemy_x = random.randint(0, screen_width)
    enemy_y = 0

def bullet_create():
    global bullet_y, bullet_x, bullet_visible
    bullet_x = player_x
    bullet_y = player_y - bullet_height
    bullet_visible = True

def model_update():
    """ Изменяет математическую модель игры."""
    player_model()
    bullet_model()
    enemy_model()

def enemy_model():
    global enemy_x, enemy_y
    enemy_x += enemy_dx
    enemy_y += enemy_dy

def player_model():
    # изменяем математическую модель
    global player_x
    player_x = player_x + player_dx
    if player_x < 0:
        player_x = 0
    if player_x + player_width > screen_width:
        player_x = screen_width - player_width

def bullet_model():
    # пуля летит, если она видна
    global bullet_visible, bullet_y
    if bullet_visible:
        bullet_y = bullet_y + bullet_dy
        # если пуля улетела за границу экрана, ее не видно
        if bullet_y < 0:
            bullet_visible = False
            print(f"{bullet_visible=}")
        # если пуля попала во врага
        rect_bullet = pg.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
        rect_enemy = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        # есть пересечение прямоугольников?
        if (rect_enemy.colliderect(rect_bullet)):
            print('BANG!!!!')
            enemy_create()


def redraw():
    # рисовать
    # display.fill('blue', (20, 50, 100, 250))
    display.blit(background_img, (0, 0))
    display.blit(player_img, (player_x, player_y))
    if bullet_visible:
        display.blit(bullet_img, (bullet_x, bullet_y))
    display.blit(enemy_img, (enemy_x, enemy_y))
    pg.display.update()

def event_process():
    """ Обработка событий: клавиши, мышь, Х """
    global player_dx
    running = True
    # получить события игры и обработать их
    for event in pg.event.get():
        # нажали на Х и закрыли окно
        if event.type == pg.QUIT:
            running = False
        # нажали на клавишу q и закрыли окно
        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            running = False

        # клавиши <- и -> игрок движется влево или вправо
        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            player_dx = - player_velocity
        if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            player_dx = player_velocity
        # отпустила клавишу - игрок СТОП!!!!!
        if event.type == pg.KEYUP and event.key == pg.K_LEFT:
            player_dx = - 0
        if event.type == pg.KEYUP and event.key == pg.K_RIGHT:
            player_dx = 0

        # стреляем по клавише ПРОБЕЛ
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            if not bullet_visible:
                bullet_create()
                print('Fire!')

    return running

# все функции закончились, опять global namespace
running = True
while running:
    model_update()
    redraw()
    running = event_process()

pg.quit()

