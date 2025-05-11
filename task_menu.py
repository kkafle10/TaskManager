# This is the main file to run the Task Manager app.

#import all the task-related function from task_manager.py
import task_manager

#Terminal menu interface
def menu():
    while True:
        print("\n Task Manager Menu")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark task as completed")
        print("4. Edit a task")
        print("5. Delete a task")
        print("6. Exit")

        # Ask the user to choose an option
        choice = input("Enter your choice (1-6): ")

        # Option 1: Add a new task
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        
        # Option 2: List all tasks from Firestore
        elif choice == "2":
            task_manager.list_tasks()
        
        # Option 3: Mark a task as completed
        elif choice == "3":
            title = input("Enter title of task to mark as complete: ")
            task_manager.complete_task(title)
        
        # Option 4: Edit a task's title and/or description
        elif choice == "4":
            current = input("Enter current title of task: ")
            new_title = input("New title (leave blank to skip): ")
            new_description = input("New description (leave blank to skip): ")

            # Pass new values only if user typed them
            task_manager.edit_task(
                current,
                new_title=new_title if new_title else None,
                new_description=new_description if new_description else None
            )
        
        # Option 5: Delete a task
        elif choice == "5":
            title = input("Enter title of task to delete: ")
            task_manager.delete_task(title)
        
        # Option 6: Exit the program
        elif choice == "6":
            print("Goodbye!")
            break
        # Catch invalid inputs
        else:
            print("Invalid choice. Please try again!")

# Call the menu to start the program
menu()
