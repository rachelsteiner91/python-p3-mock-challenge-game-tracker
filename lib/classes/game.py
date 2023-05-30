class Game:
# init method / constructor 
    def __init__(self, title):
        self.title = title #setting the title
        self._results = []
        self._players = []

#1 getter setter OPTION 1 for setting up the title
    def get_title(self):
        return self._title #returning the title property
    
    def set_title(self, title): #setter
            self._title = title #setting up the title property with the inputted title param
    
    title = property(get_title, set_title) #compiling the getter and setter

#1 getter setter OPTION 2 for setting up the title - using the decorator
    @property #1. use property decorator
    def title(self): #2. write the getter function
         return self._title #3. we return the title property
    
    @title.setter
    def title(self, title):  #1. setter then #2. setting up the property 
            #3. if the inputted title is a string
            #4. if the length is greater than 0
            #5. check that it has attribute: if false, the attribute doesn't exist. If true, then the attribute exists
            if isinstance(title,str) and len(title) > 0 and not hasattr(self, 'title'):        
                self._title = title 
            else:
                 raise Exception("Title must be string greater than 0 character. Title cannot be changed after the game is initialized")
         
     
#####Object Relationship Attributes and Properties for the Game class####
##Game results(self, new_result=None)##
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            #1. check if new result exists
            self._results.append(new_result)
            #2. add new results to instance attribute
        return self._results
    #3. return the list of result instance associated with the game instance
    #4. call this in the Result class as well as 'game.result(self)'

##Game players(self, new_player=None)## 
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
            #add the new player to the game.player list
        return self._players
    #You will need to call this method in Result.__init__() as 'game.players(player)'


    
    
###Aggregate and Association Methods = bonus deliverables###### 
####these are bonus deliverables#####
    def average_score(self, player):
        pass

 












