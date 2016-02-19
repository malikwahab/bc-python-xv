import unittest
from notesApplication import NotesApplication

class NotesAppTest(unittest.TestCase):
    def test_app_author(self):
        notes = NotesApplication("Malik")
        self.assertEqual("Malik", notes.author)
    def test_app_list(self):
        notes = NotesApplication("Malik")
        self.assertEqual([], notes.note_list)
    def test_app_create(self):
        notes = NotesApplication("Malik")
        note_id = notes.create("Chidi is the instructor that gives all the instructions")
        self.assertEqual("Chidi is the instructor that gives all the instructions", notes.note_list[note_id])

if __name__== "__main__":
    unittest.main()
