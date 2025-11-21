import pandas as pd

# Load CSV files
recipes = pd.read_csv("recipe.csv")
ingredients = pd.read_csv("ingredients.csv")
steps = pd.read_csv("steps.csv")
users = pd.read_csv("users.csv")
interactions = pd.read_csv("interactions.csv")

errors = []   # store all validation errors


# -----------------------------
# 1. VALIDATE RECIPES
# -----------------------------
for index, row in recipes.iterrows():
    rid = row["recipeId"]

    # title
    if pd.isna(row["title"]) or row["title"].strip() == "":
        errors.append(f"Recipe {rid}: Missing title")

    # difficulty
    if row["difficulty"] not in ["easy", "medium", "hard"]:
        errors.append(f"Recipe {rid}: Invalid difficulty '{row['difficulty']}'")

    # prepTime
    if pd.isna(row["prepTime"]) or row["prepTime"] <= 0:
        errors.append(f"Recipe {rid}: prepTime must be > 0")

    # cookTime
    if pd.isna(row["cookTime"]) or row["cookTime"] <= 0:
        errors.append(f"Recipe {rid}: cookTime must be > 0")

    # ingredients exist
    if len(ingredients[ingredients["recipeId"] == rid]) == 0:
        errors.append(f"Recipe {rid}: No ingredients found")

    # steps exist
    if len(steps[steps["recipeId"] == rid]) == 0:
        errors.append(f"Recipe {rid}: No steps found")


# -----------------------------
# 2. VALIDATE USERS
# -----------------------------
for index, row in users.iterrows():
    uid = row["userId"]

    if pd.isna(uid):
        errors.append("User: Missing userId")

    if pd.isna(row["name"]) or row["name"].strip() == "":
        errors.append(f"User {uid}: Missing name")

    if pd.isna(row["email"]) or "@" not in row["email"]:
        errors.append(f"User {uid}: Invalid email '{row['email']}'")

    if pd.isna(row["location"]):
        errors.append(f"User {uid}: Missing location")


# -----------------------------
# 3. VALIDATE INTERACTIONS
# -----------------------------
valid_recipe_ids = set(recipes["recipeId"].tolist())
valid_user_ids = set(users["userId"].tolist())

for index, row in interactions.iterrows():
    uid = row["userId"]
    rid = row["recipeId"]

    # recipe must exist
    if rid not in valid_recipe_ids:
        errors.append(f"Interaction row {index}: recipeId '{rid}' not found in recipes")

    # user must exist
    if uid not in valid_user_ids:
        errors.append(f"Interaction row {index}: userId '{uid}' not found in users")

    # views >= 0
    if row["views"] < 0:
        errors.append(f"Interaction row {index}: views must be >= 0")

    # likes >= 0
    if row["likes"] < 0:
        errors.append(f"Interaction row {index}: likes must be >= 0")

    # rating 1–5
    if not (1 <= row["rating"] <= 5):
        errors.append(f"Interaction row {index}: rating must be between 1 and 5")



# -----------------------------
# 4. EXPORT VALIDATION REPORT
# -----------------------------
with open("validation_report.txt", "w", encoding="utf-8") as f:
    if len(errors) == 0:
        f.write("ALL RECORDS ARE VALID ✔\n")
    else:
        f.write("VALIDATION ERRORS FOUND:\n\n")
        for e in errors:
            f.write(e + "\n")

print("✔ Validation completed")
print("✔ validation_report.txt generated")
