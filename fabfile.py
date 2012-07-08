from fabric.api import local
from quiz_generator import QuizGenerator

def generate(slide_template_file=None):
    verify_file_is_given(slide_template_file)
    QuizGenerator().generate_from_file(slide_template_file)

def save(slide_template_file=None):
    verify_file_is_given(slide_template_file)
    QuizGenerator().save(slide_template_file)

def verify_file_is_given(slide_template_file):
    if slide_template_file is None:
        raise StandardError("Need to specify template file")