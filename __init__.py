from mycroft import MycroftSkill, intent_file_handler


class RandomNumber(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('number.random.intent')
    def handle_number_random(self, message):
        self.speak_dialog('number.random')


def create_skill():
    return RandomNumber()

