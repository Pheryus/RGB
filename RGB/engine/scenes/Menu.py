import pygame, sys


class Menu():
    def __init__(self,font,loop, window):
        self.image = pygame.image.load("pictures/rgb.png").convert_alpha()
        self.opcao = 0 #posição que começa selecionada
        self.start = 0 #jogo em andamento
        self.loop = loop #classe loop
        self.time = 100
        self.font = font
        self.window = window
        self.menuSE = pygame.mixer.Sound("sounds/menu.wav")
        self.choiceSE = pygame.mixer.Sound("sounds/action.ogg")
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

        self.keyboardControl()
        self.mouseControl(  )

    def keyboardControl(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.option_set(-1)
            self.choiceSE.play()
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.option_set(1)
            self.choiceSE.play()
        elif pygame.key.get_pressed()[pygame.K_RETURN] or pygame.key.get_pressed()[pygame.K_SPACE]:
            self.startGame()

    def startGame(self):
        self.menuSE.play()
        self.loop.limpa_testa()
        self.calls()

    def checkMouseCollision(self,i, pos):
        return (pos[0] >= self.window.width*0.33 and pos[0] <= self.window.width*0.33 + self.font.sizeWord(self.font.menuDictionary[i],self.font.size) and pos[1] >= self.window.height*0.28 + 200*i and pos[1] <= self.window.height*0.35 + 220*i)

    def mouseControl(self):
        pos = pygame.mouse.get_pos()
        for i in range(0,3):
            if self.opcao != i:
                if self.checkMouseCollision(i,pos):
                    self.choiceSE.play()
                    self.opcao = i
                    break

        checkMouse = pygame.mouse.get_pressed()
        if checkMouse[0]:
            if self.checkMouseCollision(0,pos):
                self.startGame()




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
