'''Database using JSON files'''
import json

from models.multiple_choice_question import MultipleChoiceQuestion
from models.short_answer_question import ShortAnswerQuestion 
from models.fill_in_question import FillInQuestion

class QuestionDatabaseJSON():
    '''
    Class for json database
    filepath: String path to the file that will be used as a database
    '''
    def __init__(self, filepath):
        self.questions = []
        self.filepath = filepath

        self.fetch_questions()

    def fetch_questions(self):
        '''
        Fetching questions from the JSON file to internal questions variable
        '''
        try:
            with open(self.filepath, 'r') as file:
                json_data = json.load(file)

                for question in json_data:
                    # creating instances of models from objects parsed from json file, then appending them to the variable
                    if type(question).__name__ == "MultipleChoiceQuestion":
                        question = MultipleChoiceQuestion(question.body, question.when_used, question.difficulty, question.answers)
                        self.questions.append(question)
                    elif type(question).__name__ == "ShortAnswerQuestion":
                        question = ShortAnswerQuestion(question.body, question.when_used, question.difficulty, question.answer_properties)
                        self.questions.append(question)
                    elif type(question).__name__ == "FillInQuestion":
                        question = FillInQuestion(question.body, question.when_used, question.difficulty, question.answers)
                        self.questions.append(question)

        except:
            # in case something goes wrong (either file does not exist or it does but with a wrong content), it will be created/overwritten with "[]"
            with open(self.filepath, 'w') as file:
                file.write("[]")

    def submit_question(self, question):
        '''
        Saving questions both in local variable and in JSON file
        question: Instance of one of the question models classes
        '''
        self.questions.append(question)
        # loading previously saved json
        with open(self.filepath, "r") as file:
            json_data = json.load(file)
            print(json_data)

        with open(self.filepath, 'w+') as file:
            # turning question from class to object
            new_json_data = {
                "body": question.body,
                "type": type(question).__name__,
                "first_used": question.first_used,
                "last_used": question.last_used,
                "difficulty": question.difficulty
            }

            # adding model-specific fields
            if type(question).__name__ == "MultipleChoiceQuestion" or type(question).__name__ == "FillInQuestion":
                new_json_data["answers"] = question.answers
            elif type(question).__name__ == "ShortAnswerQuestion":
                new_json_data["answer_properties"] = {"max_word_count": question.max_word_count, "key_points": question.key_points}

            # adding newly created object to the ones previously created and then writting an array of them into the json file
            json_data.append(new_json_data)
            file.write(json.dumps(json_data))
