from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, player_speed, x, y,width, height):
        super().__init__()
        self.image = transform.scale(image.load(img),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, sprite, player_speed, x, y):
        super().__init__(sprite, player_speed, x, y)
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_z] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_x] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_n] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_m] and self.rect.y < 400:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def __init__(self, sprite, player_speed, x, y):
        super().__init__( sprite, player_speed, x, y)
    def update(self):
        boll




game = True
finish = False
FPS = 60
win = display.set_mode((700, 500))
display.set_caption('PING PONG')
background = transform.scale(image.load('fon.jpg'),(700, 500))
mixer.init()
mixer.music.load('spider_dance.ogg')
mixer.music.play()
clock = time.Clock()
rocet1 = Player('rocet.png',5,0,0,50,100)
rocet2 = Player('rocet.png',5,650,0,50,100)
ball = Enemy('ball.png', 7,250,350,50,50)


while game:
    clock.tick(FPS)
    win.blit(background,(0,0))
    GameSprite.reset(rocet1)
    GameSprite.reset(rocet2)
    GameSprite.reset(ball)
    Player.update_l(rocet1)
    Player.update_r(rocet2)
    display.update()


    for e in event.get():
        if e.type == QUIT:
            game = False
