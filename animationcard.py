import pygame as py
import time
py.init()
py.mixer.init()
screen = py.display.set_mode((800,800))
py.display.set_caption("birthday card animation")
running = True 
pg1 = py.image.load("images (1).jpeg")
pg2 = py.image.load("images (2).jpeg")
pg3 = py.image.load("images (3).jpeg")
pg4 = py.image.load("images (4).jpeg")
pg5 = py.image.load("images (5).jpeg")
pg1 = py.transform.scale(pg1, (800,800))
pg2 = py.transform.scale(pg2, (800,800))
pg3 = py.transform.scale(pg3, (800,800))
pg4 = py.transform.scale(pg4, (800,800))
pg5 = py.transform.scale(pg5, (800,800))
bday_song = py.mixer.music.load("echoes_of_lumen-happy-birthday-song-596310.mp3")
py.mixer.music.play()
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.mixer.music.stop()
            running = False 

    screen.fill("white")
    font1 = py.font.SysFont("Arial", 50)
    text1 = font1.render("Hope you have a great birthday!", True, "black")

    screen.blit(pg1, (0, 0))
    screen.blit(text1, (300, 200))
    py.display.flip()
    time.sleep(2)
    screen.blit(pg2, (0, 0))
    font1 = py.font.SysFont("Arial", 30)
    text1 = font1.render("Hope you have a great day!", True, "black")
    screen.blit(text1, (300, 200))
    font1 = py.font.SysFont("Arial", 30)
    text1 = font1.render("Wishing you all the best!", True, "black")
    py.display.flip()
    time.sleep(2)
    screen.blit(pg3, (0, 0))
    font1 = py.font.SysFont("Arial", 30)
    text1 = font1.render("Enjoy your special day!", True, "black")
    screen.blit(text1, (300, 200))
    py.display.flip()
    time.sleep(2)
    screen.blit(pg4, (0, 0))
    font1 = py.font.SysFont("Arial", 30)
    text1 = font1.render("Have a wonderful birthday!", True, "black")
    screen.blit(text1, (300, 200))
    py.display.flip()
    time.sleep(2)
    screen.blit(pg5, (0, 0))
    font1 = py.font.SysFont("Arial", 30)
    text1 = font1.render("Thank you for being such a great friend!", True, "black")
    screen.blit(text1, (300, 200))
    py.display.flip()
    time.sleep(2)




















py.quit()