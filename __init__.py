from random import randint
from mycroft import MycroftSkill, intent_file_handler


class RandomNumber(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    @intent_file_handler('number.random.intent')
    def handle_number_random(self, message):
        num1 = message.data.get('num1')
        num2 = message.data.get('num2')
        random = randint(num1,num2)
        if num1 is not none:
            if num2 is not none:
                self.speak_dialog('number.random',
                                    {'numsum': random})
    

    def stop(self):
        pass

def create_skill():
    return RandomNumber()

