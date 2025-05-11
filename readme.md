## Overview

**Project Title**: Task Manager

**Project Description**: A Task Manager built in Python that uses Firestore as a cloud database. It allows user to create, view, edit, mark complete, and delete tasks in real time, with all the data stored persistentlty online.

**Project Goals**:
- Build a simple software that interacts with a cloud database ( Firestore)
- Practice CRUD operation in Python with database
- Implement error handling for a smooth user experience
- Explore real-world tools like firebase Admin SDK

## Instructions for Build and Use

Steps to build and/or run the software:

1. Set up a firebase project and enable firestore as the database
2. Generate a Firebase Admin SDK service account key and download the JSON file
3. Install required python packages: (firebase-admin)
4. Create two Python files:
  -task_manager.py — defines functions to add, list, update, edit, and delete tasks in Firestore
  -task_menu.py — provides a menu-driven interface for interacting with the task manager
5. Use try/except blocks in each function to handle errors and prevent crashes
6. Store all tasks in Firestore collection(tasks) to ensure data persists even after the program closes
7. Use Git and Github for version control and to publish the project online

Instructions for using the software:

1. Once you open the project folder(Sprint 1) in an editor(VS Code), run the file task_menu.py
2. Choose an option from the terminal menu:
    1 to add a new task
    2 to view all tasks stored in the cloud
    3 to mark a task as completed
    4 to edit a task’s title or description
    5 to delete a task
    6 to exit the program
3. When prompted, enter task details such as title and description
4. All task data is stored and updated in Firebase Firestore automatically
5. The menu will reappear after each action, allowing you to manage multiple tasks in one session
 

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.13.3
* Firebase Admin SDK for Python
* Firebase project with Firestore enabled
* Service Account Key(JSON) 
* VS Code or any code environment of your choice

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Firebase Admin SDK (Python) Setup Guide](https://firebase.google.com/docs/admin/setup)
* [Google Cloud Firestore Python Client Docs](https://cloud.google.com/python/docs/reference/firestore/latest)
* [Python try/except (Error Handling) Documentation](https://docs.python.org/3/tutorial/errors.html)
* [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Explore ways to simulate basic user authentication or integrate with a frontend for real login functionality (JS, React, etc.) 
* [ ] Build a simple web or mobile app interface (e.g., using Flask or React Native)  
* [ ] Add task categories or tags using a second Firestore collection to organize tasks by type
