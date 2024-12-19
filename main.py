import sys
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot
def main():
	pygame.init()
	# sets game clock for fps purposes
	clock = pygame.time.Clock()
	# initial fps value
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()
	Asteroid.containers = (asteroid_group, updatable, drawable)
	Player.containers = (updatable,drawable)
	AsteroidField.containers = (updatable,)
	AsteroidField()
	shots_group = pygame.sprite.Group()
	Shot.containers = (shots_group, updatable, drawable)
	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		# Update all sprites
		for x in updatable:
			x.update(dt)
		
		# check for collisions
		for asteroid in asteroid_group:
			if player.collides(asteroid):
				print("Game Over!")
				sys.exit()

			# collision check for bullet hitting asteroid
			for bullet in shots_group:
				if bullet.collides(asteroid):
					bullet.kill()
					asteroid.split()

		# Draw all sprites
		for x in drawable:
			x.draw(screen)
		pygame.display.flip()
				
		dt = clock.tick(60) / 1000
if __name__ == "__main__":
	main()
