import pygame

win = pygame.display.set_mode((100,100))
clock = pygame.time.Clock()
box1= pygame.Rect(30,50,50,50)
box2 = pygame.Rect(30,1200,50,50)
speedx = 5
speedy = 7
run = True
while run:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	win.fill((255,255,255))
	pygame.draw.rect(win,(0,0,0),(30,30,1020,2220),3)
	pygame.draw.rect(win,(108,200,102),box1)
	box1.x += speedx
	if box1.x >= 1005 or box1.x <= 30:
		speedx *= -1
	
	pygame.draw.rect(win,(8,200,202),box2)
	box2.x += speedy
	if box2.x >= 1000 or box2.x <= 30:
		speedy *= -1
		
	pygame.draw.line(win,(0,0,0),(box1.x+25,box1.y+50),(box2.x+25,box2.y),50)
	pygame.display.update()
	