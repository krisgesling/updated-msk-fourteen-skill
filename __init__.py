from mycroft import MycroftSkill, intent_file_handler


class UpdatedMskFourteen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fourteen.msk.updated.intent')
    def handle_fourteen_msk_updated(self, message):
        self.speak_dialog('fourteen.msk.updated')


def create_skill():
    return UpdatedMskFourteen()

