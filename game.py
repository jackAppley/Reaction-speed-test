# import libraries
import pygame
import random
import os

# initialise pygame
pygame.init()

# game window dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont('Consolas', 30)

active = False
done = False
text = '0'
statusLight = (255, 0, 0)
timer = 0

if os.path.exists('score.txt'):
	with open('score.txt', 'r') as file:
		best = int(file.read())
else:
	best = 0

# create game windows
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

playerHeight = 100
playerWidth = 100

player = pygame.Rect(((SCREEN_WIDTH/2-playerWidth/2), (SCREEN_HEIGHT/2-playerHeight/2), playerWidth, playerHeight))

run = True
while run:

	clock.tick(FPS)

	showBest = 'best: \n' + str(best)

	screen.fill((255,255,255))
	pygame.draw.rect(screen, statusLight, player)

	key = pygame.key.get_pressed()
	if key[pygame.K_SPACE]:
		if active:
			if done != True:
				reactionSpeed = (pygame.time.get_ticks()-start_ticks)
				text = text = str(reactionSpeed).rjust(3)
				done = True
				if best == 0 or reactionSpeed < best:
					best = reactionSpeed
					with open('score.txt', 'w') as file:
						file.write(str(best))
		else: 
			screen.blit(font.render('not yet dumbass', True, (0, 0, 0)), (32, 100))

	if key[pygame.K_r]:
		if active:
			active = False
			timer = 0
			done = False
			text = '0'
		else:
			pass

	if key[pygame.K_ESCAPE]:
		best = 0
		with open('score.txt', 'w') as file:
			file.write(str(best))

	if active: 
		statusLight = (0, 255, 0)
	else:
		statusLight = (255, 0, 0)
		if timer >= 60:
			rand = random.randint(0, 60)
			if rand == 0:
				active = True
				start_ticks = pygame.time.get_ticks()
		else:
			if key[pygame.K_SPACE]:
				timer = 0
			else:
				timer += 1

	screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
	screen.blit(font.render(showBest, True, (0, 0, 0)), (32, 532))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()