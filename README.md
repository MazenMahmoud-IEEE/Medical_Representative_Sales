# Medical Representative Sales Analysis 

## Team Members
- AbdelRahman AbdelHalem Helal Ahmed
- Mazen Mohamed Elsayed Elsafty
- Mazen Mahmoud Shaban Mohamed
- Rashad Mohamed AboElmkaram Shehab
- Mazen Mohamed Mohamed Ahmed
- Karim Ahmed Farhat Eid

## Supervisor
Eng. Sherif Said

## Track
IBM Data Science (ALX1_AIS3_S1e)

## Organization
Digital Egypt Pioneers Initiative

---

## Abstract
Medical representatives play a vital role in the pharmaceutical industry by bridging the gap between pharmaceutical companies and healthcare professionals. This project focuses on analyzing factors influencing doctors' prescribing behaviors and developing a supervised machine learning model to predict the likelihood of doctors prescribing drugs from a local pharmaceutical company. Using the AdaBoost algorithm, the model achieved an accuracy of **84%** and an **F1-score of 88%**. Key insights on factors such as doctor age, specialty, and location were also analyzed, providing useful guidance for optimizing sales strategies.

---

## 1. Introduction

### 1.1 Background
Medical representatives promote and sell pharmaceutical products to healthcare professionals in a competitive market with similar alternatives. This project leverages machine learning to predict doctors' prescribing behaviors based on their profiles, aiming to help companies optimize representatives' strategies.

### 1.2 Problem Statement
Medical representatives face a challenge in persuading doctors to prescribe their company’s drugs when alternatives are available. This project addresses the primary issue of predicting whether a doctor, based on specific features, will prescribe a drug from the local company.

### 1.3 Objectives
1. To determine the factors influencing doctors’ prescribing behaviors.
2. To analyze relationships between variables such as doctor age, specialty, and location.
3. To build a supervised machine learning model to predict if a doctor will prescribe a local company’s generic drugs.

---

## 2. Literature Review
Studies indicate that a doctor’s specialty, experience, and location significantly impact prescribing habits. Various machine learning algorithms have been applied to similar problems in healthcare, with AdaBoost being particularly effective for imbalanced classification tasks.

---

## 3. Methodology

### 3.1 Data Collection
The dataset was sourced from two tables: `medicine_table` and `doctor_table`, containing information about doctors, their specialties, locations, and prescribing behaviors.

### 3.2 Data Preprocessing
1. **Handling Missing Values**: Missing data was imputed or dropped as needed.
2. **Feature Encoding**: Categorical features (e.g., specialty, location) were encoded using one-hot and label encoding.
3. **Normalization**: Continuous variables (e.g., age, experience) were normalized with `MinMaxScaler`.
4. **Skewness Check**: Checked skewness; it was acceptable, so no further transformation was applied.

---

## 4. Exploratory Data Analysis (EDA)

### 4.1 Key Visualizations and Insights
1. **Correlation Heatmap**: Showed strong correlations between doctor class and examination price with prescribing behavior.
2. **Bar Charts**:
   - **Specialties**: General Practitioners (GPs) and Chest specialists were more likely to prescribe local company drugs.
   - **Class Distribution**: Class B doctors were the most frequent prescribers.
   - **Drug Price**: Drugs priced at 50, 100, 120, or 150 were most frequently prescribed by local doctors.
   - **Workplace**: Clinic doctors were more likely to prescribe local company drugs, while hospital doctors were neutral.
3. **Box Plots**:
   - **Price**: Fairly consistent, with a median of 35 and a range of 20 to 45.
   - **Examination Price**: Median around 100 with a range of 50 to 200, showing a consistent pricing structure.

### 4.2 Feature Importance
The most important features of the AdaBoost model:
- **Doctor’s Class**: The most influential factor.
- **Examination Price**: Doctors with lower examination prices were more likely to prescribe local company products.

---

## 5. Model Development

### 5.1 Model Selection
Various machine learning models were tested, including Decision Trees, Random Forests, and Support Vector Machines. AdaBoost was selected for its superior performance.

### 5.2 Model Training
Data was split in an 80:20 ratio for training and testing. Hyperparameter tuning was done through grid search, and metrics like accuracy and F1-score were used for evaluation.

### 5.3 Model Performance
- **Accuracy**: 84.6%
- **F1-Score**: 88.2%

---

## 6. Streamlit Deployment
- We have developed a streamlit app for user usage 
- App link : https://medical-representative-sales.streamlit.app/

---

## 7. Conclusion
The project successfully applied supervised machine learning to predict doctors' prescribing behaviors. Analyzing features such as class, specialty, and examination price led to an AdaBoost model with an accuracy of **84.6%** and an **F1-score of 88.2%**. These results offer pharmaceutical companies insights for more efficient marketing strategies, ultimately saving resources and improving targeting.

---

## 8. Future Work
1. **Model Improvement**: Further tuning of the AdaBoost model and exploring advanced algorithms.
2. **Expanded Dataset**: Including more doctors and additional features to improve robustness.
3. **Real-Time Recommendations**: Developing a real-time recommendation system for medical representatives.

---

## 9. References
- [Scikit-learn documentation](https://scikit-learn.org/)

---





---
