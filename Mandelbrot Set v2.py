import numpy as np
import pygame as pg
from time import perf_counter as pf
# from pygame.locals import *

def create(mnx, mxx, mny, mxy, numel):
	a = np.linspace(mnx, mxx, numel)
	b = np.linspace(mny, mxy, numel)
	x, y = np.meshgrid(a, b)
	return x+y*1j


WINSIZE = 1000		# square window
WINSCALE = 1
NUMEL = WINSIZE//WINSCALE

MAXVAL = 20
ITERS = 100

# MINx = 0.283795
# MAXx = 0.283796
# MINy = -0.009767
# MAXy = -0.009766
MINx = -1.5
MAXx = 0.5
MINy = -1
MAXy = 1


print("Calculating the Mandelbrot set values. Please wait\n")

t = pf()
# Making the Mandelbrot set
Z = create(MINx, MAXx, MINy, MAXy, NUMEL)#.flatten()
Zc = 0
N = np.zeros((NUMEL, NUMEL), dtype=np.int16)#.flatten()

i = 0
while (i:=i+1)<ITERS:
	# t1 = pf()
	Zc = Zc**2 + Z
	N = np.where(np.abs(Zc)<MAXVAL, i, N)
	# print(f"Iteration {i+1} took {pf()-t1} seconds.")

N = (N/ITERS*255).transpose().astype(np.uint8)

N = np.tile(N, (3, 1, 1))
N = np.transpose(N, axes=[1,2,0])

# print(N)

print(f"\nDone calculating in {pf()-t} seconds.\n\nRendering the set...")

t = pf()
# displaying the set

img = pg.surfarray.make_surface(N)


def draw():
	win.fill((0, 0, 0))
	win.blit(img, (0, 0))
	pg.display.update()


win = pg.display.set_mode((WINSIZE, WINSIZE))
pg.display.set_caption("Mandelbrot Set")
draw()

print(f"Rendering took {pf()-t} seconds.")

while 1:
	for e in pg.event.get():
		if e.type==pg.QUIT:
			exit()
		elif e.type==pg.MOUSEBUTTONDOWN:
			x, y = pg.mouse.get_pos()
			x = MINx + x*(MAXx-MINx)/WINSIZE
			y = MINy + y*(MAXy-MINy)/WINSIZE
			print(f"X = {x} | Y = {y}")

