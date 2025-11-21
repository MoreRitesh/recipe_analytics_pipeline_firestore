# 🍽️ Recipe Analytics Pipeline with Firestore  
A complete end-to-end Data Engineering project using **Firebase Firestore**, **Python ETL**, **Data Validation**, **Analytics**, and **Matplotlib Visualizations**.

---

## 📌 Overview  
This project demonstrates a real-world **Data Engineering pipeline** built on top of a recipe analytics platform.  
The system collects recipe-related data in Firestore, exports it into structured CSVs, validates data quality,  
performs analytics, and generates visual insights.

The pipeline includes:

- Firebase → CSV Data Extraction  
- Data Quality Validation  
- Normalized Dataset Creation  
- Analytics & Insight Generation  
- Matplotlib Visualizations  
- ER & Architecture Diagrams  

---

## 🏗️ Project Architecture  
This diagram shows the entire workflow from Firestore → ETL → Validation → Analytics → Charts.

![Architecture Diagram](Diagrams/Architecture_Diagram.png)

---

## 🧩 ER Diagram  
The ER diagram represents relationships between **Users**, **Recipes**, **Ingredients**, **Steps**, and **Interactions**.

![ER Diagram](Diagrams/ER_Diagram.png)

---

## 📁 Folder Structure
```
recipe_analytics_pipeline/
│
├── README.md
├── .gitignore
│
├── data/
│   ├── recipe.csv
│   ├── ingredients.csv
│   ├── steps.csv
│   ├── users.csv
│   ├── interactions.csv
│
├── etl/
│   ├── export_firestore_to_csv.py
│   ├── seed_firestore.py
│   └── (ServiceAccountKey.json removed for security)
│
├── Validation/
│   ├── validate_data.py
│   └── validation_report.txt
│
├── analytics/
│   ├── analytics_report.py
│   ├── analytics_charts.py
│   ├── insights_report.csv
│   ├── insights_report.txt
│
│   ├── Charts/
│   │   ├── chart_boxplot_ratings.png
│   │   ├── chart_bubble_views_likes_rating.png
│   │   ├── chart_correlation_matrix.png
│   │   ├── chart_difficulty_donut.png
│   │   ├── chart_heatmap_views_likes.png
│   │   ├── chart_preptime_vs_cooktime.png
│   │   ├── chart_treemap_ingredients.png
│   │   └── chart_user_activity.png
│
├── Diagrams/
│   ├── Architecture_Diagram.png
│   └── ER_Diagram.png
│
└── requirements.txt
```

---

## 🔥 Firestore Setup  
Firestore collections used:

- `users`
- `recipes`
- `ingredients`
- `steps`
- `interactions`

Seed Firestore with sample recipe data:

```bash
python etl/seed_firestore.py
```

---

## 📤 ETL: Export Firestore to CSV  
This script extracts Firestore data and saves it into structured CSV files.

```bash
python etl/export_firestore_to_csv.py
```

Outputs:
- recipe.csv  
- ingredients.csv  
- steps.csv  
- users.csv  
- interactions.csv  

---

## 🛡️ Data Validation  
Ensures data completeness & consistency.

Run:
```bash
python Validation/validate_data.py
```

Generates:
- `validation_report.txt`

---

## 📊 Analytics & Insights  
Run:
```bash
python analytics/analytics_report.py
```

Outputs:
- insights_report.csv  
- insights_report.txt  

---

## 📈 Key Visualizations  
Below are 4 selected charts that best represent the dataset and insights.

---

### ⭐ **1. Difficulty Distribution (Donut Chart)**
![Difficulty Chart](analytics/Charts/chart_difficulty_donut.png)

---

### ⭐ **2. Heatmap: Views vs Likes**
![Heatmap](analytics/Charts/chart_heatmap_views_likes.png)

---

### ⭐ **3. Treemap: Ingredient Popularity**
![Treemap](analytics/Charts/chart_treemap_ingredients.png)

---

### ⭐ **4. Bubble Chart: Views vs Likes vs Rating**
![Bubble Chart](analytics/Charts/chart_bubble_views_likes_rating.png)

---

## 📝 Summary  
This project showcases a complete data engineering pipeline using Firebase as the NoSQL backend and Python for ETL, validation, analytics, and visualization.

It reflects industry-level best practices including:
- Modular ETL scripts  
- Data quality enforcement  
- Statistical insights  
- Professional visualizations  
- Clean architecture  
- Well-documented project structure  

---

## 👤 Author  
**Ritesh More**  
📧 *riteshmore2702@gmail.com*  
Recipe Analytics Pipeline – Data Engineering Project
