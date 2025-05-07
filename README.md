# 🛒 Product Data Analysis

This project demonstrates how to perform data analysis on a **MySQL-backed products dataset** using **Python**, **pandas**, and **SQLAlchemy**, with visualizations built using **Matplotlib** and **Seaborn**.

---

## 📊 Project Overview

We analyze a dataset of 500 products with the following columns:
- `product_id`: Unique identifier
- `product_name`: Name of the product
- `price`: Product price (USD)
- `quantity_in_stock`: Available stock count

---

## 🔧 Tech Stack

- **Python 3.11+**
- **MySQL 8+**
- **SQLAlchemy** (Database connection)
- **pymysql** (MySQL driver)
- **pandas** (Data processing)
- **matplotlib / seaborn** (Data visualization)

---

## 📂 Files Included

| File                  | Description                                 |
|-----------------------|---------------------------------------------|
| `products.sql`        | SQL script to populate 500 sample entries   |
| `product_analysis.py` | Main Python analysis & chart generation     |
| `README.md`           | Project documentation                       |
| `cleaned_data.csv`    | Optional: Exported cleaned dataset          |
| `graphs/`             | Folder containing generated plots/images    |

---

## 📈 Analysis Performed

1. **Summary statistics**
2. **Top categories by average price**
3. **Stock availability distribution**
4. **Price vs Stock scatter plot**
5. **Most expensive & cheapest products**

---

## 📌 Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/haseebahmedkha/SalesSQLAnalysisProject.git
   cd product-data-analysis
