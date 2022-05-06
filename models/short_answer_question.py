'''Model for short answer question'''
from models.question import Question

class ShortAnswerQuestion(Question):
    '''
    Class for short answer question
    answer_properties: Object that consists of
        max_word_count: Int representing maximum word count an answer could have
        key_points: List of strings representing key points that should be addressed in the answer
    '''
    def __init__(self, body, when_used, difficulty, answer_properties):
        super().__init__(body, when_used, difficulty)
        self.max_word_count = answer_properties["max_word_count"]
        self.key_points = answer_properties["key_points"]
        self.type = "Short Answer"

    def set_max_word_count(self, max_word_count):
        '''Change the max word count'''
        self.max_word_count = max_word_count

    def print(self):
        '''Printing question (for non-GUI version)'''
        super().print()
        print("Question type: Short answer")
        print(f'Max word count: {self.max_word_count}')
        print(f'Key points: {", ".join(self.key_points)}')

    def get_formatted_answers(self):
        '''This formats the answers of the question in a way that works well with the main \
            screen'''        
        formatted = ""
        formatted += "Max Word Count: " + str(self.max_word_count) + "\n"
        for point in self.key_points:
            formatted += "Point: " + str(point) + "\n"
        return formatted
