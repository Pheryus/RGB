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
        self.som = [ pygame.mixer.Sound("sounds/som" + str(i) +".wav") for i in range(3) ]
        self.actionsound = pygame.mixer.Sound("sounds/action.ogg")
        self.start = 0

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
            self.actionsound.play()
            if not self.matriz[x][y]:
                self.matriz[x][y] = self.players[i].cor
                self.players[i].cor = mudacor
                self.testa_pontos(x,y)
                if self.atual == nplayer-1:
                    self.atual = 0
                else:
                    self.atual += 1

    def desenha_tela_borda(self,window):
        for i in range(window.tam):
            for j in range(window.tam):
                if (not self.matriz[j][i]):
                    aux = (255,255,255)
                else:
                    aux = self.matriz[j][i]
                pygame.draw.rect(window.tela,aux, (window.qd*i + window.bx,window.qd*j + window.by, window.qd,window.qd),0)
                pygame.draw.rect(window.tela,(0,0,0), (window.qd*i + window.bx,window.qd*j + window.by, window.qd,window.qd),1)


    def desenha_cor_personagem(self,nplayers,borda):
        pygame.draw.rect(borda.tela,self.players[0].cor,((int)(borda.bx / 4), borda.by + 180, borda.qd,borda.qd),0)
        pygame.draw.rect(borda.tela,self.players[1].cor,((int)(borda.width - 3*borda.bx/4), borda.by + 180, borda.qd,borda.qd),0)

    def testa_pontos(self,x,y):
        pts = self.players[self.atual].pontos
        aux = self.matriz[x][y]
        vizo = [None for i in range(25)]
        vizg = [None for i in range(16)]
        v1 = 0
        #se for verde
        if aux == (0,255,0):
            for i in range (-1,2):
                for j in range(-1,2):
                    if x+i >= 0 and x+i < self.tam and y+j >= 0 and y+j < self.tam and self.matriz[x+i][y+j] != aux:
                        vizg[v1] = self.matriz[x+i][y+j]
                    v1 += 1
            for i in range(4):
                if vizg[i] and vizg[8-i] and tuple(map(operator.add, vizg[i], vizg[8-i])) == (255,0,255):
                     self.players[self.atual].pontos += 1
        #azul ou vermelho
        else:
            for i in range(-2,3):
                for j in range(-2,3):
                    if abs(i)+abs(j) not in (0,3):
                        if x+i >= 0 and x+i < self.tam and y+j >= 0 and y+j < self.tam:
                            vizo[v1] = self.matriz[x+i][y+j]
                        v1 += 1
            print (vizo)
            for i in range(3):
                #se for vermelho
                print (i)
                if (aux == (255,0,0)):
                    if (vizo[i] and vizo[i+3] and vizo[i][1]+vizo[i+3][2] == 510):
                        print ("aqui1")
                        self.players[self.atual].pontos += 1
                    if (vizo[i+10] and vizo[i+13] and vizo[i+10][1]+vizo[i+13][2] == 510):
                        print ("aqui2")
                        self.players[self.atual].pontos += 1
                else:
                    if (vizo[i] and vizo[i+3] and vizo[i][0]+vizo[i+3][1] == 510):
                        print ("aqui3")
                        self.players[self.atual].pontos += 1
                    if (vizo[i+10] and vizo[i+13] and vizo[i+10][1] + vizo[i+13][0] == 510):
                        print ("aqui4")
                        self.players[self.atual].pontos += 1

            if (aux == (255,0,0)):
                if (vizo[6] and vizo[7] and vizo[6][2] + vizo[7][1] == 510):
                    print ("geba2")
                    self.players[self.atual].pontos += 1
                if (vizo[8] and vizo[9] and vizo[8][1] +  vizo[9][2] == 510):
                    print ("geba3")
                    self.players[self.atual].pontos += 1
            #se for azul
            else:
                if (vizo[6] and vizo[7] and vizo[6][0] + vizo[7][1] == 510):
                    print ("geba1")
                    self.players[self.atual].pontos += 1
                if (vizo[8] and vizo[9] and vizo[8][1] + vizo[9][0] == 510):
                    print ("geba2")
                    self.players[self.atual].pontos += 1
        v1 = 0
        pts -= self.players[self.atual].pontos
        pts = abs(pts)
        if (pts>0):
            self.som[pts].play()
