from notesApplication import NotesApplication

def create_new_note(note_author):
    content = input("Enter Note Content Below \n")
    if content == "":
        return "failed no content Entered"
    note_author.create(content)
    return "Success Note Created"
def open_note(note_author):
    note_id = input("Enter 'all' to print all notes or note'Id to open note:")
    if note_id == 'all':
        return note_author.list()
    else:
        note = note_author.get(int(note_id))
        if not note:
            return "invalid Note id Entered"
        return note
def delete_note(note_author):
    note_id = input("Enter id of note to be deleted:")
    if note_author.delete(int(note_id)):
        return "Note "+note_id+" deleted"
    return "Invalid Note Id entered"
    
def search_note(note_author):
    search_text = input("Enter text you want to search")
    return note_author.search(search_text)
def edit_note(note_author):
    note_id = input("Enter id of note you want to edit:")
    if note_id == "":
        return "Enter an Id"
    elif note_author.is_note_id(note_id):
        content = input("Enter new Content")
        note_edit = note_author.edit(node_id, content)
        return "Note Edited"
    else:
        return "Invalid note Id entered"

#Output Program strat here

user_input = ""

#Untill an input is entered, application keeps asking for name
while user_input == "":
    user_input = input("Welcome! Enter Your Name:")
note_author = NotesApplication(user_input)

#the user guide statement
guide = "Enter \n'New' to create a new list\n'Open' to open a note\n'Delete' to delete a note\n'Search' to search all notes\n'Edit to edit a note\n'Exit to quit Application\n:"

user_action = ''
#apllication remains alive until user entered exit
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
        print(search_note(note_author))
    elif user_action == 'edit':
        print(edit_note(note_author))
    elif user_action == 'exit':
        break
    else:
        #continue the while loop until user enter a valid input
        print("INVALID!! follow Guide to use application")
        continue
#save the state of the application to keep notes