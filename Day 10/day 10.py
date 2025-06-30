
    with open("try.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'try.txt' does not exist.")

with open("notes.txt", "w") as file:
    file.write("\nThis is a new note.\n")

with open("notes1.txt", "a") as file:
    file.write("\nThis is a new second note.")


## Note App
# 1: Define file name
FILE_NAME = "notes.txt"

# 2: Display menu options
def show_menu():
  print("\n MENU")
  print("1. Add new note")
  print("2. View notes")
  print("3. Delete notes")
  print("4. Exit")

# 3: Add a new note
def add_note():
  note = input("Enter your note: ")
  with open(FILE_NAME, "a") as file:
    file.write(note + "\n")
  print("Note added successfully!")

# 4: View all notes
def view_notes():
  try:
    with open(FILE_NAME, "r") as file:
      content = file.read()
      if content:
        print("\n Your Notes ")
        print(content)
      else:
        print("\nNo notes found.")
  except FileNotFoundError:
    print("No notes found.")

# 5: Delete all notes
def delete_notes():
  confirm = input("Are you sure you want to delete all notes? (Yes/n): ")
  if confirm.lower() == "yes":
    with open(FILE_NAME, "w") as file:
      pass
    print("All notes have been deleted")
  else:
    print("Deletion cancelled")

# 6: Main Program 
while True:
  show_menu()
  choice = input("Enter your choice (1-4): ")

  if choice == "1":
    add_note()
  elif choice == "2":
    view_notes()
  elif choice == "3":
    delete_notes()
  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")