import pygame

WHITE = (255,255,255)
COLOR = (200,255,255)
SIZE = (300,300) 
RECT = pygame.draw.rect((20,20))
WIN = pygame.display.set_mode((20,20))
def draw():
	WIN.fill((COLOR))
	pygame.display.update()
def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw()
	pygame.quit()

if __name__ == "__main__":
	main()