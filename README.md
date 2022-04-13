# Group 9 Sprint 

Our goal is to have a fully fleshed out GUI along with automated testing for models in the backend.

## Steps

1. Figure out a GUI library in Python for our project
    1. PySimpleGUI with Tkinter
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

Run the following commands to install the right library, then run main_screen.py.

```bash
pip install -r requirements.txt
# You might need to install tkinter globally depending on the OS you are running
export PYTHONPATH=$(pwd)
python3 main_screen.py
```

NOTE: If you get display errors trying to run the program through hopper, download the files and run it locally.
## Usage

After running main_screen.py, a GUI will appear showing search features, available questions,
and several buttons. The user can click a button to add a question which will open a new screen.
The user can also select options at the top and click search which will filter the viewable questions.
