# 📊 Amazon Sales Analytics 2025 — End-to-End Data Analysis Project  
### **By: Shavilya | Data Analyst**

This repository contains a complete **end-to-end data analytics project** built on an Amazon Sales dataset (15,000+ orders).  
The project focuses on **sales performance analysis, product insights, payment trends, delivery behavior, customer ratings, and Tableau dashboarding** — following the same analytical workflow used by teams at **Accenture, Fractal Analytics, Mu Sigma, TCS**, and other leading analytics firms.

---

# 🚀 Project Overview

The goal of this project is to:

- Clean, prepare, and understand raw e-commerce sales data  
- Explore sales, product, customer, and operational patterns  
- Build visual analytics using Tableau  
- Generate insights that can help improve revenue, logistics, and customer satisfaction  
- Organize everything in a clean, reproducible project structure  

This project covers the full lifecycle:

**Raw Data → Cleaning → EDA → Visualization → Insights → Recommendations**

---

# 📦 Dataset Overview

The dataset (stored locally in the `data/` directory, not pushed to GitHub) contains:

- **Orders**  
- **Products & categories**  
- **Customer IDs**  
- **Quantity & pricing**  
- **Payment method**  
- **Delivery status**  
- **Review ratings & text**  
- **State & country**

Total columns: **14**  
Total rows: **~15,000**

A schema and sample row are documented in:
data/README.md 

---

# 🧹 Data Preparation

Performed primarily in **`notebooks/analysis.ipynb`**:

- Converted `Date` to datetime format  
- Extracted `Year`, `Month`, `Day`  
- Verified `Total_Sales_INR = Quantity × Unit_Price_INR`  
- Handled missing review ratings/text  
- Created key derived metrics:
  - `AOV` (Average Order Value)  
  - `Revenue_per_Order`  
  - `Delivery_Success_Rate`  

---

# 📊 Exploratory Data Analysis (EDA)

All core analysis is inside:
notebooks/analysis.ipynb

### Key analyses completed:

### 🔹 **1. Sales & Revenue Analysis**
- Total Revenue  
- Total Orders  
- Units Sold  
- Average Order Value (AOV)  
- Daily/Monthly revenue trends  

### 🔹 **2. Category Performance**
- Revenue by Product Category  
- Quantity Sold by Category  
- **Pareto Analysis**: Top 4 categories ≈ 80% of total revenue  
- Identification of high-performing & underperforming segments  

### 🔹 **3. Product-Level Insights**
- Top 10 best-selling products  
- Bottom 10 products needing improvement  
- Price vs Rating patterns  
- High-volume but low-rated product clusters  

### 🔹 **4. Payment Method Analysis**
- Payment method distribution  
- Revenue contribution by method  
- Return/cancellation behavior vs payment type  
- COD vs prepaid comparison  

### 🔹 **5. Delivery & Operations Analysis**
- Delivered vs Returned orders  
- Category-wise return rate  
- State-wise delivery performance  
- Relationship between delivery delays and low ratings  

### 🔹 **6. Customer Review & Rating Analysis**
- Rating distribution  
- Top 10 highest-rated products  
- Lowest-rated products  
- Basic text analysis on `Review_Text`  
- Impact of delivery issues on rating score  

---

# 📊 Tableau Dashboard

Dashboard files are located here:
reports/tableau/AmazonSalesDashboard.twb

### **Dashboard Contains:**
  1.  KPI – Revenue Overview
  2.  KPI – Total Orders
  3.  KPI – Units Sold
  4.  KPI – Average Order Value (AOV)
  5.  Revenue Trend (Line Chart)
  6.  Category Sales (Bar Chart)
  7.  Pareto Analysis (Category-wise)
  8.  Payment Method Revenue
  9.  Delivery Status Breakdown
  10.  Rating Distribution


### **Screenshots (if any) should be placed in:**
reports/tableau/AmazonSalesDashboard.png

---

# 🧰 Tools & Technologies Used

### **Languages**
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- SQL  
- Tableau Calculated Fields  

### **Tools**
- Jupyter Notebook  
- Tableau  
- Excel  
- Git & GitHub  

### **Scripts**
Located in:
get_data.py    → Code to load or fetch dataset into local environment

---
# 📈 Summary of Key Insights

- Revenue was **consistently stable** over the period  
- All product categories showed **balanced contribution**  
- **Top 4 categories generated ~80% revenue** (Pareto)  
- COD orders showed **higher cancellation/return rates**  
- Delivery delays strongly correlated with **lower ratings**  
- Highly rated products showed **1.8× higher repeat purchase potential**  
- Certain categories had disproportionately high return rates  

---

# ▶️ How to Run This Project

### 1. Clone the Repo  
```bash
git clone https://github.com/<your-username>/amazon-sales-analytics.git
cd amazon-sales-analytics 

## 2. Set up Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt 

## 3. Add the Dataset
Place your CSV in:
data/raw/

## 4. Open Notebook
jupyter lab 

## Run: 
notebooks/analysis.ipynb 
```

# 🤝 Connect With Me

### LinkedIn:
https://www.linkedin.com/in/shavilya-rajput-9674141a0/

### GitHub:
https://github.com/shavilya

# 📜 License 
<b>MIT License.</b>
