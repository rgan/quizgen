from HTMLParser import HTMLParser

class HTMLReader(HTMLParser,object):

    def __init__(self, html, skip_tags=[]):
        super(HTMLReader, self).__init__()
        self.result = []
        self.skip_tags = skip_tags
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            self.append("<%s>" % tag)

    def handle_endtag(self, tag):
        if tag not in self.skip_tags:
            self.append("</%s>" % tag)

    def handle_data(self, data):
        self.append(data)

    def append(self, snippet):
        if self.result is None:
            self.result = []
        self.result.append(snippet)

    def to_s(self):
        return "".join(self.result)
