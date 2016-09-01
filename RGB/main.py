from engine.control import Control, Fonts, Window
from engine.player import Player
from engine.scenes import Menu, LoopControl
import sys
import pygame


def main():
    tam = 9
    #inicializa pygame
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.display.set_caption("RGB")
    pygame.mixer.music.load('songs/Universal.ogg')
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1)
    #criar um contador de tempo
    timer = pygame.time.Clock()
    FPS = 15

    #inicializa Window
    window = Window(9,60)
    #numeroplayers
    nplayers = 2
    #cria classe Controle
    controle = Control(tam,nplayers,window)
    #inicializa fonte
    fonte = Fonts(nplayers,controle, window)

    jogo = 1
    loop_control = LoopControl(FPS,window,timer)
    #inicializa menu
    menu = Menu(fonte, loop_control,window)
    pygame.time.wait(300)
    while jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
        loop_control.limpa_testa()
        fonte.atualiza_fonts(controle,nplayers)
        controle.loop_control(nplayers,timer, window)
        loop_control.loop()
        jogo = controle.end_game()


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
