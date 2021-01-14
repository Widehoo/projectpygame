import os
import pygame

size = width, height = 710, 400
pygame.display.set_caption("Revolver")
screen = pygame.display.set_mode(size)
inJump = False
gravity = 10
delta = 10
fps = 16
Mright = False
Mleft = False
animation = 0
clock = pygame.time.Clock()
walking_on_right = [pygame.image.load("sprites/R_R1.png"), pygame.image.load("sprites/R_R2.png"),
                    pygame.image.load("sprites/R_R3.png"), pygame.image.load("sprites/R_R4.png")]
walking_on_left = [pygame.image.load("sprites/R_L1.png"), pygame.image.load("sprites/R_L2.png"),
                   pygame.image.load("sprites/R_L3.png"), pygame.image.load("sprites/R_L4.png")]
hero_stand = pygame.image.load('sprites/Stand.png')

all_sprites = pygame.sprite.Group()
hero = pygame.sprite.Sprite(all_sprites)
hero.image = hero_stand
hero.rect = hero.image.get_rect()
bg = pygame.image.load('data/bg.jpg')
hero.rect.bottomright = 200, 400


def draw():
    global animation
    screen.blit(bg, (0, 0))
    if animation + 1 >= 16:
        animation = 0
    if Mleft:
        screen.blit(walking_on_left[animation // 4], (hero.rect.left, hero.rect.top))
        animation += 1
    elif Mright:
        screen.blit(walking_on_right[animation // 4], (hero.rect.left, hero.rect.top))
        animation += 1
    else:
        screen.blit(hero_stand, (hero.rect.left, hero.rect.top))
    pygame.display.flip()


running = True

while running:
    clock.tick(fps)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_a] and hero.rect.left > 0:
            hero.rect.left -= delta
            Mleft = True
            Mright = False
        elif keys[pygame.K_d] and hero.rect.right < 707:
            hero.rect.left += delta
            Mleft = False
            Mright = True
        else:
            Mleft = False
            Mright = False
            animation = 0
        if not inJump:
            if keys[pygame.K_SPACE]:
                inJump = True
    if inJump:
        if gravity >= -10:
            if gravity == -10:
                hero.rect.top += ((gravity + 5) ** 2) / 3
            if gravity < 0:
                hero.rect.top += (gravity ** 2) / 3
            else:
                hero.rect.top -= (gravity ** 2) / 3
            gravity -= 1
        else:
            inJump = False
            gravity = 10

    if hero.rect.bottom > 400:
        hero.rect.bottom = 400
    draw()

pygame.quit()
