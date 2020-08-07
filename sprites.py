# declarations
import pygame as pg
from constants import *
vect = pg.math.Vector2


class Player(pg.sprite.Sprite):

    def __init__(self, color, width, height, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)
        self.pos = vect(screen_width / 2, screen_height / 2)
        self.vel = vect(0, 0)
        self.acc = vect(0, 0)

    def jump(self):
        self.rect.x += platform_tolerance
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= platform_tolerance
        if hits:
            self.vel.y = player_jump_str

    def update(self):
        self.acc = vect(0, player_gravity)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -player_acc
            if keys[pg.K_k]:
                self.acc.x = -player_acc - player_sprint
        if keys[pg.K_d]:
            self.acc.x = player_acc
            if keys[pg.K_k]:
                self.acc.x = player_acc + player_sprint
        self.acc.x += self.vel.x * player_friction

        self.vel += self.acc
        if self.vel.x < player_x_deadzone or self.vel.x > -player_x_deadzone:
            if not keys[pg.K_a] and not keys[pg.K_d]:
                self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image  = pg.Surface((w, h))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y