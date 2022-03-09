'''Database using txt files'''
class QuestionDatabaseTXT():
    '''
    This takes in a question and saves the information to a text file.
    Information is seperated by commas and new lines.
    Input:
    question   - string representation of question
    answers    - array of strings representing answers
    properties - array of strings representing properties
    '''
    def __init__(self, filepath):
        self.filepath = filepath

    def submit(self, question, answers, properties):
        '''Opens a file, appends information, closes the file '''
        with open(self.filepath, "a", encoding="utf8") as file:
            file.write("QUESTION:" + question + "\n")
            file.write("ANSWERS:" + ",".join(answers) + "\n")
            file.write("PROPERTIES:" + ",".join(properties) + "\n")
            file.write("\n")

    def fetch_table(self):
        '''
        This method reads the database file for questions, then prints them out.

        Input : none
        Output: Questions stored in the database printed in order
        '''
        q_header = "QUESTION:"
        with open(self.filepath, "r", encoding="utf8") as file:
            table = []
            for line in file:
                if line.startswith(q_header):
                    table.append(line[len(q_header):].strip())
        for question in table:
            print(question)
