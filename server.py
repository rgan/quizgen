import tornado.ioloop
import tornado.web
import os

from slide_handler import SlideHandler

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r"/slides/(?P<slide>[\w+]*)", SlideHandler),
        ]

        settings = { "static_path" : os.path.join(os.path.dirname(__file__), "public")}
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    app = Application()
    app.listen(8000)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
