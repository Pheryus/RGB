import pygame, sys


class Menu():
    def __init__(self,font,loop):
        print(pygame.image.get_extended())
        self.image = pygame.image.load("pictures/rgb.png").convert_alpha()
        self.opcao = 0 #posição que começa selecionada
        self.start = 0 #jogo em andamento
        self.loop = loop #classe loop
        self.time = 100
        self.font = font
        self.menuSE = pygame.mixer.Sound("sounds/menu.wav")
        self.loop_menu()



    def loop_menu(self):
        while (not self.start):
            self.loop.limpa_testa(150)
            self.choose_options()
            self.font.atualiza_menu(self.opcao)
            self.loop.loop()
 ##iniciar
 ##opções
 ##tutorial
 ##sair

    def choose_options(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.option_set(-1)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.option_set(1)
        elif pygame.key.get_pressed()[pygame.K_RETURN] or pygame.key.get_pressed()[pygame.K_SPACE]:
            self.menuSE.play()
            self.loop.limpa_testa()
            self.calls()

    def calls(self):
        if self.opcao == 0:
            self.start = 1
        elif self.opcao == 1:
            self.options()
        elif self.opcao == 2:
            self.loop.quit()

    def options(self):
        print ("Nada ainda")


    def option_set(self, v):
        if self.opcao + v < 0:
            self.opcao = 2
        elif self.opcao + v == 3:
            self.opcao = 0
        else:
            self.opcao += v
