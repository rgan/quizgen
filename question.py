class Question(object):
    CURRENT_ID = 1

    @classmethod
    def id(cls):
        return_value = cls.CURRENT_ID
        cls.CURRENT_ID+=1
        return return_value

    @classmethod
    def single_line_answer(cls, question_text):
        id = cls.id()
        return '''\
            <div id="%s">
                %s <input type="text" id=%s></input>
            </div>
        ''' % (id, question_text, id)

    @classmethod
    def multi_line_answer(cls, question_text):
        id = cls.id()
        return '''\
            <div id="%s">
                %s <textarea rows=10 cols=30 id=%s></textarea>
            </div>
        ''' % (id, question_text, id)

    @classmethod
    def single_choice(cls, question_text, *choices):
        id = cls.id()
        choice_html = ''
        for choice in choices:
            choice_html += '<input type=radio name="%s">%s</input>' % (id, choice)
        return '''\
            <div id="%s">
                %s %s
            </div>
        ''' % (id, question_text, choice_html)

    @classmethod
    def multi_choice(cls, question_text, *choices):
        id = cls.id()
        choice_html = ''
        answer_id=0
        for choice in choices:
            answer_id += 1
            choice_html += '<input type=checkbox id="%s">%s</input>' % (str(id) + "_" + str(answer_id), choice)
        return '''\
            <div id="%s">
                %s %s
            </div>
        ''' % (id, question_text, choice_html)