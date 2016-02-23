class NotesApplication(object):
    """

    A note Object class with attributes
    and methods for managing those notes. Provides
    methods to create, get, edit, delete amd search list

    attributes
    self.content_format -- The format for displaying notes
    self.author -- Author of the notes in the object
    self.note_list -- a list object to hold note contents

    """

    content_format = "Note ID: {}\n{}\n\nBy Author {}\n"

    def __init__(self, author):
        """
            create self.author with the passed argument author
            and initialize an empty string
            self,author -- the author of the notes
            list -- a list object to hold all note content

        """
        self.author = author
        self.note_list = []

    def create(self, note_content):
        """
            takes in one parameter, the note content and adds it to the
            lists holding all the notes of the object

            notee_content -- content of the note to be created

            return
            False if an empty string is passed as content
            the key(note id) of the note in the list

        """
        if note_content == '':
            return False
        self.note_list.append(note_content)
        return (len(self.note_list) - 1)

    def list(self):
        """
            list out content all the notes in object
            using the format define by self.content_format
            content -- the formatted contents from the list

            return
            returns the content of all the list or informing of no notes

        """
        if len(self.note_list) <= 0:
            return "No note created yet"
        content = ""
        for i in range(len(self.note_list)):
            content += self.content_format.format(i, self.note_list[i], self.author)
        return content

    def get(self, note_id):
        """
            Get a note with the  id passed as argument
            uses the is_note_id method to check if note_id a 
            valid id

            return
            False if no note is found with te id
            The content of the notes
        """
        if self.is_note_id(note_id):
            return self.note_list[int(note_id)]
        else:
            return False

    def is_note_id(self, note_id):
        """
            Checks if an id exist with that id

            return
            True if it does
            False if not in the list
        """
        try:
            self.note_list[int(note_id)]
            return True
        except (IndexError, ValueError):
            return False

    def search(self, search_text):
        """
            Takes a search text and return all notes where the search text exist

            return
            A formatted String containing all the list with that search
            or a string informing the user that search term does not exist
        """
        content = "Showing results for search " + search_text + "\n"
        found = 0
        for i in range(len(self.note_list)):
            if self.note_list[i].find(search_text) > -1:
                content += self.content_format.format(i, self.note_list[i], self.author)
                found += 1
        if found == 0:
            return "No Result found"
        return content

    def delete(self, note_id):
        """
            Delete the note content with index as note_id

            return
            True on success
            False if id is not an index of the note list
        """
        if self.is_note_id(note_id):
            del(self.note_list[int(note_id)])
            return True
        else:
            return False

    def edit(self, note_id, new_content):
        """
            Replace the content with the note id with the new content pass

            return
            True on success
            False if id is not an index of the note list
        """
        if self.is_note_id(note_id):
            self.note_list[int(note_id)] = new_content
            return True
        else:
            return False
