import pygame
#from engine.control import Window
class Player():
    def __init__(self,imagem,cor, borda,ordem):
        self.posicao = [0,0]
        self.imagem = imagem
        self.cor = cor
        self.pontos = 0
        self.bx = borda.bx
        self.by = borda.by
        self.qd = borda.qd
        self.ordem = ordem

    def getpontos(self):
        self.pontos += 1

    def desenha_personagem(self,window):
        inix = self.bx + self.posicao[1]*self.qd
        iniy = self.by + self.posicao[0]*self.qd
        fimx = self.bx + (1 + self.posicao[1])*self.qd
        fimy = self.by + (1 + self.posicao[0])*self.qd
        if self.ordem == 0:
            pygame.draw.polygon(window.tela, self.imagem,((inix,iniy),(fimx, iniy), (fimx,fimy)), 0)
        else:
            pygame.draw.polygon(window.tela,self.imagem,((inix,iniy), (inix,fimy), (fimx,fimy)), 0)        

    def move_pos(self,coor,tam):
        for i in range(2):
            if (self.posicao[i] < tam-1 and coor[i] == 1) or (self.posicao[i] > 0 and  coor[i] == -1):
                self.posicao[i] += coor[i]
        
        
