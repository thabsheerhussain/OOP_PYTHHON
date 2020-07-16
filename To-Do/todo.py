import datetime

last_id = 0

class todo:
    def __init__(self, todo):
        self.todo = todo
        self.creation_date = datetime.date.today()
        global last_id 
        last_id += 1
        self.id = last_id

class do:
    def __init__(self):
        self.dos[]
    def new_note(self, todo):
        self.dos.append(note(todo))
    