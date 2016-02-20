class NotesApplication(object):
    content_format = "Note ID: {} \n{} \n\nBy Author {}\n"
    def __init__(self, author):
        self.author = author
        self.note_list = []
    def create(self, note_content):
        self.note_list.append(note_content)
        return (len(self.note_list) - 1)
    def list(self):
        content = ""
        for i in range(len(self.note_list)):
            content += self.content_format.format(i, self.note_list[i], self.author)
        return content
    def get(self, note_id):
        if self.is_note_id(note_id):
            return self.note_list[note_id]
        else:
            return False
    def is_note_id(self, note_id):
        try:
            valid_id = self.note_list[int(note_id)]
            return True
        except (IndexError, ValueError):
            return False
    def search(self, search_text):
        content = "Showing results for search "+search_text+"\n"
        found = 0
        for i in range(len(self.note_list)):
            if self.note_list[i].find(search_text) > -1:
                content += self.content_format.format(i, self.note_list[i], self.author)
                found += 1
        if found == 0:
            return "No Result found"
        return content
    def delete(self, note_id):
        if self.is_note_id(note_id):
            del(self.note_list[note_id])
            return True
        else:
            return False
    def edit(self, note_id, new_content):
        if self.is_note_id(note_id):
            self.note_list[note_id] = new_content
            return self
        else:
            return False
'''
malik_note = NotesApplication("Malik")

malik_note.create("I Love to code, and coding loves me too")
malik_note.create("Here is temmie beside me, temmie loves to code too")
malik_note.create("Adim is over there, with all the programming experience")
print(malik_note.create("Chidi is the instructor that gives all the instructions"))
malik_note.edit(2, "Adim is over there, enjoying coding with all the programming experience")
#print(malik_note.list())
#malik_note.delete(2)
print(malik_note.is_note_id("hmamfej"))


'''
