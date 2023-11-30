import pygame
import math

WHITE = (255,255,255)
dark_white = (100,100,100)
COLOR = (200,255,255)
SIZE = (300,300) 
WIN = pygame.display.set_mode((20,20))
x = 1
y = 1
a = 1
b = 1
x1 = math.sin(math.radians(x))
y1 = math.sin(math.radians(y))
x2 = math.sin(math.radians(a))
y2 = math.sin(math.radians(b))

def main():
	global x,y,a,b
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		x += 6
		y += 6
		a += 7
		b += 7
		
		
		WIN.fill(dark_white)
		pygame.draw.rect(WIN,WHITE,x1,y1,10,10)
		pygame.display.update()
	pygame.quit()

if __name__ == "__main__":
	main()