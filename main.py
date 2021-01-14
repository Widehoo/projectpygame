import os
import pygame

size = width, height = 710, 400
screen = pygame.display.set_mode(size)
inJump = False
gravity = 10
delta = 10
fps = 30
clock = pygame.time.Clock()

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
hero_image = load_image('chu.png')
hero = pygame.sprite.Sprite(all_sprites)
hero.image = hero_image
hero.rect = hero.image.get_rect()
bg = pygame.image.load('data/bg.jpg')
hero.rect.bottomright = 200, 400
running = True

while running:
    clock.tick(fps)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_a] and hero.rect.left > 0:
            hero.rect.left -= delta
        if keys[pygame.K_d] and hero.rect.right < 707:
            hero.rect.left += delta
        if not inJump:
            if keys[pygame.K_SPACE]:
                inJump = True
        else:
            if gravity >= -10:
                if gravity < 0:
                    hero.rect.top += (gravity ** 2) / 3
                else:
                    hero.rect.top -= (gravity ** 2) / 3
                gravity -= 1
            else:
                inJump = False
                gravity = 10

    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()
