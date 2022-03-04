'''Parent model for questions'''
from abc import ABC, abstractmethod

class Question(ABC):
    '''Parent class for questions'''
    def __init__(self, body, when_used, difficulty):
        self.body = body
        self.first_used = when_used["first_used"]
        self.last_used = when_used["last_used"]
        self.difficulty = difficulty 
    @abstractmethod
    def print(self):
        '''Print question to the terminal'''
        pass
