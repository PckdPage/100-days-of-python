# 1: Initiate empty list
shopping_list = []

# 2: Define menu
def menu():
    print("Shopping List Menu")
    print("1. View shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear List")
    print("5. Exit")

# 3: Main Part (logic)
while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("LIST")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index+1}.{item}")
        
    elif choice == "2":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to the list.")
    
    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list")
        else:
            print(f"{item} is not in the list.")
    
    elif choice == "4":
        shopping_list.clear()
        print("List Cleared!")
    
    elif choice == "5":
        print("Byee!")
        break

    else:
        print("Invalid Choice. Please try again.")

