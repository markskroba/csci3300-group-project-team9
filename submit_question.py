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
        file.write("QUESTION:" + question + "\n")
        file.write("ANSWERS:" + ",".join(answers) + "\n")
        file.write("PROPERTIES:" + ",".join(properties) + "\n")
        file.write("\n")

submit("question",["answer1","answer2"],["prop1", "prop2"])
