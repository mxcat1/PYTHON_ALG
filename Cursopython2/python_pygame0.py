import pygame,sys
from pygame.locals import *

WIDTH=650
HEIGHT=450

def load0_imagen(filename,transparent=False):
    try: imagen=pygame.image.load(filename)
    except pygame.error, message:
            raise SystemExit, message
    imagen=imagen.convert()
    if transparent:
            color=imagen.get_at((0,0))
            imagen.set_colorkey(color,RLEACCEL)
    return imagen

def main():
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("PYgame juego")
    background_image = load0_imagen('dota2.jpg')
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                sys.exit(0)
        screen.blit(background_image, (0,0))
        pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()
    main()