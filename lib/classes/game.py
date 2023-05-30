class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

#Game property title
# Returns the Game's title
# Titles must be strings greater than 0 characters
# If you are using exceptions, uncomment lines 25-26 and 32-33 in testing/game_test.py.
# raise Exception if setter fails
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if title and isinstance(title, str) and not hasattr(self, 'title'):
            self._title = title
        else:
            raise Exception("Title must be a string greater than 0 characters.")
        
    
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        pass
    
    def average_score(self, player):
        pass

    def get_title(self):
        return self.title


#####
    # class Game:
    # def __init__(self, title):
    #     self.title = title
    #     self._results = []
    #     self._players = []

    # @property
    # def title(self):
    #     return self._title
    
    # @title.setter
    # def title(self, title):
    #     if title and isinstance(title, str) and not hasattr(self, 'title'):
    #         self._title = title
    #     else:
    #         raise Exception
        
    # def results(self, new_result=None):
    #     from classes.result import Result
    #     if new_result and isinstance(new_result, Result):
    #         self._results.append(new_result)
    #     return self._results
    
    # def players(self, new_player=None):
    #     from classes.player import Player
    #     if new_player and isinstance(new_player, Player):
    #         self._players.append(new_player)
    #     return self._players
    
    # def average_score(self, player):
    #     player_scores = [r.score for r in self._results if r.player == player]
    #     if player_scores:
    #         return sum(player_scores) / len(player_scores)
    #     return 0