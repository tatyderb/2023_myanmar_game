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
display.blit(background_img, (0, 0))

# шрифт для букв
sysfont = pg.font.SysFont('arial', 40)
text_img = sysfont.render('Score: 123', True, 'red')

font = pg.font.Font('resources/font/04B_19__.TTF', 48)
game_over_img = font.render('Game Over', True, 'white')
w = game_over_img.get_width()
h = game_over_img.get_height()
x = screen_width/2 - w/2
y = screen_height/2 - h/2
display.blit(game_over_img, (x, y))

running = True
while running:
    # рисовать
    display.fill('blue', (20, 50, 100, 250))
    display.blit(text_img, (100, 200))
    pg.display.update()

    # получить события игры и обработать их
    for event in pg.event.get():
        # нажали на Х и закрыли окно
        if event.type == pg.QUIT:
            running = False
        # нажали на клавишу q и закрыли окно
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            running = False




pg.quit()

