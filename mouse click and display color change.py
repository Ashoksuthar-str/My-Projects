import pygame

win = pygame.display.set_mode((100,100))
clock = pygame.time.Clock()
run = True
while run:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	mouse_pos = pygame.mouse.get_pos()
	left_cpick = pygame.mouse.get_pressed()[0]
	if left_cpick:
		win.fill((100,100,255))
	else:
		win.fill((255,100,100))
	pygame.display.update()