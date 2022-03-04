'''
This takes in a question and saves the information to a text file.
Information is seperated by commas and new lines.

Input:
question   - string representation of question
answers    - array of strings representing answers
properties - array of strings representing properties
'''
def submit(question, answers, properties):
    '''Opens a file, appends information, closes the file '''
    with open("database.txt", "a", encoding="utf8") as file:
        file.write(question + "\n")
        file.write(",".join(answers) + "\n")
        file.write(",".join(properties) + "\n")
        file.write("\n")
