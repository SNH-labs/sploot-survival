import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, enemies):
        super().__init__()
        self.image = pygame.Surface((12, 12))
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.speed = 5

        self.pos = pygame.math.Vector2(self.rect.center)
        self.closest = min(enemies, key=lambda enemy: (pygame.math.Vector2(enemy.rect.center) - self.pos).length_squared())
        self.direction = pygame.math.Vector2(self.closest.rect.center) - self.pos


    def update(self):

        if self.direction.length_squared() > 0:
            direction = self.direction.normalize()
            self.pos += direction * self.speed
            self.rect.center = self.pos

        if self.rect.x < -20 or self.rect.x > 620 or self.rect.y < -20 or self.rect.y > 620:
            self.kill()

