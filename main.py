import pygame as pg

def init():
    pg.init()

    width = 800
    height = 600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Alien')

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pg.display.flip()

if __name__ == '__main__':
    init()