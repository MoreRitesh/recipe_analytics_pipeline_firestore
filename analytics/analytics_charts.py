import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import squarify  # pip install squarify (only if allowed)

# Load CSV files
recipes = pd.read_csv("recipe.csv")
ingredients = pd.read_csv("ingredients.csv")
interactions = pd.read_csv("interactions.csv")


# -----------------------------------
# 1) Heatmap: Views vs Likes
# -----------------------------------
pivot = interactions.pivot_table(values="views", index="recipeId", columns="likes", aggfunc="sum", fill_value=0)

plt.figure(figsize=(8,6))
plt.imshow(pivot, aspect='auto')
plt.title("Heatmap: Views vs Likes")
plt.xlabel("Likes")
plt.ylabel("Recipe ID")
plt.colorbar(label="Views")
plt.tight_layout()
plt.savefig("chart_heatmap_views_likes.png")
plt.close()


# -----------------------------------
# 2) Bubble Chart: Views vs Likes vs Rating
# -----------------------------------
plt.figure(figsize=(8,6))
plt.scatter(interactions["views"], interactions["likes"], s=interactions["rating"]*100)
plt.xlabel("Views")
plt.ylabel("Likes")
plt.title("Bubble Chart: Views vs Likes (Bubble = Rating)")
plt.tight_layout()
plt.savefig("chart_bubble_views_likes_rating.png")
plt.close()


# -----------------------------------
# 3) Treemap: Ingredient Popularity
# -----------------------------------
ingredient_counts = ingredients["ingredient"].value_counts()

plt.figure(figsize=(8,6))
squarify.plot(sizes=ingredient_counts.values, label=ingredient_counts.index)
plt.title("Treemap: Ingredient Popularity")
plt.axis("off")
plt.savefig("chart_treemap_ingredients.png")
plt.close()


# -----------------------------------
# 4) Donut Chart: Difficulty Distribution
# -----------------------------------
difficulty_counts = recipes["difficulty"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(difficulty_counts, labels=difficulty_counts.index, wedgeprops={'width':0.4}, autopct="%1.1f%%")
plt.title("Difficulty Distribution (Donut Chart)")
plt.tight_layout()
plt.savefig("chart_difficulty_donut.png")
plt.close()


# -----------------------------------
# 5) Scatter: PrepTime vs CookTime
# -----------------------------------
plt.figure(figsize=(8,6))
plt.scatter(recipes["prepTime"], recipes["cookTime"])
plt.xlabel("Prep Time")
plt.ylabel("Cook Time")
plt.title("Scatter Plot: PrepTime vs CookTime")
plt.tight_layout()
plt.savefig("chart_preptime_vs_cooktime.png")
plt.close()


# -----------------------------------
# 6) Boxplot: Ratings
# -----------------------------------
plt.figure(figsize=(6,5))
plt.boxplot(interactions["rating"])
plt.title("Boxplot: Ratings")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("chart_boxplot_ratings.png")
plt.close()


# -----------------------------------
# 7) User activity bar chart
# -----------------------------------
user_activity = interactions.groupby("userId")[["views","likes"]].sum().sum(axis=1)

plt.figure(figsize=(8,5))
plt.bar(user_activity.index, user_activity.values)
plt.title("User Activity (Views + Likes)")
plt.xlabel("User ID")
plt.ylabel("Total Engagement")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart_user_activity.png")
plt.close()



corr = interactions[["views","likes","rating"]].corr()

plt.figure(figsize=(6,5))
plt.imshow(corr, cmap="gray")
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)
plt.colorbar()
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("chart_correlation_matrix.png")
plt.close()


print("✔ All advanced charts generated successfully!")
