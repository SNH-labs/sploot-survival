import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sploot Survival V0.1")

back_surface = pygame.Surface((600, 600 ))
back_surface.fill("grey")
player_surface = pygame.Surface((100, 100))
player_rect = player_surface.get_rect()
player_rect.center = (300, 300)
PLAYER_SPEED = 10
FRAMES = ["purple", "red", "blue"]

cur_index = 0
anim_timer = 0
anim_speed = 200

while True:

    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    anim_timer += dt
    if anim_timer >= anim_speed:
        anim_timer = 0
        cur_index = (cur_index + 1) % len(FRAMES)
        print(cur_index)

    player_surface.fill(FRAMES[cur_index])

    screen.blit(back_surface, (0, 0))

    screen.blit(player_surface, player_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player_rect.x < 500:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player_rect.y < 500:
        player_rect.y += PLAYER_SPEED


    pygame.display.update()


