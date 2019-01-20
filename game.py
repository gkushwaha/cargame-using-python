import pygame
from modules import *

pygame.init()

gController = Controller()

clock = pygame.time.Clock()

while True:
	dt = clock.tick(200)

	gController.processUserInput()

	gController.updateGame(dt/1000)

	gController.drawScreen()
