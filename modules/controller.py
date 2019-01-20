import pygame, os
from .player import Player
from .spike_ball import spike_ball
from .gui import Gui
from .database import Database

class Controller:
	def __init__(self):
		self.sprites=[]
		self.spike_ballGroup = pygame.sprite.Group()
		self.screen_width = 600
		self.screen_height = 500
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.loadArt()
		self.count_second=0
		self.thegui = Gui()
		self.theplayer = Player(50, 50, self.screen_width, self.screen_height, self.sprites[0])
		

		#for i in range(3):
		self.spike_ballGroup.add(spike_ball(0, 450, self.screen_width, self.screen_height, self.sprites[1]))
		self.spike_ballGroup.add(spike_ball(550, 450, self.screen_width, self.screen_height, self.sprites[1]))	
		self.spike_ballGroup.add(spike_ball(275, 450, self.screen_width, self.screen_height, self.sprites[1]))	
		

	def loadArt(self):
		self.sprites.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'../Images/player.png')))
		self.sprites.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'../Images/spike_ball.png')))

	def processUserInput(self):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				quit()

		keys = pygame.key.get_pressed()
		self.theplayer.turning = keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]
		self.theplayer.forward = keys[pygame.K_UP]
		self.theplayer.backward = keys[pygame.K_DOWN]

	def updateGame(self, dt):
		self.theplayer.update(dt, self.thegui.score, self.count_second )
		for a in self.spike_ballGroup.sprites():
			a.update(dt)

		collide_list = pygame.sprite.spritecollide(self.theplayer, self.spike_ballGroup, True)

		if collide_list:
			pygame.quit()
			self.thedatabase = Database(self.thegui.score, self.count_second)
			quit()
		else:
			self.thegui.score += .5

		self.count_second = int(self.thegui.score/100)

	def drawScreen(self):
		self.screen.fill((0,0,0))
		self.theplayer.draw(self.screen)
		
		for a in self.spike_ballGroup.sprites():
			a.draw(self.screen)

		self.thegui.draw(self.screen)

		pygame.display.flip()