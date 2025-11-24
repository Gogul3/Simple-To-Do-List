import sys

todo_list = []

def show_menu():
    print("\n--- Simple To-Do List ---")
    print("1. View to-do list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Quit")

def display_list():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, item in enumerate(todo_list, 1):
            print(f"{idx}. {item}")

def add_item():
    item = input("\nEnter a new to-do item: ").strip()
    if item:
        todo_list.append(item)
        print(f'"{item}" added to your to-do list.')
    else:
        print("No item entered.")

def remove_item():
    display_list()
    if not todo_list:
        return
    try:
        num = int(input("\nEnter the number of the item to remove: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f'"{removed}" removed from your to-do list.')
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        if choice == "1":
            display_list()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()