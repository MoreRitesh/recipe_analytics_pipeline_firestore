#  Recipe Analytics Pipeline with Firestore
A complete end-to-end Data Engineering project using **Firebase Firestore**, **Python ETL**, **Data Validation**, **Analytics**, and **Matplotlib Visualizations**.

---

##  Overview
This project demonstrates a full data engineering workflow built on top of a recipe platform dataset. 
Data is sourced from **Firebase Firestore**, extracted via Python ETL, validated, transformed, analyzed, 
and visualized using Python.

The pipeline includes:
- Firestore → CSV Export  
- Data Quality Validation  
- Normalized Dataset Creation  
- Analytics & Insights  
- Chart Visualizations  
- ER Diagram  
- Architecture Diagram  

---

##  Project Architecture  
![Architecture Diagram](Diagrams/Architecture_Diagram.png)

---

##  ER Diagram  
![ER Diagram](Diagrams/ER_Diagram.png)

---

##  Folder Structure  
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
│   └── (ServiceAccountKey.json was removed for security)
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
│   │
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

##  Firestore Setup  
Firestore collections used in this project:
- `users`
- `recipes`
- `ingredients`
- `steps`
- `interactions`

Data is populated using:
```
etl/seed_firestore.py
```

---

##  ETL: Export Firestore Data  
Exports Firestore collections into CSV format.

Run:
```
python etl/export_firestore_to_csv.py
```

---

##  Data Validation  
Ensures data completeness & consistency.

Run:
```
python Validation/validate_data.py
```

Generates:
- `validation_report.txt`

---

##  Analytics & Insights  

Run:
```
python analytics/analytics_report.py
```

Outputs:
- `insights_report.csv`
- `insights_report.txt`

---

## Visualizations  
Charts generated using:
```
python analytics/analytics_charts.py
```

Charts include:
- Difficulty donut chart  
- Boxplot of ratings  
- Ingredient treemap  
- Views vs likes bubble chart  
- Heatmap of interactions  
- Correlation matrix  
- Prep vs cook time scatter  

All charts stored in:  
`analytics/Charts/`

---

## Summary  
This project demonstrates a full data engineering pipeline using Firebase as the NoSQL backend and Python for ETL, 
validation, analytics, and visualization. It is designed to mimic a real-world recipe analytics system with 
professional documentation, diagrams, and normalized data workflows.

---

## Author  
**Ritesh More** 
**Email**: riteshmore2702@gmail.com 
Data Engineering Project – Recipe Analytics Pipeline
