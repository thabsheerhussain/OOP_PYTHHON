import sys
from notebook import notebook

class menu:

    def __init__(self):
        self.notebook = notebook()
        self.choice = {

            "1":self.show_notes,
            "2":self.search_note,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit,
        }
    def display(self):
        print(
            """
            Notebook Menu

            "1":self.show_notes,
            "2":self.search_note,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit,
            """
        )
    def run(self):
        while True:
            self.display()
            choice = input("enter the choice")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                """ enter a valide option"""
    def show_notes(self, notes =None):
        if not notes:
            notes = self.notebook.notes
        for notef in notes:
            print("{0}: {1}\n{2}".format(notef.id,notef.tags, notef.memo))
        
    def search_note(self):
        filter = input("search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("enter the note")
        self.notebook.new_note(memo)
        print("your note is saved")

    def modify_note(self):
        id = input("enter note id")
        memo = input("enter the note")
        tags = input("enter the tags")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tags(id,tags)



    def quit(self):
        print("Thank you for useing")
        sys.exit(0)
if __name__ == "__main__":
    menu().run()