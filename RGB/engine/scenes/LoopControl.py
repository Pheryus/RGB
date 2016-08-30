import pygame, sys




class LoopControl():
    
    def __init__(self,fps,window,timer):
        self.fps = fps
        self.window = window
        self.timer = timer
        self.playtime = 0.0

    def limpa_testa(self, time=1):
        pygame.time.wait(time)
        self.window.tela.fill((255,255,255))
        for evento in pygame.event.get():
            if evento.type is pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_F4] and pygame.key.get_pressed()[pygame.K_LALT]:
                    pygame.quit()
                    sys.exit(0)
    
    def loop(self):
        pygame.display.flip()
        milisegundos = self.timer.tick(self.fps)
        self.playtime += milisegundos/1000
        #print framerate and playtime in titlebar
        text = "FPS: {0: .2f} Playtime : {1:.2f}".format(self.timer.get_fps(),self.playtime)
        pygame.display.set_caption(text)

    def quit(self):
        pygame.quit()
        sys.exit(0)
