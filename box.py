import pygame
from pygame.locals import *



class box():
    def __init__(self,screen,startX) -> None:
        self.voxel=[[0 for i in range(10)] for j in range(10)]
        self.startX=startX
        self.startY=50
        self.screen=screen
        self.width=40

    def draw(self):
        mouseX,mouseY=pygame.mouse.get_pos()
        if(self.startX+400>mouseX>self.startX and self.startY+400>mouseY>self.startY):
            mouseState=pygame.mouse.get_pressed()
            if(mouseState[0]):
                self.voxel[int((mouseX-self.startX)/40)][int((mouseY-self.startY)/40)]=1
            elif(mouseState[2]):
                self.voxel[int((mouseX-self.startX)/40)][int((mouseY-self.startY)/40)]=0


        for i in range(10):
            for j in range(10):
                if self.voxel[i][j]==1:
                    pygame.draw.rect(self.screen,(0, 179, 164),(self.startX+i*self.width,self.startY+j*self.width,self.width,self.width))
                    pygame.draw.rect(self.screen,((0,0,0)),(self.startX+i*self.width,self.startY+j*self.width,self.width,self.width),1)
                else:
                    pygame.draw.rect(self.screen,(255,255,255),(self.startX+i*self.width,self.startY+j*self.width,self.width,self.width))
                    pygame.draw.rect(self.screen,((0,0,0)),(self.startX+i*self.width,self.startY+j*self.width,self.width,self.width),1)

        pygame.draw.rect(self.screen,(0, 255, 0),(self.startX,self.startY,400,400),4)