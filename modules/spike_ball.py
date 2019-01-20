import pygame, random
from .objectfunction import rot_center

class spike_ball(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, img):
		pygame.sprite.Sprite.__init__(self)
		self.image=img
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = 0, 450
		self.x, self.y = x, y
		self.screen_width = width
		self.screen_height = height
		self.angle= random.randrange(360)
		self.turningSpeed = random.randrange(-360, 360)
		self.xVel, self.yVel = 50, 50

	def update(self, dt):
		self.angle += self.turningSpeed *dt
		self.dx = self.xVel * dt
		self.dy = self.yVel * dt
		self.x += self.dx
		self.y += self.dy

		self.rect.x = self.x
		self.rect.y = self.y

		

		if ((self.rect.y < 0) or (self.rect.y > self.screen_height - 50)):
			self.yVel *= -1
			

		if((self.rect.x<0) or (self.rect.x > self.screen_width - 50)):
			self.xVel *= -1

		#if(self.angle > 360):
		#	self.angle -=360
		#elif(self.angle < 0):
		#	self.angle +=360

	def draw(self, screen):
		newImage, newRect = rot_center(self.image, self.rect, self.angle)
		screen.blit(newImage, newRect)
