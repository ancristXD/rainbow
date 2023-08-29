import pygame
import sys
import random

from pygame.constants import QUIT

pygame.init()

x, y = 500, 500

win = pygame.display.set_mode((x, y))

mg = pygame.time.Clock()
iliya = False
chenge = 0
r = 0
g = 0
b = 0
a = 10
s = 10
d = 10
h = 10
while not iliya:
    win.fill((a, s, d))
    mu = pygame.mouse.get_pos()
    cl = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            iliya = True

    def text(x, y, size, text):
        t = pygame.font.SysFont(None, size)
        g = t.render(text, True, (0, 0, 0))
        gg = t.render(text, True, (255, 255, 255))
        win.blit(g, (x, y))
        win.blit(gg, (x-1, y-1))
    pygame.draw.rect(win, (255, 255, 255), [10, 10, 243, 10])
    pygame.draw.circle(win, (255, 255, 255), [12, 15], 5)
    pygame.draw.circle(win, (255, 255, 255), [253, 15], 5)
    pygame.draw.circle(win, (0, 0, 255), [12, 15], 5)
    if 10+243 > mu[0] > 10 and 10+10 > mu[1] > 10:
        pygame.draw.rect(win, (120, 120, 120), [10, 10, 243, 10])
        pygame.draw.circle(win, (120, 120, 120), [12, 15], 5)
        pygame.draw.circle(win, (120, 120, 120), [253, 15], 5)
        if cl[0] == 1:
            a = mu[0]
    pygame.draw.circle(win, (255, 0, 0), [a+2, 15], 10)
    pygame.draw.rect(win, (255, 0, 0), [10, 10, a, 10])
    pygame.draw.circle(win, (255, 0, 0), [12, 15], 5)
    text(270, 8, 30, "vermelho")
    # 2
    pygame.draw.rect(win, (255, 255, 255), [10, 30, 243, 10])
    pygame.draw.circle(win, (0, 0, 255), [12, 35], 5)
    pygame.draw.circle(win, (255, 255, 255), [253, 35], 5)
    if 10+243 > mu[0] > 10 and 30+10 > mu[1] > 30:
        pygame.draw.rect(win, (120, 120, 120), [10, 30, 243, 10])
        pygame.draw.circle(win, (120, 120, 120), [12, 35], 5)
        pygame.draw.circle(win, (120, 120, 120), [253, 35], 5)
        if cl[0] == 1:
            s = mu[0]
    pygame.draw.circle(win, (0, 255, 0), [s+2, 35], 10)
    pygame.draw.rect(win, (0, 255, 0), [10, 30, s, 10])
    pygame.draw.circle(win, (0, 255, 0), [12, 35], 5)
    text(270, 27, 30, "verde")
    # 3
    pygame.draw.rect(win, (255, 255, 255), [10, 50, 243, 10])
    pygame.draw.circle(win, (0, 0, 255), [12, 55], 5)
    pygame.draw.circle(win, (255, 255, 255), [253, 55], 5)
    if 10+243 > mu[0] > 10 and 50+10 > mu[1] > 50:
        pygame.draw.rect(win, (120, 120, 120), [10, 50, 243, 10])
        pygame.draw.circle(win, (120, 120, 120), [12, 55], 5)
        pygame.draw.circle(win, (120, 120, 120), [253, 55], 5)
        if cl[0] == 1:
            d = mu[0]
    pygame.draw.circle(win, (0, 0, 255), [d+2, 55], 10)
    pygame.draw.rect(win, (0, 0, 255), [10, 50, d, 10])
    pygame.draw.circle(win, (0, 0, 255), [12, 55], 5)
    text(270, 48, 30, "azul")
    pygame.display.update()
