'''
Menu module.
'''
import sys
from notebook import Notebook

class Menu:
    '''
    Display a menu and respond to choices when run.

    Attributes
    ----------
    notebook: Notebook.
        Notebook object.
    choices: dict,
        dictionary with corespondaces between numbers of options
    and options they-selves.

    Methods
    ----------
    run:
        activates a work with menu.
    display_menu: None,
            prints a string for menu.
    show_notes: None,
            prints notes to the user.
    search_notes: None,
            shows notes that correspond to the given filter.
    add_note: None:
            creates a new note.
    modify_note: None,
            modifies a note.
    '''
    def __init__(self):
        '''
        Initializes the object.
        '''
        self.notebook = Notebook()
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_note,
        "4": self.modify_note,
        "5": self.quit
        }

    def display_menu():
        '''
        Prints a string for menu.
        '''
        print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
             """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        '''
        Prints notes to the user.
        '''
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        '''
        Shows notes that correspond to the given filter.
        '''
        filer_value = input("Search for: ")
        notes = self.notebook.search(filer_value)
        self.show_notes(notes)

    def add_note(self):
        '''
        Adds a new note.
        '''
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        '''
        Modifies a note.
        '''
        id_value = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id_value, memo)
        if tags:
            self.notebook.modify_tags(id_value, tags)

    def quit():
        '''
        Quites the program.
        '''
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
