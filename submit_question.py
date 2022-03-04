
def submit(question, answers, properties):
	file = open("database.txt", "a")
	file.write(question + "\n")
	file.write(",".join(answers) + "\n")
	file.write(",".join(properties) + "\n")
	file.write("\n")
	file.close()

