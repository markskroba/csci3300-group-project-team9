from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, body, first_used, last_used,difficulty):
        self.body = body

        self.first_used = first_used
        self.last_used = last_used
        self.difficulty = difficulty 

    @abstractmethod
    def print(self):
        pass