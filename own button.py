import pygame
pygame.font.init()


win = pygame.display.set_mode((2200,2200))
box = pygame.Rect(50,500,500,150)
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		win.fill((255,255,255))
		x,y = pygame.mouse.get_pos()
		pygame.draw.rect(win,(100,100,100),box)
		button = pygame.mouse.get_pressed()[0]
		if button and 500 < y < 650 and 50 < x < 550:
			pygame.draw.rect(win,(255,100,100),(50,500,500,150))
			
		pygame.display.update()
		