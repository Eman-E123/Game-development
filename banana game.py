import pygame as py
import random
py.init()
screen = py.display.set_mode((800,800))
py.display.set_caption("screen")
running = True 
george = py.image.load("george (2).png")
george = py.transform.scale(george, (150,150))
georgesprite = george.get_rect()
georgesprite.center = (400,400)


banana = py.image.load("banana.png")
banana = py.transform.scale(banana, (80,70))
bananasprite = banana.get_rect()
bananasprite.center = (300,300)
font1 = py.font.SysFont("Arial", 30)
text1 = font1.render("Score: 0", True, "black")
score = 0











while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 
    keys = py.key.get_pressed()
    if keys[py.K_a]:
        georgesprite.x -= 5
    if keys[py.K_d]:
        georgesprite.x += 5
    if keys[py.K_w]:
        georgesprite.y -= 5
    if keys[py.K_s]:
        georgesprite.y += 5
    if georgesprite.colliderect(bananasprite):
        bananasprite.x = random.randint(0, 800)
        bananasprite.y = random.randint(0, 800)
        score += 1
    screen.fill("white")
    screen.blit(george, georgesprite)
    screen.blit(banana, bananasprite)
    text1 = font1.render("Score: "+str(score), True, "black")
    screen.blit(text1, (10, 10))
    py.display.flip()

py.quit()