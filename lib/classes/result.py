# from player import Player
# from game import Game

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

## for the last Player and Game deliverables, You will need to call this method in Result.__init__().
        player.results(self) 
        player.games_played(game) 
        game.results(self)
        game.players(player) # from the last deliverable

@property #getter
def score(self):
    return self._score

@score.setter #setter 
def score(self, score):
        #Scores must be integers between 1 and 5000, inclusive
        if isinstance(score,int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be between 1 and 5000, inclusive")

########Object Relationship Attributes and Properties######
##### player ##### 'Result property player' ####
@property #getter for the player, Result property player
def player(self):
     return self._player

@player.setter #setter for the player 
def player(self, player):
     from classes.player import Player  #1. import the Player class  
     # #FYI player is inside of the classes folder and the class is called Player, so Player is inside of the classes folder aka from classes.player import Player
     if isinstance(player, Player): #2. Check if the player param is an instance of the Player class (param, Class)
          self._player = player
     else:
          raise Exception("Player must be an instance of the Result Class <3")

##### game ###### 'Result property game' ######
# Result property game
# Returns the game that was played
# Games must be Game instances
# raise Exception if setter fails
@property
def game(self):
     return self._game

#setter
@game.setter
def game(self, game):
     from classes.game import Game
     if isinstance(game, Game):
        self._game = game
     else:
        raise Exception("Game must be an instance!")
     





