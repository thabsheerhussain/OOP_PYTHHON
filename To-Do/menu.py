import sys
from todo import todo

class menu:
     def __init__(self):
        self.todo = todo()
        self.choice = {

            "1":self.show_todo,
            "3":self.add_todo,
            "4":self.finish_todo,
            "5":self.quit,
        }
        
    def display(self):
        print(
            """
                Menu

            "1":self.show_todo,
            "3":self.add_todo,
            "4":self.finish_todo,
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

    def show_todo(self, dos =None):
        if not dos:
            dos = self.todo.dos
        for todof in dos:
            print("{0}: {1}\n{2}".format(todof.id, todof.todo))

    def add_note(self):
        note = input("enter the note")
        self.todo.new_note(todo)
        print("your note is saved")

    def quit(self):
        print("Thank you for useing")
        sys.exit(0)
if __name__ == "__main__":
    menu().run()