from main_screen_wrapper import MainWrapper

wrapper = MainWrapper("test_data.json")
question_list = []
for item in wrapper.database.questions:
    question_list.append(item)

def test_get_details_false():
    question = "Not in list"
    result = wrapper.get_details(question)
    assert result == []

def test_get_details_true():
    question = "What?"
    result = wrapper.get_details(question)
    assert result == ['What?', 'True: Answer 1!\nFalse: incorrect '\
        'answer\nFalse: other incorrect answer\n', 4, 'Multiple Choice']

def test_create_buttons_size():
    row_size = 3
    result = wrapper.create_buttons(row_size)
    assert result != []
    assert len(result[0]) == 3
    for item in result:
        assert len(item) <= row_size

def test_filtered_buttons_type():
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
    criteria = ['','5','','','']
    filtered,clean = wrapper.filtered_buttons(criteria)
    for item in question_list:
        if item in filtered:
            assert item.difficulty == '5'
        else:
            assert item.difficulty != '5'
        if item in clean:
            assert item.difficulty != '5'
