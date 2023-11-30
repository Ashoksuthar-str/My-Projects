import pygame
import random
pygame.font.init()

win = pygame.display.set_mode((100,100))

color1 = 255
color2 = 255
color3 = 255
num = 0

x,y = 500,1000

Font = pygame.font.SysFont("Arial" , 555)
count = Font.render("0",10,(50,50,50))
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	mouse_x,mouse_y = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()[0]
	if mouse_press:
		
		color1 = random.randint(0,255)
		color2 = random.randint(0,255)
		color3 = random.randint(0,255)
		x = random.randint(100,600)
		y = random.randint(50,1600)
		
	win.fill((color1,color2,color3))
	win.blit(count,(x,y))
	pygame.display.update()