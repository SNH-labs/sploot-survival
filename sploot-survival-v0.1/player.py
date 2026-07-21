import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

        self.frames = ["red", "purple", "blue"]
        self.cur_index = 0
        self.anim_timer = 0
        self.anim_speed = 200

        self.health = health

    def animate(self, dt):
        self.anim_timer += dt
        if self.anim_timer >= self.anim_speed:
            self.anim_timer = 0
            self.cur_index = (self.cur_index + 1) % (len(self.frames))
        self.image.fill(self.frames[self.cur_index])

    def update(self, dt):
        self.animate(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < 550:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed

        if self.health <= 0:
            self.kill()
