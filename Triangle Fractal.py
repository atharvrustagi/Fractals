import pygame as pg
from random import randint
# from time import perf_counter as pf

win = pg.display.set_mode((1000,1000))
win.fill((0,0,0))
vertices = ((500, 200), (211, 700), (788, 700))

def draw(cnt):
	# win.fill((0,0,0))
	pg.draw.polygon(win, (255,255,255), vertices, 2)
	pg.draw.circle(win, (255,255,255), point, 1)
	if cnt>fwd and count%speed==0:
		pg.display.update()

def new_point(pt):
	v = vertices[randint(0,len(vertices)-1)]
	npt = (abs(v[0]+pt[0])//2, abs(v[1]+pt[1])//2)
	# pts.append(npt)
	return npt
	

# checking triangle
# for i in range(3):
# 	print(((vertices[(i+1)%3][0]-vertices[i][0])**2 + (vertices[(i+1)%3][1]-vertices[i][1])**2)**0.5)

point = (500, 700) # any random point
points = [point]

count = 0
speed = 10		# increase this for a faster result
fwd = 1e0		# increase to fast forward

while 1:
	for e in pg.event.get():
		if e.type==pg.QUIT:
			exit()
	draw(count)
	count += 1
	point = new_point(point)
