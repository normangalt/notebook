'''
Notebook module.
'''

import datetime
# Store the next available id for all new notes
LAST_ID = 0
class Note:
    '''Represent a note in the notebook. Match against a
            passstring in searches and store tags for each note.'''
    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        global LAST_ID
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        LAST_ID += 1
        self.id = LAST_ID

    def match(self, filter_input):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags.

        Parameters
        ----------
        filter_input: str,
                    filter a note must be matched to.
        '''
        return filter_input in self.memo or filter_input in self.tags

class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''
    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list.

        Parameters
        ----------
        memo: str,
            the string the note must contain.
        tags: str,
            the tags of the note.
        '''
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its
        memo to the given value.

        Parameters
        ----------
        note_id: int,
            id of the note to modify.
        memo: str,
            string to use to modify the note.
        '''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given id and change its
        tags to the given value.

        Parameters
        ----------
        note_id: int,
            id of the note to modify.
        tags: str,
            string to use to modify the tags of the note.
        '''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter_input):
        '''
        Find all notes that match the given filter
        string.

        Parameters
        ----------
        filter_input: str,
                    string to filter the notes by.
        '''
        return [note for note in self.notes if note.match(filter_input)]
