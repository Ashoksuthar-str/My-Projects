import pygame
import math
WIDTH,HEIGHT = 600,800
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
n = 0
r=0
wheelvalue = 0
w = 180
def main():
	clock.tick(24)
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		WIN.fill((150,255,255))
		global n,w,wheelvalue,r
		n += 2
		w += 2
		r += 2
		y = math.sin(math.radians(n))
		h = math.cos(math.radians(n))
		k = math.sin(math.radians(w))
		boxsincos = pygame.Rect((h*20)+100,(y*20)+100,50,50)
		pygame.draw.rect(WIN,(0,0,0),boxsincos)
		box2sinx = pygame.Rect((y*20)+500,300,50,50)
		pygame.draw.rect(WIN,(0,0,0),box2sinx)
		box3siny = pygame.Rect(500,(y*20)+100,50,50)
		pygame.draw.rect(WIN,(0,0,0),box3siny)
		boxcosx = pygame.Rect((h*20)+700,100,50,50)
		pygame.draw.rect(WIN,(0,0,0),boxcosx)
		boxcosy = pygame.Rect(900,(h*20)+100,50,50)
		pygame.draw.rect(WIN,(0,0,0),boxcosy)
		boxsinsin = pygame.Rect((y*20)+100,(y*20)+300,50,50)
		pygame.draw.rect(WIN,(0,0,0),boxsinsin)
		boxsinsin1 = pygame.Rect((y*20)+300,(k*20)+300,50,50)
		pygame.draw.rect(WIN,(0,0,0),boxsinsin1)
		boxsincos = pygame.Rect((y*20)+300,(h*20)+100,50,50)
		pygame.draw.rect(WIN,(0,0,0),boxsincos)
		wheelvalue += 1
		sinwheel = math.sin(math.radians(wheelvalue))
		coswheel = math.cos(math.radians(wheelvalue))
		pygame.draw.circle(WIN,(0,0,0),(sinwheel*50+800,coswheel*50+300),25)
	
		pygame.display.update()
				
	pygame.quit()
	
if __name__=='__main__':
	main()