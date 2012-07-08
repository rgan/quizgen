import os
import unittest
from quiz_generator import QuizGenerator

class QuizGeneratorTest(unittest.TestCase):

    def test_should_generate_output_file(self):
        generated_file_name="generated/slide1.html"
        if os.path.exists(generated_file_name):
            os.remove(generated_file_name)
        QuizGenerator().generate_from_file("slide1.tmpl")
        self.assertTrue(os.path.exists(generated_file_name))