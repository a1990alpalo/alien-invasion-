#from pathlib import Path
import json 

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats():

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings 
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        self.path = self.settings.scores_file
        self.path.parent.mkdir(parents=True, exist_ok=True)

        try:
            contents = self.path.read_text(encoding="utf-8")
            scores = json.loads(contents)
            self.hi_score = scores.get("hi_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        scores = {
            "hi_score": self.hi_score
        }
        contents = json.dumps(scores, indent= 4)

        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(contents, encoding="utf-8")
        
    def reset_stats(self):    
        self.ships_left = self.settings.starting_ship_count 
        self.score = 0
        self.level = 1


    def update(self, collisions):
        #update score 
        self._update_score (collisions)
        # update max score
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')

    def _update_hi_score(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
        #print(f'Max: {self.max_score}')   
         
    
    
    def _update_score (self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Basic: {self.score}')
        
    def update_level(self):
        self.level += 1


        
    
