import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space ship shooter")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)

FPS = 60
VEL = 5
BULLET_VEL = 9
MAX_BULLETS = 10

P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2

PLAYER_ONE = pygame.image.load(os.path.join("assets", "adibas.jpg"))
PLAYER_ONE = pygame.transform.rotate(pygame.transform.scale(PLAYER_ONE, (70, 70)), 0)

PLAYER_TWO = pygame.image.load(os.path.join("assets", "opachki.jpg"))
PLAYER_TWO = pygame.transform.rotate(pygame.transform.scale(PLAYER_TWO, (70, 70)), 0)

BACKGROUND = pygame.image.load(os.path.join("assets", "chikiBriki.jpg"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

def draw_window(player_one, player_two, p1_bullets, p2_bullets, p1_health, p2_health):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    p1_health_text = HEALTH_FONT.render("HEALTH: " + str(p1_health), 1, RED)
    p2_health_text = HEALTH_FONT.render("HEALTH: " + str(p2_health), 1, RED)

    WIN.blit(p2_health_text, (WIDTH - p1_health_text.get_width() - 10, 10))
    WIN.blit(p1_health_text, (10, 10))


    WIN.blit(PLAYER_ONE, (player_one.x, player_one.y))
    WIN.blit(PLAYER_TWO, (player_two.x, player_two.y))

    for bullet in p1_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in p2_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()

def player_one_move(player_one, keys_pressed):
    if keys_pressed[pygame.K_a] and player_one.x - VEL > 0:
        player_one.x -= VEL
    
    if keys_pressed[pygame.K_d] and player_one.x + VEL + 70 < BORDER.x:
        player_one.x += VEL

    if keys_pressed[pygame.K_w] and player_one.y - VEL > 0:
        player_one.y -= VEL

    if keys_pressed[pygame.K_s] and player_one.y + VEL + 70 < HEIGHT:
        player_one.y += VEL

def player_two_move(player_two, keys_pressed):
    if keys_pressed[pygame.K_LEFT] and player_two.x - VEL > BORDER.x + BORDER.width:
        player_two.x -= VEL
    
    if keys_pressed[pygame.K_RIGHT] and player_two.x + VEL + 70 < WIDTH:
        player_two.x += VEL

    if keys_pressed[pygame.K_UP] and player_two.y - VEL > 0:
        player_two.y -= VEL

    if keys_pressed[pygame.K_DOWN] and player_two.y + VEL + 70 < HEIGHT:
        player_two.y += VEL

def handle_bullets(p1_bullets, p2_bullets, player_one, player_two):
    for bullet in p1_bullets:
        bullet.x += BULLET_VEL

        if player_two.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p1_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            p1_bullets.remove(bullet)

    for bullet in p2_bullets:
        bullet.x -= BULLET_VEL

        if player_one.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p2_bullets.remove(bullet)
        
        elif bullet.x < 0:
            p2_bullets.remove(bullet)

def draw_winner(text):
    draw_text = HEALTH_FONT.render(text, 1, RED)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    player_one = pygame.Rect(100, 300, 70, 70)
    player_two = pygame.Rect(700, 300 ,70, 70)

    clock = pygame.time.Clock()
    run = True

    p1_bullets = []
    p2_bullets = []

    p1_health = 10
    p2_health = 10

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(p1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player_one.x + player_one.width, player_one.y + player_one.height//2 - 2, 10, 5)
                    p1_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(p2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player_two.x, player_two.y + player_two.height//2 - 2, 10, 5)
                    p2_bullets.append(bullet)

            if event.type == P2_HIT:
                p2_health -= 1

            if event.type == P1_HIT:
                p1_health -= 1


        winner_text = ""

        if p2_health <= 0:
            winner_text = "LADA WIN"

        if p1_health <= 0:
            winner_text = "GOPNIK WIN"

        if winner_text != "":
            draw_winner(winner_text)
            break
        
        keys_pressed = pygame.key.get_pressed()
        player_one_move(player_one, keys_pressed)
        player_two_move(player_two, keys_pressed)

        handle_bullets(p1_bullets, p2_bullets, player_one, player_two)

        draw_window(player_one, player_two, p1_bullets, p2_bullets, p1_health, p2_health)

    pygame.quit()


if __name__ == "__main__":
    main()