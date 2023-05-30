class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
    
    @property #getter
    def username(self):
        return self._username   #return the username property
    @username.setter #setter property
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16: #if the username is string and length is between 2 and 16 inclusive 
            self._username = username   #username property = username param 
        else:
            raise Exception("Usernames must be strings between 2 and 16 characters, inclusive.")
       
######Object Relationship Attributes and Properties for the Player class######  
#'Player results(self, new_result=None)'####  
    def results(self, new_result=None):
        from classes.result import Result
        #1. import the result class
        if new_result and isinstance(new_result, Result): #2. if new_result exists
            self._results.append(new_result) 
            #3. add new result to instance
        return self._results 
        #returns a list of results associated with that player
        #4. in the Result class, add this method in the init method as 'player.results(self)' aka You will need to call this method in 'Result.__init__()'
    
    def games_played(self, new_game=None):
        from classes.game import Game
        #import the game class
        if new_game and isinstance(new_game, Game): #if the game exists
            self._games_played.append(new_game)
        return self._games_played #return a list of game instance

        #4. add the player.games_played(game) to the Result class init method aka You will need to call this method in Result.__init__().
    



###Aggregate and Association Methods = bonus deliverables###### 
####these are bonus deliverables#####
    def played_game(self, game):
        pass
    
    def num_times_played(self, game):
        pass
    
    @classmethod
    def highest_scored(cls, game):
        pass
        


