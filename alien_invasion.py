import sys
import pygame
from settings import Settings 

class AlienInvasion: 
    """Manage the game screen and the main loop"""
    
    def __init__(self) -> None:
        """Initiates pygame and create the game window"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bf = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h),
            )
        

        self.running = True
        self.clock = pygame.time.Clock()
    
    def run_game(self)-> None:
        """run the main game loop """
        #Game Loop 
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.bf, (0,0))        
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

        
            



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
