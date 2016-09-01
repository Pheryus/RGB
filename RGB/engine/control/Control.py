from engine.player import Player
from engine.control import Window
import pygame
import operator



cor = [(255,255,255), (255,0,0),(0,255,0), (0,0,255), (255,255,0),(255,0,255)]


class Control():

    def __init__(self, tam,nplayers,borda):
        self.matriz = [[ None for i in range(tam)] for j in range(tam)]
        self.atual = 0
        self.tam = tam
        #self.sprites = [[pygame.image.load("/..sprites.convert_alpha() for i in range(1,9)]
        self.players = [0 for i in range (nplayers)]
        self.cria_player(nplayers,borda)
        self.som = [ pygame.mixer.Sound("sounds/som" + str(i) +".wav") for i in range(4) ]

        self.actionsound = pygame.mixer.Sound("sounds/action.ogg")
        self.start = 0
        self.turns = 0



    def cria_player(self,nplayer, borda):
        for i in range(nplayer):
            self.players[i] = Player(cor[i+4],cor[i+1], borda,i)

    def desenha_players(self,tela,nplayers):
        for i in range(nplayers):
            self.players[i].desenha_personagem(tela)

    def loop_control(self,nplayers,time, window):
        if (not self.start):
            self.som[0].play()
            self.start = 1
            pygame.time.wait(1000)
        self.move_players(window,nplayers,time)
        self.color_player(nplayers,time)
        self.desenha_cor_personagem(nplayers,window)
        self.desenha_tela_borda(window)
        self.desenha_players(window,nplayers)


    def end_game(self):
        if (self.turns == 81):
            if self.players[0] == self.players[1]:
                print("EMPATE")
            elif self.players[0] >= self.players[0]:
                print("PLAYER 1 GANHOU!")
            else:
                print("PLAYER 2 GANHOU!")
            return False
        return True


    def move_players(self,borda, nplayers,time):

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.players[0].move_pos([0,1],borda.tam)
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.players[0].move_pos([0,-1],borda.tam)
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.players[0].move_pos([-1,0],borda.tam)
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.players[0].move_pos([1,0],borda.tam)
            if pygame.key.get_pressed()[pygame.K_d]:
                self.players[1].move_pos([0,1],borda.tam)
            if pygame.key.get_pressed()[pygame.K_a]:
                self.players[1].move_pos([0,-1],borda.tam)
            if pygame.key.get_pressed()[pygame.K_w]:
                self.players[1].move_pos([-1,0],borda.tam)
            if pygame.key.get_pressed()[pygame.K_s]:
                self.players[1].move_pos([1,0],borda.tam)

    def color_player(self,nplayer,time):
        i = self.atual
        mudacor = cor[0]
        if self.players[i].cor == cor[1]:
            mudacor = cor[3]
        elif self.players[i].cor == cor[2]:
            mudacor = cor[1]
        else:
            mudacor = cor[2]
        x = self.players[i].posicao[0]
        y = self.players[i].posicao[1]
        if (pygame.key.get_pressed()[pygame.K_RETURN] and self.atual == 0 ) or (pygame.key.get_pressed()[pygame.K_SPACE] and self.atual == 1):
            self.turns += 1
            self.actionsound.play()
            if not self.matriz[x][y]:
                self.matriz[x][y] = self.players[i].cor
                self.players[i].cor = mudacor
                self.checkPoints(x,y)
                if self.atual == nplayer-1:
                    self.atual = 0
                else:
                    self.atual += 1

    def desenha_tela_borda(self,window):
        for i in range(window.tam):
            for j in range(window.tam):
                if (not self.matriz[j][i]):
                    actualcolor = (255,255,255)
                else:
                    actualcolor = self.matriz[j][i]
                pygame.draw.rect(window.tela,actualcolor, (window.qd*i + window.bx,window.qd*j + window.by, window.qd,window.qd),0)
                pygame.draw.rect(window.tela,(0,0,0), (window.qd*i + window.bx,window.qd*j + window.by, window.qd,window.qd),1)


    def desenha_cor_personagem(self,nplayers,borda):
        pygame.draw.rect(borda.tela,self.players[0].cor,((int)(borda.bx / 4), borda.by + 180, borda.qd,borda.qd),0)
        pygame.draw.rect(borda.tela,self.players[1].cor,((int)(borda.width - 3*borda.bx/4), borda.by + 180, borda.qd,borda.qd),0)

    def getAdjacentsColors(self,adjsize, actualcolor,x,y):
        index = 0
        adjcolor = [None for i in range(25)]
        for i in range (adjsize[0],adjsize[1]):
            for j in range(adjsize[0],adjsize[1]):
                #TEST IF IT'S OUTSIDE THE SCREEN
                if abs(i)+abs(j) not in (0,3):
                    if x+i >= 0 and x+i < self.tam and y+j >= 0 and y+j < self.tam:
                        if self.matriz[x+i][y+j] != actualcolor:
                            adjcolor[index] = self.matriz[x+i][y+j]
                    index += 1
        return adjcolor

    def checkGreenAdjacentsColors(self, vizg):
        for i in range(4):
            if vizg[i] and vizg[7-i] and tuple(map(operator.add, vizg[i], vizg[7-i])) == (255,0,255):
                 self.players[self.atual].pontos += 1

    def checkOtherAdjacentsColors(self, actualcolor, adj):

        #checking diagonals
        for i in range(3):
            #red test
            if (actualcolor == (255,0,0)):
                if (adj[i] and adj[i+3] and adj[i][2]+adj[i+3][1] == 510):
                    self.players[self.atual].pontos += 1
                if (adj[i+10] and adj[i+13] and adj[i+10][1]+adj[i+13][2] == 510):
                    self.players[self.atual].pontos += 1
            #blue test
            else:
                if (adj[i] and adj[i+3] and adj[i][0]+adj[i+3][1] == 510):
                    self.players[self.atual].pontos += 1
                if (adj[i+10] and adj[i+13] and adj[i+10][1] + adj[i+13][0] == 510):
                    self.players[self.atual].pontos += 1

        #checking vertical and horizontal
        #red check
        if (actualcolor == (255,0,0)):
            if (adj[6] and adj[7] and adj[6][2] + adj[7][1] == 510):
                self.players[self.atual].pontos += 1
            if (adj[8] and adj[9] and adj[8][1] +  adj[9][2] == 510):
                self.players[self.atual].pontos += 1
        #blue check
        else:
            if (adj[6] and adj[7] and adj[6][0] + adj[7][1] == 510):
                self.players[self.atual].pontos += 1
            if (adj[8] and adj[9] and adj[8][1] + adj[9][0] == 510):
                self.players[self.atual].pontos += 1


    def checkPoints(self,x,y):
        pts = self.players[self.atual].pontos
        actualcolor = self.matriz[x][y]
        neightborhood = [ (-1,2), (-2,3)]
        #if it's green
        if actualcolor == (0,255,0):
            self.checkGreenAdjacentsColors(self.getAdjacentsColors(neightborhood[0], actualcolor,x,y))

        #red or green
        else:
            self.checkOtherAdjacentsColors(actualcolor, (self.getAdjacentsColors(neightborhood[1], actualcolor,x,y)))

        self.getPoints(pts)


    def getPoints(self, pts):
        pts -= self.players[self.atual].pontos
        pts = abs(pts)
        if (pts>0):
            self.som[pts].play()
