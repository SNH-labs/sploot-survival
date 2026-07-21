import pygame
from health import Health
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, health):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rand_top = (random.randint(-50, 650), -50)
        self.rand_left = (-50, random.randint(-50, 650))
        self.rand_bottom = (random.randint(-50, 650), 650)
        self.rand_right = (650, random.randint(-50, 650))
        self.spawn_list = [self.rand_top, self.rand_left, self.rand_bottom, self.rand_right]

        self.rect = self.image.get_rect(center=(random.choice(self.spawn_list)))
        self.speed = 2

        self.frames = ["black", "green", "brown"]
        self.cur_index = 0
        self.anim_timer = 0
        self.anim_speed = 200
        self.health = health
        self.max = health
        self.health_bar = Health(self.rect.x, self.rect.y - 20, 50, 2, self.max)

        self.pos = pygame.math.Vector2(self.rect.center)


    def animate(self, dt):
        self.anim_timer += dt
        if self.anim_timer >= self.anim_speed:
            self.anim_timer = 0
            self.cur_index = (self.cur_index + 1) % (len(self.frames))
        self.image.fill(self.frames[self.cur_index])

    def update(self, dt, target):
        self.animate(dt)

        direction = pygame.math.Vector2(target) - self.pos
        if direction.length() > 0:
            direction = direction.normalize()
            self.pos += direction * self.speed
            self.rect.center = self.pos

        self.health_bar = Health(self.rect.x, self.rect.y -20, 50, 2, self.max)

        if self.health <= 0:
            self.kill()
