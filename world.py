from settings import *
from random import seed, randint
from tile import Tile

# Class Imports go here
seed(randint(1, 999999999999999999))

class World():
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.SysFont('system', 30)
        self.status_dict = {
            'start': 0,
            'play': 1,
            'gameover': 2,
            'setup': 3
        }
        self.lookup_status = {str(value): key for key, value in self.status_dict.items()}
        
        # Creating Game Variables
        self.score = 0
        
        # Create Sprite Groups Here
        # self.player = pygame.sprite.GroupSingle(Player(...))
        self.tiles = pygame.sprite.Group()
        
        # Setting Game Status to Setup
        self.status = self.status_dict['setup']
    
    #Update Function if the Game Status is Start
    def update_start(self):
        is_left_clicked = pygame.mouse.get_pressed()[0]
        # Start Text goes Here
        start_text = self.font.render('Press Space or Click to Start', True, colours['black'])
        start_text_rect = start_text.get_rect()
        self.display.blit(start_text, (W//2-start_text_rect.width//2, H//2-start_text_rect.height//2))
        
        if is_left_clicked or pygame.key.get_pressed()[pygame.K_SPACE]:
            self.status = self.status_dict['play']
    
    #Update Function if the Game Status is Setup
    def update_setup(self):
        # Empty Sprite Groups Here
        self.tiles.empty()
        
        # Reset Variables here
        self.score = 0
        
        # Changing Game Status to Start
        self.status = self.status_dict['start']
    
    #Update Function if the Game Status is Gameover
    def update_gameover(self):
        is_left_clicked = pygame.mouse.get_pressed()[0]
        
        # Play Again Text goes here
        playagain_text = self.font.render('Press Space or Click to Play again', True, colours['black'])
        playagain_text_rect = playagain_text.get_rect()
        
        self.display.blit(playagain_text, (W//2-playagain_text_rect.width//2, H//2-playagain_text_rect.height//2))
        
        
        # Gameover Text goes here
        gameover_text = self.font.render('Gameover.', True, colours['black'])
        gameover_text_rect = gameover_text.get_rect()
        
        self.display.blit(gameover_text, (W//2-gameover_text_rect.width//2, H//2-playagain_text_rect.height//2-(gameover_text_rect.height+3)))
        
        
        # More text goes here (like score)
        score_text = self.font.render(f'Score: {self.score}', True, colours['black'])
        score_text_rect = score_text.get_rect()
        
        self.display.blit(score_text, (W//2-score_text_rect.width//2, H//2+gameover_text_rect.height//2+3))
        
        if is_left_clicked or pygame.key.get_pressed()[pygame.K_SPACE]:
            self.status = self.status_dict['play']
    
    #Update Function if the Game Status is Play
    def update_play(self):
        # Generating a Random Number Here
        seed(randint(1, 999999999999999999))
        n = randint(1, 7)
        
        # More Game Logic to Run every frame
        if pygame.key.get_pressed()[pygame.K_SPACE]: self.tiles.add(Tile((0, 0)))
        
        # Drawing the Sprites to the Display through Sprite groups
        self.tiles.draw(self.display)
        # self.player.draw(self.display)
        
        # Death Condition goes here
        # Ex: if (hit_groud): self.status = self.status_dict['gameover']
    
    def update(self):
        eval(f"self.update_{self.lookup_status[str(self.status)]}()")