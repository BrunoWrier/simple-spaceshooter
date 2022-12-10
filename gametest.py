import pygame
from random import randint
from bulletclass import Bullet
from playerclass import Player
from enemyclass import Enemy
# import starsanimated

# starting pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('calibri', 30)
 
# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# screen etc
screen_WIDTH = 800
screen_HEIGHT = 600

dis = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
pygame.display.set_caption('Space game by BrunoWrier')
 
# variables
game_over = False
global score
score = 0
timer_shoot = 0

text_surface = my_font.render('Score: ' + str(score), False, (255, 255, 255))
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0

speed = 8

# player and bullets list
player = Player(x1, y1, speed, white)
bullets = []

enemies = []
global timer
timer = 0
global enemyPassed
enemyPassed = 0

 
# clock and redraw function
clock = pygame.time.Clock()
def update(object, have_wallcolision: bool, have_bulletcolision: bool, list=None):
    object.update()
    if have_wallcolision:
        window_rect = pygame.Rect(0, 0, screen_WIDTH, screen_HEIGHT)
        if not window_rect.collidepoint((object.x, object.y)):
            list.pop(list.index(object))
            if list == enemies:
                global enemyPassed
                enemyPassed += 1

    # bullet colision and score points
    if have_bulletcolision:
        for bullet in bullets:
            for rect in object.rects:
                enemy_rect = rect
                if enemy_rect.collidepoint((bullet.x, bullet.y)):
                    try:
                        list.pop(list.index(object))
                    except:
                        print('Enemy not found in list')
                        return
                    global score
                    score = score + 1
                    
    

def redraw():

    for enemy in enemies:
        enemy.draw(dis)
    if enemyPassed < 6:
        for bullet in bullets:
            bullet.draw(dis)
        player.draw(dis)

    pygame.display.update()
 
def spawnEnemy(list):
    enemy_x = 0
    enemy_y = 0
    timer_point = 50

    global score
    global timer
    
    if score > 10 and score < 40:
        timer_point = 20
    elif score > 40:
        timer_point = 10

    

    if timer >= timer_point:
        enemy_x = randint(10, 790)
        list.append(Enemy(enemy_x, 10))
        timer = 0
    elif timer < 50:
        timer = timer + 1


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # shoot
        if event.type == pygame.KEYDOWN and enemyPassed < 6:
            if event.key == pygame.K_SPACE and timer_shoot >= 12:
                bullets.append(Bullet(player.x1+5, player.y1, 4, red))
                timer_shoot = 0  
    
    # update bullets
    for bullet in bullets[:]:
        update(bullet, True, False, bullets)

    # update enemies
    for enemy in enemies[:]:
        update(enemy, True, True, enemies)

    # stars
    # starsanimated.stars(dis)
    
    timer_shoot += 1
    spawnEnemy(enemies)
    if enemyPassed < 6:
        player.controls()
    dis.fill(black)
    
    text_surface = my_font.render('Score: ' + str(score), False, (255, 255, 255))
    dis.blit(text_surface, (0,0))
    redraw()

    clock.tick_busy_loop(20)
 
 
pygame.quit()
quit()