import pygame as pg
from random import randint
from time import perf_counter as pf

win = pg.display.set_mode((1000,1000))
# vertices = ((500, 200), (211, 700), (788, 700))
vertices = ((250,250),(250,750),(750,750),(750,250))
def draw():
	win.fill((0,0,0))
	pg.draw.polygon(win, (255,255,255), vertices, 2)
	for p in points:
		pg.draw.circle(win, (255,255,255), p, 1)
	pg.display.update()

def new_point(pt, pts):
	global r, pvx
	while r==pvx:
		r = randint(0,len(vertices)-1)
	v = vertices[r]
	pvx = r
	npt = (abs(v[0]+pt[0])//2, abs(v[1]+pt[1])//2)
	pts.append(npt)
	return npt

pvx = 0
r = 0

# checking triangle
for i in range(3):
	print(((vertices[(i+1)%3][0]-vertices[i][0])**2 + (vertices[(i+1)%3][1]-vertices[i][1])**2)**0.5)

point = (500, 400) # any random point
points = [point]

count = 0

while 1:
	t = pf()
	for e in pg.event.get():
		if e.type==pg.QUIT:
			exit()
	if count>1e5:		# increase this value for a faster result
		draw()
		print(f"FPS: {round(1/(pf()-t))}")
	count += 1
	point = new_point(point, points)
