'''Parent model for questions'''

class Question():
    '''
    Parent class for questions
    body: Text of a question
    when_used: Object of two elements - first_used, last_used, both are strings epoch time
    difficulty: Integer from 0 to 5
    '''
    def __init__(self, body, when_used, difficulty):
        self.body = body
        self.first_used = when_used["first_used"]
        self.last_used = when_used["last_used"]
        self.difficulty = difficulty

    def set_body(self, body):
        '''Change body of a question'''
        self.body = body

    def print(self):
        '''Print question to the terminal (for non-GUI version)'''
        if self.first_used:
            print(f'First used: {self.first_used.strftime("%m/%d/%Y, %H:%M:%S")}')
        if self.last_used:
            print(f'Last used: {self.last_used.strftime("%m/%d/%Y, %H:%M:%S")}')

        print(f'Difficulty: {self.difficulty}')
        print(self.body)
        # the rest will be printed by specific models
