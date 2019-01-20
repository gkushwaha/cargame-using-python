import pygame

def rot_center(image, rect, angle):
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = rot_image.get_rect(center=rect.center)
	return rot_image, rot_rect
