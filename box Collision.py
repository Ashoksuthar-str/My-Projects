import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0))
box = pygame.Rect(0,40,40, 40)
xspeed = 6
yspeed = 6
while True:
    clock.tick(60)
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255,255,255),box)
    box.x += xspeed
    box.y += yspeed
    if box.right >= 1080 or box.left <= 0:
    	xspeed *= -1
    if box.bottom >= 2280 or box.top <= 0:
    	yspeed *= -1
    	
    pygame.display.update()