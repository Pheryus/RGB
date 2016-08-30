import pygame

class Window():

    def __init__(self, tamanho, qd):
        #pygame.display.list_modes()[0]
        self.tela = pygame.display.set_mode([1360,768])
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.bx = (self.width - (tamanho * (qd + 2))) / 2
        self.by = (self.height - (tamanho * (qd + 2))) / 2
        self.qd = qd
        self.tam = tamanho
