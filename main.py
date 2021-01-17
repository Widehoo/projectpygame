import os
import pygame

pygame.init()
size = width, height = 784, 544
pygame.display.set_caption("Revolver")
screen = pygame.display.set_mode(size)
inJump = False
gravity = 11
delta = 10
fps = 16
Moving_right = False
Moving_left = False
Jump_up = False
Jump_down = False
animation = 0
score = 0
clock = pygame.time.Clock()
walking_on_right = [pygame.image.load("sprites/R_R1.png"), pygame.image.load("sprites/R_R2.png"),
                    pygame.image.load("sprites/R_R3.png"), pygame.image.load("sprites/R_R4.png")]
walking_on_left = [pygame.image.load("sprites/R_L1.png"), pygame.image.load("sprites/R_L2.png"),
                   pygame.image.load("sprites/R_L3.png"), pygame.image.load("sprites/R_L4.png")]
hero_stand = pygame.image.load('sprites/Stand.png')
hero_jump_up = pygame.image.load("sprites/J_UL.png")
hero_jump_down = pygame.image.load("sprites/J_DL.png")
hero_jump_up_right = pygame.image.load("sprites/J_UR.png")
hero_jump_down_right = pygame.image.load("sprites/J_DR.png")

all_sprites = pygame.sprite.Group()
hero = pygame.sprite.Sprite(all_sprites)
hero.image = hero_stand
hero.rect = hero.image.get_rect()
hero.rect.bottomright = 200, 535

ground = pygame.sprite.Sprite(all_sprites)
ground.image = pygame.image.load('data/ground.png')
ground.rect = ground.image.get_rect()
ground.rect.bottomleft = -50, 485
grdelta = 20

wallstart = 2000
wall1 = pygame.sprite.Sprite(all_sprites)
wall1.image = pygame.image.load('data/wall1.png')
wall1.rect = ground.image.get_rect()
wall1.rect.bottomleft = wallstart, 375
wallspeed = 20

pygame.mixer.music.load("music/bg_music.mp3")
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)

i = 1
slower = 0.5


def print_text(message, x, y, color=(198, 207, 207), letter_type="sprites/shrift.ttf", letter_size=30):
    letter_type = pygame.font.Font(letter_type, letter_size)
    text = letter_type.render(message, True, color)
    screen.blit(text, (x, y))


def draw():
    global wallspeed, wallstart
    global animation
    global i
    global slower
    if i + 1 >= 340:
        i = 1
    if 230 < i < 330:
        slower = 1
    else:
        slower = 0.5
    bg = pygame.image.load(f'captures/{int(i // 1)}.png')
    screen.blit(bg, (0, 0))
    i += slower

    if ground.rect.right < 1000:
        ground.rect.left = -50
    screen.blit(ground.image, (ground.rect.left, ground.rect.bottom))
    ground.rect.left -= grdelta

    if wall1.rect.left < -300:
        wall1.rect.left = wallstart
    screen.blit(wall1.image, (wall1.rect.left, wall1.rect.bottom))
    wall1.rect.left -= wallspeed
    wallstart = 750

    if animation + 1 >= 16:
        animation = 0
    if Moving_left and not Jump_up and not Jump_down:
        screen.blit(walking_on_left[animation // 4], (hero.rect.left, hero.rect.top))
        animation += 1
    elif Moving_right and not Jump_up and not Jump_down:
        screen.blit(walking_on_right[animation // 4], (hero.rect.left, hero.rect.top))
        animation += 1
    elif Moving_left and Jump_up and not Jump_down:
        screen.blit(hero_jump_up, (hero.rect.left, hero.rect.top))
    elif Moving_left and not Jump_up and Jump_down:
        screen.blit(hero_jump_down, (hero.rect.left, hero.rect.top))
    elif Moving_right and Jump_up and not Jump_down:
        screen.blit(hero_jump_up_right, (hero.rect.left, hero.rect.top))
    elif Moving_right and not Jump_up and Jump_down:
        screen.blit(hero_jump_down_right, (hero.rect.left, hero.rect.top))
    elif Jump_up:
        screen.blit(hero_jump_up_right, (hero.rect.left, hero.rect.top))
    elif Jump_down:
        screen.blit(hero_jump_down_right, (hero.rect.left, hero.rect.top))
    else:
        screen.blit(walking_on_right[animation // 4], (hero.rect.left, hero.rect.top))
        animation += 1
    print_text("Score:" + str(score), 560, 20)
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
            Moving_left = True
            Moving_right = False
        elif keys[pygame.K_d] and hero.rect.right < 780:
            hero.rect.left += delta
            Moving_left = False
            Moving_right = True
        else:
            Moving_left = False
            Moving_right = False
            animation = 0
        if not inJump:
            if keys[pygame.K_SPACE]:
                inJump = True
                Jump_up = True
    if inJump:
        if gravity >= -11:
            if gravity == -11:
                hero.rect.top += ((gravity + 5) ** 2) / 2
            if gravity < 0:
                hero.rect.top += (gravity ** 2) / 2
                Jump_up = False
                Jump_down = True
            else:
                hero.rect.top -= (gravity ** 2) / 2
            gravity -= 1
        else:
            inJump = False
            gravity = 11
            Jump_up = False
            Jump_down = False

    if hero.rect.bottom > 535:
        hero.rect.bottom = 535
    if hero.rect.right > wall1.rect.left + 75 and hero.rect.right < wall1.rect.left + 175 \
            and hero.rect.bottom > 415:
        pygame.quit()

    draw()
    score += 1
pygame.quit()
