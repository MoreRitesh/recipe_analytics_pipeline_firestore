from google.cloud import firestore
from google.oauth2 import service_account
from datetime import datetime
import random

# Load credentials without needing GOOGLE_APPLICATION_CREDENTIALS
credentials = service_account.Credentials.from_service_account_file(
    "ServiceAccountKey.json"   # <-- change this path
)

db = firestore.Client(credentials=credentials, project="recipe-analytics-rm")

# Your main recipe (Puran Poli)
my_recipe = {
    "recipeId": "puran_poli_ritesh",
    "title": "Ritesh Special Puran Poli",
    "description": "Authentic Maharashtrian sweet flatbread stuffed with chana dal and jaggery filling.",
    "difficulty": "medium",
    "prepTime": 40,
    "cookTime": 30,
    "ingredients": [
        "2 cups wheat flour",
        "1 cup chana dal (split Bengal gram)",
        "1 cup grated jaggery",
        "1/4 tsp cardamom powder",
        "2 tbsp ghee",
        "Salt as needed"
    ],
    "steps": [
        "Wash and boil chana dal until soft.",
        "Drain and mash the dal, then mix with jaggery and cook to make puran.",
        "Knead wheat flour dough with a little salt.",
        "Stuff the puran into dough balls and roll gently.",
        "Cook on tawa with ghee until golden brown."
    ],
    "createdAt": datetime.utcnow()
}

def insert_initial_data():
    # -------------------------------
    # 1) Insert USERS collection
    # -------------------------------
    users = []
    for i in range(1, 11):
        user = {
            "userId": f"user_{i}",
            "name": f"User {i}",
            "email": f"user{i}@example.com",
            "location": random.choice(["Pune", "Mumbai", "Nagpur", "Nashik"]),
            "createdAt": datetime.utcnow()
        }
        db.collection("users").document(user["userId"]).set(user)
        users.append(user)

    print("✔ 10 users inserted")


    # -------------------------------
    # 2) Insert main recipe
    # -------------------------------
    db.collection("recipes").document(my_recipe["recipeId"]).set(my_recipe)
    print("✔ Puran Poli recipe inserted")


    # -------------------------------
    # 3) Insert 15 synthetic recipes
    # -------------------------------
    for i in range(1, 16):
        recipe = {
            "title": f"Sample Recipe {i}",
            "description": "Synthetic recipe for ETL testing",
            "difficulty": ["easy", "medium", "hard"][i % 3],
            "prepTime": 10 + i,
            "cookTime": 15 + i,
            "ingredients": ["ingredient1", "ingredient2"],
            "steps": ["step1", "step2"],
            "createdAt": datetime.utcnow()
        }
        db.collection("recipes").add(recipe)

    print("✔ 15 synthetic recipes inserted")


    # -------------------------------
    # 4) Insert interactions
    # (Views & likes are numeric counts)
    # -------------------------------
    for j in range(1, 11):
        interaction = {
            "recipeId": "puran_poli_ritesh",
            "userId": f"user_{j}",
            "views": random.randint(1, 20),
            "likes": random.randint(0, 5),
            "rating": random.randint(1, 5),
            "timestamp": datetime.utcnow()
        }
        db.collection("interactions").add(interaction)

    print("✔ 10 interactions inserted")


if __name__ == "__main__":
    insert_initial_data()
