# Group 9 Sprint 

Our goal is to have a fully fleshed out GUI along with automated testing for models in the backend.

## Steps

1. Figure out a GUI library in Python for our project
2. Main Screen
3. Add Questions
    1. Selection menu for type of questions
    2. Fields for entering question
    3. Fields for entering answers
    4. Fields for entering properties
4. Show Questions
    1. Displays questions
    2. Allows for interactions, such as edit or delete question
    3. Some sort of rudimentary search feature
5. Automated Testing
    1. Set up automated testing using PyTest
    2. Set up seperate directory for tests
    3. Automated tests for controller 


## Install

Run the following commands to install the right library, then run main.

```bash
pip install -r requirements.txt
python3 main.py
```

## Usage

After running main.py, the user will be prompted to add a question, print all questions, or quit.
The questions are stored according to the type of question (i.e. multiple choice, fill in the blank, etc.), and the information is saved in a JSON file managed by question database class.
