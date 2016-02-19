from notesApplication import NotesApplication
def create_new_note(note_author):
    content = input("Enter Note Content Below \n")
    if content == "":
        return "failed no content Entered"
    note_author.create(content)
    return "Success Note Created"
def open_note(note_author):
    note_id = input("Enter 'all' to print all notes or note'Id to open note:")
    #check valid id
    if note_id == 'all':
        return note_author.list()
    else:
        return note_author.get(int(note_id))
def delete_note(note_author):
    note_id = input("Enter id of note to be deleted:")
    note_author.delete(int(note_id))
    return "Note "+note_id+" deleted"
def search_note(note_author):
    search_text = input("Enter text you want to search")
    return note_author.search(search_text)
def edit_note(note_author):
    note_id = input("Enter id od note you want to edit:")
    if note_id == "":
        return "Enter an Id"
    content = input("Enter new Content")
    note_author.edit(node_id, content)
    return "Note Edited"
user_input = ""


while user_input == "":
    user_input = input("Welcome! Enter Your Name:")
note_author = NotesApplication(user_input)


guide = "Enter \n'New' to create a new list\n'Open' to open a note\n'Delete' to delete a note\n'Search' to search all notes\n'Edit to edit a note\n'Exit to quit Application\n:"
user_action = ''
while user_action != "exit":
    user_action = input(guide).lower()
    if user_action == 'new':
        status = create_new_note(note_author)
        print(status)
    elif user_action == 'open':
        notes = open_note(note_author)
        print(notes)
    elif user_action == 'delete':
        print(delete_note(note_author))
    elif user_action == 'search':
        result = search_note(note_author)
        print(result)
    elif user_action == 'edit':
        edit_note(note_author)
    elif user_action == 'exit':
        break
    else:
        print("INVALID!! follow Guide to use application")
        continue
