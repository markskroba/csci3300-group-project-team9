'''Model for short answer question'''
from models.question import Question

class ShortAnswerQuestion(Question):
    '''
    Class for short answer question
    max_word_count: Int representing maximum word count an answer could have
    key_points: List of strings representing key points that should be addressed in the answer
    '''
    def __init__(self, body, when_used, difficulty, max_word_count, key_points):
        super().__init__(body, when_used, difficulty)
        self.max_word_count = max_word_count
        self.key_points = key_points

    def set_max_word_count(self, max_word_count):
        '''Change the max word count'''
        self.max_word_count = max_word_count

    def print(self):
        '''Printing question (for non-GUI version)'''
        super().print()
        print("Question type: Short answer")
        print(f'Max word count: {self.max_word_count}')
        print(f'Key points: {", ".join(self.key_points)}')
