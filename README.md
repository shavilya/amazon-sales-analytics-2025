# 📊 E-Commerce Revenue & Supply Chain Optimization  
### **End-to-End Data Analysis Project**  
**By: Shavilya | Data Analyst**

This repository contains a complete **end-to-end data analytics project** built on an **Amazon Sales dataset (15,000+ orders)**.

The project focuses on **sales performance analysis, product insights, payment trends, delivery behavior, customer ratings, and Tableau dashboarding** — following the same analytical workflow used by analytics teams at **Accenture, Fractal Analytics, Mu Sigma, TCS**, and similar firms.

---

## 📊 Tableau Dashboard Snapshot

<img width="2598" height="1798" alt="Amazon_Sales_Dashboard" src="https://github.com/user-attachments/assets/49f74c2a-6e3f-4486-a8cc-a44e6c946c94" />


🔗 **Interactive Dashboard (Tableau Public):**  
https://public.tableau.com/views/Amazon_Sales_Dashboard_17683901017380/Amazon_Sales_Dashboard

---

## 🚀 Project Overview

The goal of this project is to:

- Clean, prepare, and understand raw e-commerce sales data  
- Explore sales, product, customer, and operational patterns  
- Build visual analytics using Tableau  
- Generate insights to improve **revenue, logistics, and customer satisfaction**  
- Maintain a **clean, reproducible analytics workflow**

**Project Lifecycle:**  
**Raw Data → Cleaning → EDA → Visualization → Insights → Recommendations**

---

## 📦 Dataset Overview

The dataset (stored locally in the `data/` directory and not pushed to GitHub) includes:

- **Orders**  
- **Products & Categories**  
- **Customer IDs**  
- **Quantity & Pricing**  
- **Payment Method**  
- **Delivery Status**  
- **Review Ratings & Text**  
- **State & Country**

**Total Columns:** 14  
**Total Rows:** ~15,000  

📄 Schema & sample rows:  
`data/README.md`

---

## 🧹 Data Preparation

Performed primarily in **`notebooks/analysis.ipynb`**:

- Converted `Date` to datetime format  
- Extracted `Year`, `Month`, `Day`  
- Validated `Total_Sales_INR = Quantity × Unit_Price_INR`  
- Handled missing review ratings and text  
- Created derived metrics:
  - **AOV (Average Order Value)**  
  - **Revenue_per_Order**  
  - **Delivery_Success_Rate**

---

## 📊 Exploratory Data Analysis (EDA)

All analysis is documented in:  
`notebooks/analysis.ipynb`

### 🔹 1. Sales & Revenue Analysis
- Total Revenue  
- Total Orders  
- Units Sold  
- Average Order Value (AOV)  
- Daily & Monthly revenue trends  

### 🔹 2. Category Performance
- Revenue by product category  
- Quantity sold by category  
- **Pareto Analysis:** Top 4 categories ≈ 80% of revenue  
- Identification of high- and low-performing segments  

### 🔹 3. Product-Level Insights
- Top 10 best-selling products  
- Bottom 10 underperforming products  
- Price vs rating relationships  
- High-volume but low-rated product clusters  

### 🔹 4. Payment Method Analysis
- Revenue contribution by payment method  
- COD vs prepaid comparison  
- Return and cancellation behavior by payment type  

### 🔹 5. Delivery & Operations Analysis
- Delivered vs returned orders  
- Category-wise return rates  
- State-wise delivery performance  
- Delivery delays vs customer ratings  

### 🔹 6. Customer Review & Rating Analysis
- Rating distribution  
- Highest and lowest-rated products  
- Basic text analysis on reviews  
- Impact of delivery issues on ratings  

---

## 📊 Tableau Dashboard Details

📁 **File Location:**  
`reports/tableau/AmazonSalesDashboard.twb`

### Dashboard Includes:
1. KPI – Total Revenue  
2. KPI – Total Orders  
3. KPI – Units Sold  
4. KPI – Average Order Value (AOV)  
5. Revenue Trend (Line Chart)  
6. Category Sales Distribution  
7. Pareto Analysis (Category-wise)  
8. Payment Method Revenue  
9. Delivery Status Breakdown  
10. Rating Distribution  

📸 **Dashboard Image:**  
`reports/tableau/AmazonSalesDashboard.png`

---

## 🧰 Tools & Technologies Used

### Languages
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)  
- **SQL**  
- **Tableau Calculated Fields**

### Tools
- Jupyter Notebook  
- Tableau  
- Excel  
- Git & GitHub  

### Scripts
- `get_data.py` → Loads or fetches the dataset into the local environment  

---

## 📈 Summary of Key Insights

- Revenue remained **stable across the analysis period**  
- Product categories showed **balanced revenue contribution**  
- **Top 4 categories generated ~80% of total revenue**  
- COD orders had **higher return and cancellation rates**  
- Delivery delays strongly correlated with **lower customer ratings**  
- Highly rated products showed **~1.8× higher repeat purchase potential**  
- Certain categories exhibited **disproportionately high return rates**

---

## ▶️ How to Run This Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/amazon-sales-analytics.git
cd amazon-sales-analytics
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Add Dataset
Place the CSV file in:
```
data/raw/
```

### 4️⃣ Run the Analysis
```bash
jupyter lab
```
Open and run:
```
notebooks/analysis.ipynb
```

---

## 🤝 Connect With Me

**LinkedIn:**  
https://www.linkedin.com/in/shavilya-rajput-96741
