import pygame

class Fonts():
    def __init__(self,nplayers,controle, window):
        #self.tam = 60*1368
        self.window = window
        self.size = 60
        self.font1 = pygame.font.Font("fonts/fonte.ttf",self.size)
        self.menuDictionary = ["New Game", "Options", "Quit" ]

        self.menu_font = pygame.font.Font("fonts/menu_font.ttf",(int)(self.size*1.5))
        self.menu_font2 = pygame.font.Font("fonts/menu_font.ttf",self.size*2)

        self.menu_options_target = [ self.menu_font2.render(self.menuDictionary[i], True, (255,0,0)) for i in range (0,3)]
        self.menu_options = [ self.menu_font.render(self.menuDictionary[i], True, (0,0,0)) for i in range (0,3)]

        self.text1 = self.font1.render('Player 1', True, (0,0,0))
        self.text2 = self.font1.render('Player 2', True, (0,0,0))
        self.title = self.menu_font.render('RGB', True, (0,0,0))
        self.points = [0 for i in range(nplayers)]
        self.cor1 = self.font1.render('Cor ', True,(0,0,0))
        self.cor2 = self.font1.render('Cor ',True,(0,0,0))
        self.nplayers = nplayers

    def sizeWord(self,word,chsize):
        value = (len(word)*(chsize/2) + chsize) * (1360/self.window.width)
        return value

    def atualiza_pontos(self,controle):
        for i in range(self.nplayers):
            self.points[i] = self.font1.render('Pontos: ' + str(controle.players[i].pontos), True, (0,0,0))

    def atualiza_menu(self, opt):
        for i in range(len(self.menu_options)):
            if i != opt:
                self.window.tela.blit(self.menu_options[i], ( (int) (self.window.width * 0.33 ), (int) ((i+1)*200)))

        self.window.tela.blit(self.menu_options_target[opt],( (int) (self.window.width * 0.33), (int) ((opt+1)*200)))


    def atualiza_fonts(self,controle, nplayers):
        self.atualiza_pontos(controle)
        self.window.tela.blit(self.title, ( (int) (self.window.width / 2) - 90, 0 ) )
        self.window.tela.blit(self.points[0], ((int) (self.window.bx / 4) , self.window.by + 60))
        self.window.tela.blit(self.points[1], ((int) (self.window.width - 3*self.window.bx/4), self.window.by+60))
        self.window.tela.blit(self.text1,( (int) (self.window.bx / 4) ,self.window.by))
        self.window.tela.blit(self.text2, ( (int) (self.window.width - 3*self.window.bx/4), self.window.by))
        self.window.tela.blit(self.cor1, ((int) (self.window.bx / 4), self.window.by + 120))
        self.window.tela.blit(self.cor2, ((int) (self.window.width - 3*self.window.bx/4), self.window.by + 120))
