import os
import tornado
from Cheetah.Template import Template
from quiz_generator import QuizGenerator

class SlideHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.quiz_generator = QuizGenerator()

    def get(self, slide):
        slide_contents = self.find(slide)
        self.write(self.quiz_generator.generate(slide_contents))

    def find(self, slide):
        fpath = os.path.join(os.path.dirname(__file__), ("data/%s.tmpl" % slide))
        print fpath
        if not os.path.exists(fpath):
            raise tornado.web.HTTPError(404)
        with open(fpath) as f:
            return f.read()
