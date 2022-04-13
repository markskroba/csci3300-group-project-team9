'''testing model classes'''

from datetime import datetime
from models.fill_in_question import FillInQuestion
from models.multiple_choice_question import MultipleChoiceQuestion
from models.short_answer_question import ShortAnswerQuestion

def test_fill_in_basics():
    '''tests that when initiating a fill in the blank question, all properties are set correctly'''
    question = FillInQuestion("This is a ___ question", {"first_used": datetime(2021, 7, 7, 1, 2, 1).strftime('%s'),
                                                         "last_used": datetime(2021, 7, 7, 1, 2, 1).strftime('%s')},
                              1, ["fill in the blank"])
    assert question.body == "This is a ___ question"
    assert question.first_used == "1625637721"
    assert question.last_used == "1625637721"
    assert question.difficulty == 1
    assert question.answers == ["fill in the blank"]

def test_multiple_choice():
    '''tests that when initiating a multiple choice question, all properties are set correctly'''
    question = MultipleChoiceQuestion("Choose the best answer:",
                                      {"first_used": datetime(2021, 7, 7, 1, 2, 1).strftime('%s'),
                                       "last_used": datetime(2021, 7, 7, 1, 2, 1).strftime('%s')}, 3,
                                      ["first option", "second option", "third option"])
    assert question.body == "Choose the best answer:"
    assert question.first_used == "1625637721"
    assert question.last_used == "1625637721"
    assert question.difficulty == 3
    assert question.answers == ["first option", "second option", "third option"]

def test_short_answer():
    '''tests that when initiating a short answer question, all properties are set correctly'''
    question = ShortAnswerQuestion("This is a short answer question", {"first_used": datetime(2021, 7, 7, 1, 2, 1).strftime('%s'),
                                                         "last_used": datetime(2021, 7, 7, 1, 2, 1).strftime('%s')},
                              4, {"max_word_count":350, "key_points": ["point 1", "point 2", "point 3"]})
    assert question.body == "This is a short answer question"
    assert question.first_used == "1625637721"
    assert question.last_used == "1625637721"
    assert question.difficulty == 4
    assert question.max_word_count == 350
    assert question.key_points == ["point 1", "point 2", "point 3"]