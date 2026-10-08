import pygame as py

screen = py.display.set_mode((800,800))
pg1 = py.image.load("flappy bird b.jpeg")
py.init()
screen = py.display.set_mode((800, 800))
py.display.set_caption("Flappy Bird")
background = py.image.load("flappy bird b.jpeg").convert()
background = py.transform.scale(background, (800, 800))
running = True


flappy_bird = py.image.load("bird-removebg-preview.png").convert_alpha()
flappy_bird = py.transform.scale(flappy_bird, (100, 100))
flappy_bird_sprite = flappy_bird.get_rect()
by = 400
flappy_bird_sprite.center = (50, by)


pipe1 = py.image.load("pipe-removebg-preview (1).png").convert_alpha()
pipe_inverted2 = py.image.load("pipe-removebg-preview (1).png").convert_alpha()
pipe1 = py.transform.scale(pipe1, (150, 500))
pipe_inverted2 = py.transform.scale(pipe_inverted2, (150, 500))
pipe_inverted2 = py.transform.rotate(pipe_inverted2, 180)
pipe_sprite1 = pipe1.get_rect()
pipe_sprite1.center = (250, 750)
pipe_sprite2 = pipe_inverted2.get_rect()
pipe_sprite2.center = (250, 50)

pipe3 = py.image.load("pipe-removebg-preview (1).png").convert_alpha()
pipe_inverted4 = py.image.load("pipe-removebg-preview (1).png").convert_alpha()
pipe3 = py.transform.scale(pipe3, (150, 500))
pipe_inverted4 = py.transform.scale(pipe_inverted4, (150, 500))
pipe_inverted4 = py.transform.rotate(pipe_inverted4, 180)
pipe_sprite3 = pipe3.get_rect()
pipe_sprite3.center = (600, 850)
pipe_sprite4 = pipe_inverted4.get_rect()
pipe_sprite4.center = (600, 200)

gravity = 0.7
velocity = 1

font1 = py.font.SysFont("Arial", 30)
text1 = font1.render("Score: 0", True, "black")
score = 0
text1 = font1.render("Score: "+str(score), True, "black")

while running:
    by = by + gravity
    pipe_sprite1.x = pipe_sprite1.x - velocity
    pipe_sprite2.x = pipe_sprite2.x - velocity
    pipe_sprite3.x = pipe_sprite3.x - velocity
    pipe_sprite4.x = pipe_sprite4.x - velocity
    if pipe_sprite1.x < -150:
        pipe_sprite1.x = 800
    if pipe_sprite2.x < -150:
        pipe_sprite2.x = 800
    if pipe_sprite3.x < -150:
        pipe_sprite3.x = 800
    if pipe_sprite4.x < -150:
        pipe_sprite4.x = 800

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    keys = py.key.get_pressed()
    if keys[py.K_SPACE]:
        by = by - 5

    screen.blit(background, (0, 0))
    screen.blit(flappy_bird, flappy_bird_sprite)
    flappy_bird_sprite.center = (50, by)
    screen.blit(pipe1, pipe_sprite1)
    screen.blit(pipe_inverted2, pipe_sprite2)
    screen.blit(pipe3, pipe_sprite3)
    screen.blit(pipe_inverted4, pipe_sprite4)
    screen.blit(text1, (10, 10))
    py.display.flip()
    


py.quit()
