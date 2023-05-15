from pygame import *
import pygame

pygame.init()

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x=0, y=0, w=50, h=50):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, w=50, h=100, speed=5, key_up=K_w, key_down=K_s):
        super().__init__(sprite_image, x, y, w, h)
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def update1(self):
        keys = key.get_pressed()
        if keys[self.key_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.key_down] and self.rect.y < 600:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, w=50, h=50, speed=5):
        super().__init__(sprite_image, x, y, w, h)
        self.dx = speed
        self.dy = speed
        

    def update2(self):
        if self.rect.y < 0 or self.rect.y > height - self.rect.h:
            self.dy *= -1
        self.rect.x += self.dx
        self.rect.y += self.dy
    def player_collide(self, player):
        if sprite.collide_rect(self, player):
            self.dx *= -1
gol1 = 0
gol2 = 0
def status():
    global gol1
    global gol2
    if ball.rect.x <= 0:
        if gol2 > 2:
            ball1.dx -= 1
            ball1.dy -= 1

            ball1.rect.x = 325
            ball1.rect.x = 325
        ball.dx -= 1
        ball.dy -= 1
        ball.rect.x = 325
        ball.rect.x = 325
        gol2 += 1

        
    if ball.rect.x >= 650:
        if gol1 > 2 :
            ball1.dx += 1
            ball1.dy += 1

            ball1.rect.x = 325
            ball1.rect.x = 325
        ball.dx += 1
        ball.dy += 1

        ball.rect.x = 325
        ball.rect.x = 325
        gol1 += 1


        


    if gol2  == 5:
        finish = True
        text_lox = font.render('2 Player win', 2, (0,255,0))
        win.blit(text_lox,(250,250))
    if gol1 == 5:
        finish = True
        text_win = font.render('1 Player win', 2, (0,255,0))
        win.blit(text_win,(250,250))
    

width = 700
height = 700

font = pygame.font.SysFont('Arial', 40)
game = True
finish = False
FPS = 60
win = display.set_mode((700, 700))
display.set_caption('PING PONG')
background = transform.scale(image.load('fon.jpg'),(700, 700))
mixer.init()
mixer.music.load('spider_dance.ogg')
mixer.music.play()
clock = time.Clock()
platform_1 = Player('rocet.png', 10, height/2, 50, 100, 5, K_w, K_s)
platform_2 = Player('rocet.png', 570, height/2, 50, 100, 5, K_UP, K_DOWN)
ball = Ball('ball.png', width/2, height/4, 50,50,3)

while game:
    if finish != True:
        clock.tick(FPS)
        win.blit(background,(0,0))
        GameSprite.reset(platform_1)
        GameSprite.reset(platform_2)
        GameSprite.reset(ball)
        Player.update1(platform_1)
        Player.update1(platform_2)
        Ball.update2(ball)
        status()
        for i in range(1):
            i = gol1
            r = " " + str(i)
            gole1 = r
        for a in range(1):
            a = gol2
            b = " "+ str(a)
            gole2 = b

        if gol1 + gol2 == 3:
            ball1 = Ball('ball.png', width/2, height/4, 50,50,3)
        if gol1 + gol2 >= 3:
            GameSprite.reset(ball1)
            Ball.update2(ball1)
        ball.player_collide(platform_1)
        ball.player_collide(platform_2)
        display.update()
        
        text_chet1 = font.render(gole2, 2, (0,255,0))
        win.blit(text_chet1,(680,20))
        text_chet2 = font.render(gole1, 2, (0,255,0))
        win.blit(text_chet2,(20,20))
    display.update()


    for e in event.get():
        if e.type == QUIT:
            game = False
