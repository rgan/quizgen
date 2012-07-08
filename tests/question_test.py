import unittest
from question import Question
from html_reader import HTMLReader

class QuestionTest(unittest.TestCase):

    def test_should_return_html_for_single_choice_question(self):
        actual = Question.single_choice("question", "a1", "a2")
        expected = '''\
            <div id="1">
                question <input type=radio name="1">a1</input><input type=radio name="1">a2</input>
            </div>
        '''
        self.assertEquals(HTMLReader(expected).to_s(), HTMLReader(actual).to_s())

    def test_should_return_html_for_single_line_answer_question(self):
        actual = Question.single_line_answer("question")
        expected = '''\
            <div id="1">
                question <input type="text" id=1></input>
            </div>
        '''
        self.assertEquals(HTMLReader(expected).to_s(), HTMLReader(actual).to_s())

    def test_should_return_html_for_multi_line_answer_question(self):
        actual = Question.multi_line_answer("question")
        expected = '''\
            <div id="1">
                question <textarea rows=10 cols=30 id=1></textarea>
            </div>
        '''
        self.assertEquals(HTMLReader(expected).to_s(), HTMLReader(actual).to_s())

    def test_should_return_html_for_multi_choice_answer_question(self):
        actual = Question.multi_choice("question", "a1", "a2")
        expected = '''\
            <div id="1">
                question <input type=checkbox id="1_1">a1</input><input type=checkbox name="1_2">a2</input>
            </div>
        '''
        self.assertEquals(HTMLReader(expected).to_s(), HTMLReader(actual).to_s())