from Cheetah.Template import Template
import os
from html_reader import HTMLReader
from question import Question

class QuizGenerator(object):

    def generate_from_file(self, slide_input_file):
        with open(slide_input_file) as f:
            slide_contents = f.read()
        with open('generated/%s.html' % os.path.splitext(slide_input_file)[0], 'w+') as f:
            f.write(self.generate(slide_contents))

    def generate(self, slide_contents):
        return str(Template(slide_contents, searchList=[{'Question' : Question}]))

    def save(self, slide_input_file):
        with open(slide_input_file) as f:
            slide_contents = f.read()
        slide_contents = HTMLReader(slide_contents, skip_tags=['html','body']).to_s()
        # TODO: this should be saved in a remote db, for now we just write to data directory
        with open('data/%s' % slide_input_file, 'w+') as f:
            f.write(slide_contents)
