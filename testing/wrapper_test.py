'''Testing main_screen_wrapper.py, which is the functions that main_screen uses'''
from main_screen_wrapper import MainWrapper

wrapper = MainWrapper("../testing/test_data.json")
question_list = []
for data_question in wrapper.database.questions:
    question_list.append(data_question)

def test_get_details_false():
    '''Asserts that a question that doesnt exist doesnt have any details returned'''
    question = "Not in list"
    result = wrapper.get_details(question)
    assert not result #result == []

def test_get_details_true():
    '''Asserts that a question that does exist has proper details returned'''
    question = "What?"
    result = wrapper.get_details(question)
    assert result == ['What?', 'True: Answer 1!\nFalse: incorrect '\
        'answer\nFalse: other incorrect answer\n', 4, 'Multiple Choice']

def test_create_buttons_size():
    '''Asserts that the 2D array of buttons is the right dimensions and non-empty'''
    row_size = 3
    result = wrapper.create_buttons(row_size)
    assert result #result != []
    assert len(result[0]) == 3
    for item in result:
        assert len(item) <= row_size

def test_filtered_buttons_type():
    '''Asserts that the filtering of questions by type works correctly'''
    criteria = ['Short Answer','','','','']
    filtered,clean = wrapper.filtered_buttons(criteria)
    for item in question_list:
        if item in filtered:
            assert item.type == 'Short Answer'
        else:
            assert item.type != 'Short Answer'
        if item in clean:
            assert item.type != 'Short Answer'

def test_filtered_buttons_difficulty():
    '''Asserts that the filtering of questions by difficulty works correctly'''
    criteria = ['','5','','','']
    filtered,clean = wrapper.filtered_buttons(criteria)
    for item in question_list:
        if item in filtered:
            assert item.difficulty == '5'
        else:
            assert item.difficulty != '5'
        if item in clean:
            assert item.difficulty != '5'
