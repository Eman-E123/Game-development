import pygame as py
import random
py.init()
screen = py.display.set_mode((800,800))
py.display.set_caption("screen")
running = True 
character = py.image.load("py_game-removebg-preview (1).png")
character = py.transform.scale(character, (100,100))
charactersprite = character.get_rect()
charactersprite.center = (400,400)


jellyfish = py.image.load("images.jpeg")
jellyfish = py.transform.scale(jellyfish, (70,60))
jellyfishprite = jellyfish.get_rect()
jellyfishprite.center = (300,300)
font1 = py.font.SysFont("Arial", 30)
text1 = font1.render("Score: 0", True, "black")
score = 0











while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 
    keys = py.key.get_pressed()
    if keys[py.K_a]:
        charactersprite.x -= 5
    if keys[py.K_d]:
        charactersprite.x += 5
    if keys[py.K_w]:
        charactersprite.y -= 5
    if keys[py.K_s]:
        charactersprite.y += 5
    if charactersprite.colliderect(jellyfishprite):
        jellyfishprite.x = random.randint(0, 800)
        jellyfishprite.y = random.randint(0, 800)
        score += 1
    screen.fill("white")
    screen.blit(character, charactersprite)
    screen.blit(jellyfish, jellyfishprite)
    text1 = font1.render("Score: "+str(score), True, "black")
    screen.blit(text1, (10, 10))
    py.display.flip()

py.quit()