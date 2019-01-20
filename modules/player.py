import pygame, math
from .objectfunction import rot_center 
from .database import Database

class Player:
	def __init__(self, x, y, width, height, img):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x, y
		self.x, self.y = x,y
		self.screen_width = width
		self.screen_height = height
		self.angle=0
		self.turning=0
		self.turningSpeed = 180
		self.forward = 0
		self.backward = 0
		self.thrust = 50
		self.velocity = 0
	def update(self, dt , score, second):
		self.angle += self.turning * self.turningSpeed *dt
		if(self.forward):
			self.velocity = self.thrust * dt
		elif(self.backward):
			self.velocity = self.thrust * dt
		elif(self.velocity > 0):
			self.velocity -= self.thrust * dt

		if((self.forward and self.velocity) > 0):
			self.x += math.sin(math.radians(self.angle + 180))* self.velocity
			self.y += math.cos(math.radians(self.angle + 180))* self.velocity
			self.rect.x, self.rect.y = self.x, self.y

		if((self.backward and self.velocity) > 0):
			self.x -= math.sin(math.radians(self.angle + 180))* self.velocity
			self.y -= math.cos(math.radians(self.angle + 180))* self.velocity
			self.rect.x, self.rect.y = self.x, self.y

		if(self.rect.x< 0 or self.rect.x>self.screen_width-30 or self.rect.y<0 or self.rect.y>self.screen_height-30):
			pygame.quit()
			self.thedatabase = Database(score, second)
			quit()


	def draw(self, screen):
		newImage, newRect = rot_center(self.image, self.rect, self.angle)
		screen.blit(newImage, newRect)