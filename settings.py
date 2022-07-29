from colours import colours
import pygame

W = 520
H = 520

# Global Data goes here
tile_size = 125
border_width = 10

def tuple_mult(tup, n, a=0):
	return tuple([i*n+a for i in tup])