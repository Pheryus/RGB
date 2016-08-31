import pygame, sys


class Menu():
    def __init__(self,font,loop, window):
        print(pygame.image.get_extended())
        self.image = pygame.image.load("pictures/rgb.png").convert_alpha()
        self.opcao = 0 #posição que começa selecionada
        self.start = 0 #jogo em andamento
        self.loop = loop #classe loop
        self.time = 100
        self.font = font
        self.window = window
        self.menuSE = pygame.mixer.Sound("sounds/menu.wav")
        self.loop_menu()
        self.choiceSE = pygame.mixer.Sound("sounds/action.ogg")


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

        self.keyboardControl()
        self.mouseControl(  )

    def keyboardControl(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.option_set(-1)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.option_set(1)
        elif pygame.key.get_pressed()[pygame.K_RETURN] or pygame.key.get_pressed()[pygame.K_SPACE]:
            self.menuSE.play()
            self.loop.limpa_testa()
            self.calls()



    def mouseControl(self):
        pos = pygame.mouse.get_pos()
        print(pos)
        for i in range(0,3):
            if (pos[0] >= self.window.width*0.33 and pos[0] <= self.window.width*0.33 + self.font.sizeWord(self.font.menuDictionary[i],self.font.size) and pos[1] >= self.window.height*0.28 + 200*i and pos[1] <= self.window.height*0.35 + 220*i):
                self.opcao = i

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
