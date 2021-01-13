import os
import pygame

size = width, height = 500, 400
screen = pygame.display.set_mode(size)
inJump = False

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as e:
        print('Не удается загрузить картинку:', name)
        raise SystemExit(e)
    image = image.convert_alpha()

    if colorkey:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


all_sprites = pygame.sprite.Group()
creature_image = load_image('chu.png')
creature = pygame.sprite.Sprite(all_sprites)
creature.image = creature_image
creature.rect = creature.image.get_rect()
creature.rect.topleft = 0, 0
delta = 3


running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_s] and creature.rect.bottom < 397:
            creature.rect.top += delta
        if keys[pygame.K_w] and creature.rect.top > 0:
            creature.rect.top -= delta
        if keys[pygame.K_a] and creature.rect.left > 0:
            creature.rect.left -= delta
        if keys[pygame.K_d] and creature.rect.right < 497:
            creature.rect.left += delta
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
