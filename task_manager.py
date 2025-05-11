# Import necessary modules for Firebase and Firestore
from firebase_admin import credentials, firestore
import firebase_admin
from google.cloud.firestore_v1 import FieldFilter

# Initialize Firebase with the service account JSON key
cred = credentials.Certificate("task-manager-c7e43-firebase-adminsdk-fbsvc-7c1dc09c47.json")
firebase_admin.initialize_app(cred)

#Create a Firestore client to access the database
db = firestore.client()

#Function to add a new task
def add_task(title, description):
    task_data = {
        "title": title,
        "description": description,
        "completed": False,
        "timestamp": firestore.SERVER_TIMESTAMP
    }
    
    try: 
        db.collection("tasks").add(task_data)
        print(f"Task {title} added successfully.")
    
    except Exception as  e:
        print(f"Failed to add task '{title}': {e}")


#Function to list all tasks
def list_tasks():
    try:
        tasks = db.collection("tasks").stream()
        print("Your tasks:")
        for task in tasks:
            task_data = task.to_dict()
            print(f"- {task_data['title']} | Done: {task_data['completed']}")
            print(f"   Description: {task_data['description']}")
            print("------")
    
    except Exception as e:
        print("Failed to list tasks:", e)


#Function to mark a task coomplete
def complete_task(title_to_complete):
    try:

        tasks = db.collection("tasks").where(filter=FieldFilter("title", "==", title_to_complete)).stream()

        found = False
        for task in tasks:
            db.collection("tasks").document(task.id).update({
                "completed": True,
                "timestamp": firestore.SERVER_TIMESTAMP
            })

            print(f" Task ' {title_to_complete}' marked as completed.")
            found = True
        
        if not found:
            print(f" Task with title {title_to_complete} was not completed (maybe it doesn't exist).")

    except Exception as e:
        print(f"Error completing task '{title_to_complete}': {e}")


#Function to edit a task's title or description
def edit_task(current_title, new_title = None, new_description=None):
    try:

        tasks = db.collection("tasks").where(filter=FieldFilter("title", "==", current_title)).stream()

        found = False

        for task in tasks:

            updates = {}

            if new_title is not None:
                updates["title"] = new_title
            
            if new_description is not None:
                updates["description"] = new_description

            updates["timestamp"] = firestore.SERVER_TIMESTAMP

            db.collection("tasks").document(task.id).update(updates)
            print(f" Task '{current_title}' updated.")
            
            found= True
        
        if not found:
            print(f" Task '{current_title}' was not found to be edited.")

    except Exception as e:
        print(f" Error editing task '{current_title}': {e}")

#Function to delete a task from Firestore
def delete_task(title_to_delete):
    try:

        tasks = db.collection("tasks").where(filter=FieldFilter("title", "==", title_to_delete)).stream()

        found = False

        for task in tasks:
            db.collection("tasks").document(task.id).delete()
            print(f" Task '{title_to_delete}' is deleted.")
            found = True
        
        if not found:
            print(f" Task '{title_to_delete}' was not deleted(maybe it doesn't exist).")

    except Exception as e:
        print(f" Error deleting task '{title_to_delete}': {e}")

#Prevents this file from running standalone
#Used to separate logic from interface
if __name__ == "__main__":
    print("This file is a library of functions. Please run task_menu.py instead.")
