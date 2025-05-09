import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("task-manager-c7e43-firebase-adminsdk-fbsvc-7c1dc09c47.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

doc_ref = db.collection("testCollection").document("helloDoc")

doc = doc_ref.get()
if doc.exists:
    print("Document data:", doc.to_dict())
else:
    print("No such document!")