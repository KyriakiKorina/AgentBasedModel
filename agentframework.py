import random

class Agent():
    

    def __init__(self, environment,agents, x = None, y = None):
        self.environment = environment
        self.w = len(environment[0])
        self.h = len(environment)
        if (x == None):
            self.x = random.randint(0,self.w - 1)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,self.h - 1)
        else:
            self.y = y
        self.agents = agents 
        self.store = 0

    '''Move and eat method : behavioural method for our agents  '''
        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % self.w
        else:
            self.x = (self.x - 1) % self.w
        
        
        if random.random() < 0.5:
        
           self.y = (self.y + 1) % self.h
        else:
            self.y = (self.y - 1) % self.h

    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    ''' distance between agents '''
    
    def distance_between(self, agent):
        return(((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5        
        
    ''' agents search in the list of other agents and if they find any within 
    a neighbourhood of themselves, they adjust their variables and their neighbours variables, 
    in order to communicate with the other agents'''
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent) 
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = sum /2
                self.store = average
                agent.store = average
                #print("distance = " + str(distance))
                