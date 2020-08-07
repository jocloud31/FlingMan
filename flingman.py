import pygame as pg
import random
from sprites import *
from constants import *
from sprites import *

class Game:
	def __init__(self):
		# initialize game window
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((screen_width, screen_height))
		pg.display.set_caption(title)
		self.clock = pg.time.Clock()
		self.running = True

	def new(self):
		# create sprite groups
		self.all_sprites = pg.sprite.Group()
		self.platforms = pg.sprite.Group()
		# create player and add to groups
		self.player = Player(green, 50, 50, self)
		self.all_sprites.add(self.player)
		# generate initial platforms and add to groups
		for plat in platform_list:
			p = Platform(*plat)
			self.all_sprites.add(p)
			self.platforms.add(p)
		self.run()

	def run(self):
		# init game loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		# game loop update
		self.all_sprites.update()

		if self.player.vel.y > 0:
			hits_ground = pg.sprite.spritecollide(self.player, self.platforms, False)
			if hits_ground:
				self.player.pos.y = hits_ground[0].rect.top
				self.player.vel.y = 0
		if self.player.rect.right >= screen_width * 1 / 2 + 200 or self.player.rect.left <= screen_width * 1 / 2 - 200:
			self.player.pos.x += -self.player.vel.x
			for plat in self.platforms:
				plat.rect.x += round(-self.player.vel.x)
				if plat.rect.right < 0:
					plat.kill()

	def events(self):
		# game loop events
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.playing = False
				self.running = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_j:
					self.player.jump()
				if event.key == pg.K_ESCAPE:
					pg.quit()


	def draw(self):
		# game loop draw
		self.screen.fill(black)
		self.all_sprites.draw(self.screen)
		pg.display.flip()

	def show_splash(self):
		pass

	def show_gameover(self):
		pass


g = Game()
g.show_splash()
while g.running:
	g.new()
	g.show_gameover()

pg.quit()