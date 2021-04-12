import pygame as pg
from math import *

win = (1280, 900)
window = pg.display.set_mode(win)
pg.display.set_caption("Fractal Tree")
run = True
clicked = True
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
brown = (120, 75, 0)

def draw():
	window.fill(white)
	tree(150, (win[0]//2, win[1]), pi/2)

def tree(length, pt, ang):
	if length < 15:
		return
	len_scl, ang_ch = 1.2, pi/9
	pt2 = (int(pt[0]-length*cos(ang)), int(pt[1]-length*sin(ang)))
	tree(length//len_scl, pt2, ang-ang_ch)
	tree(length//len_scl, pt2, ang+ang_ch)
	color = green if length<30 else brown
	pg.draw.line(window, color, pt, pt2, 2)
	pg.time.delay(2)
	pg.display.update()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()


window.fill(white)
print("Click anywhere on the window to start again...")

while run:
	for event in pg.event.get():
		if event.type == pg.MOUSEBUTTONDOWN:
			clicked = True
		elif event.type == pg.QUIT:
			exit()
	
	if clicked:
		draw()
		clicked = False
