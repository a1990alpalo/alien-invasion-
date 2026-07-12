import sys
import pygame

class AlienInvasion: 
    """Manage the game screen and the main loop"""
    
    def __init__(self):
        """Initiates pygame and create the game window"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.running = True
    
    def run_game(self):
        """run the main game loop """
        #Game Loop 
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running == False
                    pygame.quit()
                    sys.exit()

                    
                    pygame.display.flip()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
