from settings import *

class Tile(pygame.sprite.Sprite):
	# Creating Class Constructor
	def __init__(self, pos, size=(tile_size, tile_size), colour=colours['grey']):
		# Calling the Parent Classe's Constructor
		super().__init__()

		# Creating core Sprite Variables
		self.image = pygame.Surface(size)
		self.rect = self.image.get_rect(topleft=tuple_mult(pos, tile_size, border_width))
		self.image.fill(colours['white'])
		self.colour = colour
		pygame.draw.rect(self.image, self.colour, (0, 0, self.rect.width, self.rect.height), 0, 6)
  
	# Creating a function to run every frame
	def update(self):
		pass