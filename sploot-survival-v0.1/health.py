import pygame

class Health:
    def __init__(self, x, y, width, height, max_health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health

    def draw(self, surface, current_health):
        ratio = current_health/self.max_health

        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, "white", rect)
        rect_2 = pygame.Rect(self.x, self.y, self.width * ratio, self.height)
        pygame.draw.rect(surface, "red", rect_2)