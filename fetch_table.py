'''
This function reads the database file for questions, then prints them out.

Input : none
Output: Questions stored in the database printed in order
'''
def fetch_table():
    '''Method to fetch table '''
    q_header = "QUESTION:"
    with open("database.txt", "r", encoding="utf8") as file:
        table = []
        for line in file:
            if line.startswith(q_header):
                table.append(line[len(q_header):].strip())
    for question in table:
        print(question)
