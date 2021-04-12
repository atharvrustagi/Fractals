import pygame as pg
import numpy as np
from time import perf_counter as pf

WINSIZE = 500		# square window
WINSCALE = 1
NUMEL = WINSIZE//WINSCALE
pixels = np.zeros((NUMEL, NUMEL), dtype=np.uint8)		# the pixel grid

ITERS = 100
MINx = 0.23
MAXx = 0.29
MINy = -0.03
MAXy = 0.03

a, b = np.meshgrid(np.linspace(MINx, MAXx, NUMEL), np.linspace(MINy, MAXy, NUMEL))
mnset = a+b*1j
# print(mnset.__abs__())


print("\nIterating and calculating the Mandelbrot set. Please wait.")

def calc(pt):
	n = 0
	z = 0
	while (n<ITERS):
		z = z**2 + pt
		if (z.__abs__() > 100):
			break
		n += 1
	return n

t = pf()
for i in range(NUMEL):
	for j in range(NUMEL):
		n = calc(mnset[i, j])
		pixels[i, j] = int(n/ITERS*255)


# pixels = mnset**2 + mnset
# for i in range(ITERS):
# 	pixels = pixels**2 + mnset
# pixels = pixels.__abs__()
# pixels = np.where(pixels>20, 255, pixels/20*255).astype(np.uint8)
# print(itermnset)


print(f"Took {round(pf()-t, 3)} seconds\n")
print("Plotting the set...")


def draw():
	win.fill((0,0,0))
	for j, y in enumerate(range(0, WINSIZE, WINSCALE)):
		for i, x in enumerate(range(0, WINSIZE, WINSCALE)):
			clr = pixels[j, i]
			pg.draw.rect(win, (clr, clr, clr), (x, y, x+WINSCALE, y+WINSCALE))
	pg.display.update()

t = pf()
win = pg.display.set_mode((WINSIZE, WINSIZE))
draw()
print(f"Done plotting the set. Took {round(pf()-t, 3)} seconds.\n")

while 1:
	for e in pg.event.get():
		if e.type==pg.QUIT:
			exit()
		elif e.type==pg.MOUSEBUTTONDOWN:
			x, y = pg.mouse.get_pos()
			x = MINx + x*(MAXx-MINx)/WINSIZE
			y = MINy + y*(MAXy-MINy)/WINSIZE
			print(f"Mouse position: {(x, y)}")
