

import pygame
import random

BLACK=(0,0,0)
PURPLE=(100,25,150)
screen_w,screen_h = 500,500

background_color=(230,230,250)
pygame.init()
screen=pygame.display.set_mode((screen_w,screen_h))
clock=pygame.time.Clock()

class Drop:
    def __init__(self):
        self.update()
        

    def update(self):
        self.x=random.randrange(0,screen_w)
        self.y=random.randrange(0,screen_h)
        self.w= random.randint(4,8)
        self.h=(2*self.w)
        

    def fall(self):
        self.y += 1
        if self.y> screen_h:
            self.y=0-self.h
    
    def show(self):
        pygame.draw.rect(screen,PURPLE, [self.x,self.y,self.w,self.h])

    
def game_loop():
    d = [Drop() for i in range(6)]
    while True:
        screen.fill(BLACK)
        for events in pygame.event.get():
            if events.type ==pygame.QUIT:
                pygame.quit()
                quit()
        for drop in d:
            drop.show()
            drop.fall()
        pygame.display.update()
        
        clock.tick(60)

if __name__=="__main__":    
    game_loop()
    pygame.quit()
    quit()