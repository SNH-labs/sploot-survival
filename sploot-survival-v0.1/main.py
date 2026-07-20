import pygame
from player import Player
from ball import Ball
from enemy import Enemy
from health import Health
import sys

##------------------------------------SETUP-----------------------------------------##
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sploot Survival V0.1")
game_font = pygame.font.Font(None, 20)

char_sprites = pygame.sprite.Group()
weapon_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

shot_cooldown = 300
last_shot_time = 0

spawn_cooldown = 800
last_spawn = 0

player_health = 100
enemy_health = 100

health_bar = Health(10, 30, 200, 20, player_health)


##--------------------------------SURFACES & SPRITES--------------------------------##

back_surface = pygame.Surface((600, 600 ))
back_surface.fill("grey")

bodi = Player(300, 300, player_health)
char_sprites.add(bodi)

health_surface = game_font.render(f"Health: {player_health}", False, "black")

##-------------------------------------Main Loop-------------------------------------##

while True:

    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = pygame.time.get_ticks()
    if current_time - last_spawn >= spawn_cooldown:
        slug = Enemy(enemy_health)
        enemy_sprites.add(slug)
        last_spawn = current_time

    if current_time - last_shot_time >= shot_cooldown:
        ball = Ball(bodi.rect.x + 18, bodi.rect.y, enemy_sprites.sprites())
        weapon_sprites.add(ball)
        last_shot_time = current_time

    hit = pygame.sprite.groupcollide(enemy_sprites, weapon_sprites, False, True)

    for slug, ball in hit.items():
        slug.health -= 50 * len(ball)

    dmg = pygame.sprite.groupcollide(enemy_sprites, char_sprites, False, False)

    if dmg:
        bodi.health -= 1
        health_surface = game_font.render(f"Health: {bodi.health}", False, "black")

    ##--------------------------------Update & Draw---------------------------------##

    screen.blit(back_surface, (0, 0))
    screen.blit(health_surface, (10, 10))

    char_sprites.update(dt)
    weapon_sprites.update()
    enemy_sprites.update(dt, bodi.rect.center)
    char_sprites.draw(screen)
    weapon_sprites.draw(screen)
    enemy_sprites.draw(screen)
    health_bar.draw(screen, bodi.health)
    slug.health_bar.draw(screen, slug.health)

    pygame.display.update()


