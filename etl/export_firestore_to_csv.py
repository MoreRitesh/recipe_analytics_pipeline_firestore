from google.cloud import firestore
from google.oauth2 import service_account
import pandas as pd

# Load service account key
credentials = service_account.Credentials.from_service_account_file(
    "ServiceAccountKey.json"   # <-- update path
)

db = firestore.Client(credentials=credentials, project="recipe-analytics-rm")

# --------------------------
# EXPORT USERS
# --------------------------
def export_users():
    users_ref = db.collection("users").stream()

    data = []
    for doc in users_ref:
        d = doc.to_dict()
        data.append(d)

    df = pd.DataFrame(data)
    df.to_csv("users.csv", index=False)
    print("✔ users.csv exported")


# --------------------------
# EXPORT RECIPES + INGREDIENTS + STEPS
# --------------------------
def export_recipes():
    recipes_ref = db.collection("recipes").stream()

    recipe_rows = []
    ingredient_rows = []
    step_rows = []

    for doc in recipes_ref:
        d = doc.to_dict()

        recipe_id = doc.id

        # main recipe table
        recipe_rows.append({
            "recipeId": recipe_id,
            "title": d.get("title"),
            "description": d.get("description"),
            "difficulty": d.get("difficulty"),
            "prepTime": d.get("prepTime"),
            "cookTime": d.get("cookTime"),
            "createdAt": d.get("createdAt")
        })

        # ingredients table
        ingredients = d.get("ingredients", [])
        for ing in ingredients:
            ingredient_rows.append({
                "recipeId": recipe_id,
                "ingredient": ing
            })

        # steps table
        steps = d.get("steps", [])
        for i, step in enumerate(steps, start=1):
            step_rows.append({
                "recipeId": recipe_id,
                "stepNumber": i,
                "stepDescription": step
            })

    # Convert to CSV
    pd.DataFrame(recipe_rows).to_csv("recipe.csv", index=False)
    pd.DataFrame(ingredient_rows).to_csv("ingredients.csv", index=False)
    pd.DataFrame(step_rows).to_csv("steps.csv", index=False)

    print("✔ recipe.csv, ingredients.csv, steps.csv exported")


# --------------------------
# EXPORT INTERACTIONS
# --------------------------
def export_interactions():
    inter_ref = db.collection("interactions").stream()

    data = []
    for doc in inter_ref:
        d = doc.to_dict()
        data.append(d)

    df = pd.DataFrame(data)
    df.to_csv("interactions.csv", index=False)

    print("✔ interactions.csv exported")


# --------------------------
# MAIN
# --------------------------
if __name__ == "__main__":
    export_users()
    export_recipes()
    export_interactions()
    print("✔ All export tasks completed")
