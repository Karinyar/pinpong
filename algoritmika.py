from pygame import *
from random import*

window = display.set_mode((700,500))#создаю окно
display.set_caption('пин понг')#устанавливаю название окна
background=transform.scale(image.load("fon_pr.avif"),(700,500))

clock= time.Clock()
FPS=60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image= transform.scale(image.load(player_image),(50, 50))
        self.speed=player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y     
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update1(self):
        keys=key.get_pressed()
        if keys[K_DOWN] and self.rect.y <450:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
    def update2(self):
        keys=key.get_pressed()
        if keys[K_s] and self.rect.y <450:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed

racetka_r = Player("racetka.jpg", 650, 250, 5)
racetka_l = Player("racetka_2.jpg", 50, 250, 5)
ball = Player("ball.png", randint(150,520),randint(150,300),4)
speed_x= 3
speed_y= 3
finish= False
game=True
while game:
    for e in event.get():
        if e.type == QUIT:
            game= False
    window.blit(background,(0,0))
    racetka_r.update()
    racetka_r.reset()
    racetka_l.update()
    racetka_l.reset()

    
    if finiish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(racetka_r, ball) or sprite.collide_rect(racetka_l, ball):
        speed_x *= -1
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    display.update()
    clock.tick(FPS)