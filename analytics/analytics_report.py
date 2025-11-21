import pandas as pd
from datetime import datetime

# Load data
recipes = pd.read_csv("recipe.csv")
ingredients = pd.read_csv("ingredients.csv")
steps = pd.read_csv("steps.csv")
users = pd.read_csv("users.csv")
interactions = pd.read_csv("interactions.csv")

insights = []  # store insight title + text
rows = []      # store for CSV


def add_insight(title, data):
    insights.append(f"### {title}\n{data}\n")
    rows.append({"Insight": title, "Details": data})


# -----------------------------
# 1. Most viewed recipes
# -----------------------------
view_summary = interactions.groupby("recipeId")["views"].sum().reset_index()
top_viewed = view_summary.sort_values(by="views", ascending=False).head(5)
add_insight("Most Viewed Recipes", top_viewed.to_string(index=False))


# -----------------------------
# 2. Most liked recipes
# -----------------------------
like_summary = interactions.groupby("recipeId")["likes"].sum().reset_index()
top_liked = like_summary.sort_values(by="likes", ascending=False).head(5)
add_insight("Most Liked Recipes", top_liked.to_string(index=False))


# -----------------------------
# 3. Average rating per recipe
# -----------------------------
avg_rating = interactions.groupby("recipeId")["rating"].mean().reset_index()
add_insight("Average Rating Per Recipe", avg_rating.to_string(index=False))


# -----------------------------
# 4. Difficulty distribution
# -----------------------------
difficulty_dist = recipes["difficulty"].value_counts()
add_insight("Difficulty Distribution", difficulty_dist.to_string())


# -----------------------------
# 5. Average preparation and cooking time
# -----------------------------
avg_prep = recipes["prepTime"].mean()
avg_cook = recipes["cookTime"].mean()
add_insight(
    "Average Prep & Cook Time",
    f"Average Prep Time: {avg_prep:.2f} mins\nAverage Cook Time: {avg_cook:.2f} mins"
)


# -----------------------------
# 6. Most common ingredients
# -----------------------------
common_ingredients = ingredients["ingredient"].value_counts().head(10)
add_insight("Most Common Ingredients", common_ingredients.to_string())


# -----------------------------
# 7. Correlation between views & likes
# -----------------------------
correlation_df = interactions.groupby("recipeId")[["views", "likes"]].sum()
correlation_val = correlation_df["views"].corr(correlation_df["likes"])
add_insight("Correlation (Views vs Likes)", str(round(correlation_val, 3)))


# -----------------------------
# 8. Highest engagement score
# -----------------------------
interactions["engagement"] = interactions["views"] + interactions["likes"] * 2
engagement_summary = interactions.groupby("recipeId")["engagement"].sum().reset_index()
top_engagement = engagement_summary.sort_values(by="engagement", ascending=False).head(5)
add_insight("Top Engagement Recipes", top_engagement.to_string(index=False))


# -----------------------------
# 9. Ingredient popularity (total views contributed)
# -----------------------------
merged_ing = ingredients.merge(view_summary, on="recipeId")
ingredient_views = merged_ing.groupby("ingredient")["views"].sum().reset_index()
top_ing_popularity = ingredient_views.sort_values(by="views", ascending=False).head(10)
add_insight("Ingredients With Highest Views", top_ing_popularity.to_string(index=False))


# -----------------------------
# 10. User activity summary
# -----------------------------
user_activity = interactions.groupby("userId")[["views", "likes", "rating"]].sum()
add_insight("User Activity Summary", user_activity.to_string())


# -----------------------------
#  SAVE CSV + TEXT OUTPUT
# -----------------------------

# Save CSV
df_insights = pd.DataFrame(rows)
df_insights.to_csv("insights_report.csv", index=False)

# Save TXT
with open("insights_report.txt", "w", encoding="utf-8") as f:
    f.write("INSIGHTS REPORT\n")
    f.write("Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
    for line in insights:
        f.write(line + "\n")

print("✔ insights_report.csv created")
print("✔ insights_report.txt created")
