import unittest
from notesApplication import NotesApplication


class NotesAppTest(unittest.TestCase):

    notes = NotesApplication("Malik")
    notes.create("The first note created with the application for testing")
    notes.create("So you managed to get through a phone screen, ten resume revisions")
    notes.create("The life of a freelancer can sound very romantic: you have the flexibility")

    def test_app_author(self):
        self.assertEqual("Malik", self.notes.author)

    def test_app_list(self):
        notes = NotesApplication("Malik")
        self.assertEqual([], notes.note_list)

    def test_app_list_fail(self):
        notes = NotesApplication("Wahab")
        self.assertNotEqual(["has content", "But not Initialized yet"], notes.note_list)

    def test_app_create(self):
        notes = NotesApplication("Malik")
        note_id = notes.create("The first note created with the application for testing")
        self.assertEqual("The first note created with the application for testing", notes.note_list[note_id])

    def test_app_create_fail(self):
        notes = NotesApplication("Malik")
        result = notes.create("")
        self.assertFalse(result)

    def test_app_edit(self):
        self.notes.edit(0, "A new Content for the note I created earlier on")
        self.assertEqual("A new Content for the note I created earlier on", self.notes.note_list[0])

    def test_app_edit_fail(self):
        result = self.notes.edit(78, "A new Content for the note I created earlier on")
        self.assertFalse(result)

    def test_app_get(self):
        note = self.notes.get(0)
        self.assertEqual("A new Content for the note I created earlier on", note)

    def test_app_get_fail(self):
        self.assertFalse(self.notes.get(80))

    def test_app_get_list(self):
        # Construction of expected ouput
        expected_result = "Note ID: 0\nA new Content for the note I created "
        expected_result += 'earlier on\n\nBy Author Malik\nNote ID: 1\nSo '
        expected_result += 'you managed to get through a phone screen, ten resume revisions'
        expected_result += '\n\nBy Author Malik\nNote ID: 2\nThe life of a '
        expected_result += 'freelancer can sound very romantic: you have the flexibility'
        expected_result += '\n\nBy Author Malik\n'
        self.assertEqual(expected_result, self.notes.list())

    def test_app_get_list_empty(self):
        expected_result = "No note created yet"
        notes = NotesApplication('Mide')
        self.assertEqual(expected_result, notes.list())

    def test_app_is_note_id(self):
        self.assertTrue(self.notes.is_note_id(0))

    def test_app_is_note_id_fail(self):
        self.assertFalse(self.notes.is_note_id(50))

    def test_app_is_note_id_string(self):
        self.assertFalse(self.notes.is_note_id("50"))

    def test_app_delete(self):
        notes = NotesApplication('John')
        notes.create("I want to write more, But I cannot Find the word")
        notes.delete(0)
        self.assertEqual([], notes.note_list)

    def test_app_delete_Missing(self):
        notes = NotesApplication('John')
        notes.create("I want to write more, But I cannot Find the word")
        result = notes.delete(90)
        self.assertFalse(result)

    def test_app_delete_two(self):
        notes = NotesApplication('Mide')
        notes.create("Alot happened so far")
        notes.create("And alot still to happen")
        notes.delete(0)
        self.assertEqual("And alot still to happen", notes.note_list[0])

    def test_app_search(self):
        result = self.notes.search("romantic")
        expected_result = "Showing results for search romantic\n"
        expected_result += "Note ID: 2\nThe life of a freelancer can sound very"
        expected_result += " romantic: you have the flexibility\n\nBy Author Malik\n"
        self.assertEqual(expected_result, result)

    def test_app_search_two(self):
        result = self.notes.search("the")
        expected_result = "Showing results for search the\n"
        expected_result += "Note ID: 0\nA new Content for the note I created "
        expected_result += "earlier on\n\nBy Author Malik\n"
        expected_result += "Note ID: 2\nThe life of a freelancer can sound very"
        expected_result += " romantic: you have the flexibility\n\nBy Author Malik\n"
        self.assertEqual(expected_result, result)

    def test_app_search_fail(self):
        result = self.notes.search("Andela")
        expected_result = "No Result found"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
