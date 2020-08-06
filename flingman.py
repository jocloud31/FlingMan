import pygame
from pygame.locals import *
import random
import math

pygame.init()


screen_height = 720
screen_width = 1280
white = [255, 255, 255]


screen = pygame.display.set_mode((screen_width, screen_height))

boopSound = pygame.mixer.Sound("boop.wav")

playerImg = pygame.image.load("man.png")
playerX = 0
playerY = screen_height - 101
playerX_change = 0

groundImg = pygame.image.load("ground.png")
groundX = screen_width - 101
groundY = screen_height - 101


def player(x, y):
	screen.blit(playerImg, (x, y))


def ground(x, y):
	screen.blit(groundImg, (x, y))


def is_collision(player_x, player_y, ground_x, ground_y):
	distance = math.sqrt(math.pow(player_x - ground_x, 2) + (math.pow(player_y - ground_y, 2)))
	if distance < 100:
		return True
	else:
		return False


running = True
while running:
	screen.fill(white)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -1
			if event.key == pygame.K_RIGHT:
				playerX_change = 1
		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0
				
	playerX += playerX_change
	if playerX <= 0:
		playerX = 0
	elif playerX >= screen_width - 100:
		playerX = screen_width - 100
		
	collision = is_collision(playerX, playerY, groundX, groundY,)
	if collision:
		playerX_change = 0
		playerX = groundX - 100
		pygame.mixer.Sound.play(boopSound)
	
	ground(groundX, groundY)
	player(playerX, playerY)
	pygame.display.update()
