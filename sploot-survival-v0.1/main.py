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
game_over_font = pygame.font.Font(None, 50)

char_sprites = pygame.sprite.Group()
weapon_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

shot_cooldown = 200
last_shot_time = 0

spawn_cooldown = 400
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
game_over_surface = game_over_font.render("GAME OVER", False, "red")
sub_go_surface = game_font.render("Press 'space' to reset", False, "red")

##-------------------------------------RESET-------------------------------------##
def reset():
    global bodi
    global player_health
    global health_surface
    player_health = 100
    health_surface = game_font.render(f"Health: {player_health}", False, "black")
    bodi = Player(300, 300, player_health)
    char_sprites.add(bodi)
    slug = Enemy(enemy_health)
    enemy_sprites.add(slug)

##-------------------------------------Main Loop-------------------------------------##
running = True
while True:

    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset()
                running = True

    current_time = pygame.time.get_ticks()
    if current_time - last_spawn >= spawn_cooldown and running:
        slug = Enemy(enemy_health)
        enemy_sprites.add(slug)
        last_spawn = current_time

    if current_time - last_shot_time >= shot_cooldown:
        if len(enemy_sprites) > 0 and running:
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
    for slug in enemy_sprites:
        slug.health_bar.draw(screen, slug.health)

    if len(char_sprites) == 0:
        screen.blit(game_over_surface, (200, 250))
        screen.blit(sub_go_surface, (240, 300))
        char_sprites.empty()
        enemy_sprites.empty()
        weapon_sprites.empty()
        running = False

    pygame.display.update()



