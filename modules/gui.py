import pygame

class Gui:
	def __init__(self):
		self.theFont = pygame.font.SysFont('monospace', 18, True, False)
		self.scoreText = "Score: "
		self.score = 0
		self.score_x = 0
		self.score_y = 0

	def draw(self, display):
		fontSurface = self.theFont.render(self.scoreText + str(self.score), False, (255,255,255))
		display.blit(fontSurface,(self.score_x,self.score_y))