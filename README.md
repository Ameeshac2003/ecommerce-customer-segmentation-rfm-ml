# E-Commerce Customer Segmentation using RFM Analysis & Machine Learning

##  Project Overview
This project focuses on **customer segmentation for an e-commerce business** using
transactional data. The goal is to identify different customer groups such as
high-value customers, loyal customers, and low-engagement customers.

Customer behavior is analyzed using **RFM (Recency, Frequency, Monetary) analysis**,
dimensionality reduction techniques, and multiple clustering algorithms to compare
segmentation performance.

The insights are visualized using **Streamlit** and **Tableau**.

---

## Project Structure

The project is organized into multiple folders for clarity and easy navigation.
The notebooks folder contains Jupyter notebooks used for data exploration, RFM analysis, feature engineering, and machine learning modeling.
The processed_data folder stores cleaned and clustered datasets generated after preprocessing and modeling.
The report folder includes the final project report in PDF format.
The streamlit_app folder contains all files related to the Streamlit web application used for interactive visualization.
The tableau folder holds Tableau dashboards or screenshots created for business-level insights.
The README.md file provides complete documentation of the project.

---

##  Dataset
- **Dataset Name:** Online Retail Dataset  
- **Source:** Kaggle  
- **Description:**  
  Transaction-level data containing invoice number, customer ID,
  product details, quantity, unit price, and invoice date.

> Note: Only **processed and clustered datasets** are included in this repository.

---

##  Data Preprocessing
- Removed missing and invalid values
- Handled negative quantities and cancelled invoices
- Created customer-level features
- Calculated **RFM metrics**
- Scaled features for clustering
- Applied **PCA** for dimensionality reduction

---

##  Feature Engineering (RFM)
- **Recency:** Days since last purchase  
- **Frequency:** Number of transactions  
- **Monetary:** Total spending amount  

These features were used as the base for clustering and analysis.

---

##  Machine Learning & Analytics Techniques
The following techniques and models were implemented and compared:

- **RFM Analysis**
- **K-Means Clustering**
- **Hierarchical Clustering**
- **DBSCAN Clustering**
- **PCA (Principal Component Analysis)**
- **Decision Tree** (to interpret customer segments)

Cluster performance and customer distributions were analyzed across models.

---

##  Visualization & Tools
- **Streamlit**
  - Interactive customer segmentation dashboard
  - Cluster exploration and insights

- **Tableau**
  - Customer segment distribution
  - RFM score visualization
  - Business-friendly dashboards

---

##  Tools & Technologies Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Streamlit  
- Tableau  
- Jupyter Notebook  

---

##  Business Insights
- Identified high-value and loyal customer segments
- Detected low-engagement customers for re-targeting
- Compared clustering algorithms for better segmentation
- Provided actionable insights for marketing strategies

---

##  Conclusion
This project demonstrates how **RFM analysis combined with machine learning**
can effectively segment customers and support data-driven business decisions.
The integration of **Streamlit and Tableau** enhances interpretability and usability
for non-technical stakeholders.

---

##  Author
**Ameesha C**
