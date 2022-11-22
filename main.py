import pygame
from pygame.locals import *
import sys
from box import box
from convert import makeVoxel

 
pygame.init()

density=10;
boxArm=400;

width, height = 1200, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Show Text')
 

font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render('Top', True, (179, 0, 0), (255, 217, 0))
text2 = font.render('Front', True, (179, 0, 0), (255, 217, 0))
text3 = font.render('Side', True, (179, 0, 0), (255, 217, 0))


voxelTop=box(screen,0)
voxelFront=box(screen,boxArm)
voxelSide=box(screen,boxArm*2)


while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():

    if event.type == QUIT:
      pygame.quit()
      makeVoxel(voxelTop.voxel,voxelFront.voxel,voxelSide.voxel,"mesh4")
      sys.exit()
      break;
  
  screen.blit(text1, (200, 0))
  screen.blit(text2, (600, 0))
  screen.blit(text3, (1000, 0))

  voxelTop.draw()
  voxelFront.draw()
  voxelSide.draw()



  pygame.display.update()

  
