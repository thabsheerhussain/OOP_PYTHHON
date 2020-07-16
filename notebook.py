import datetime

last_id=0

class note:
    def __init__(self, memo, tags=""):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id 
        last_id += 1
        self.id = last_id
    def match(self, filter):
        return filter in self.memo or filter in self.tags

class notebook:
    def __init__(self):
        self.notes = []
    def new_note(self, memo, tags=''):
        self.notes.append(note(memo, tags))

    def _find_note(self, note_id):
        for notef in self.notes:
            if str(notef.id) == str(note_id):
                return note
            return None
    
    def modify_memo(self, note_id, memo):
        self._find_note(note_id).memo = memo
    def modify_tags(self, note_id, tags):
        self._find_note(note_id).tags = tags
    def search(self, filter):
        return [notef for notef in self.notes if notef.match(filter)]
