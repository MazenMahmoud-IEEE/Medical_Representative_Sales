# Medical Representative Sales Prediction

This project is a graduation assignment for the DEPI program, aiming to predict sales success for medical representatives. By analyzing various features such as sales history, representative details, and customer insights, we implemented machine learning models to optimize sales strategies and enhance decision-making processes.

## Project Overview

The Medical Representative Sales project leverages multiple machine learning algorithms to assess and predict sales success. The project's objective is to analyze representative characteristics, product information, and customer demographics to understand the factors that drive successful sales and to provide recommendations for future strategy.

### Project Flow and Mechanism

1. **Data Loading and Exploration**: 
   - Data is initially loaded and explored to identify missing values, outliers, and feature distributions.
   - Essential exploratory data analysis (EDA) techniques are employed to gain insights into feature relevance and correlation with the target variable.

2. **Data Preprocessing**:
   - **Normalization**: Numerical features are normalized using the `MinMaxScaler` from `sklearn.preprocessing`, scaling all numeric values between 0 and 1 to ensure fair model training.
   - **Categorical Encoding**: The `OneHotEncoder` is applied to categorical data, with `sparse_output=False` and `handle_unknown='ignore'`, creating dummy variables for categorical features to make them usable by the machine learning models.

3. **Model Training and Selection**:
   - Various machine learning algorithms are tested to determine the best-performing model:
     - **Decision Tree Classifier**: Provides a baseline understanding with interpretable tree-based structures.
     - **K-Nearest Neighbors (KNN)**: Considers proximity in feature space to predict sales outcomes.
     - **Random Forest Classifier**: A robust ensemble method that improves accuracy through multiple decision trees.
     - **XGBoost Classifier**: A gradient-boosted model known for high accuracy and efficiency.
     - **AdaBoost Classifier**: Combines multiple weak learners to form a strong predictive model.
     - **Support Vector Machine (SVM)**: Finds an optimal hyperplane for classification, effective with high-dimensional data.
   - The models are evaluated in a loop to determine the highest-performing approach based on chosen metrics.

4. **Evaluation Metrics**:
   - The model performance is assessed using the following metrics:
     - **Accuracy Score**: Provides a simple measurement of model correctness across training and testing datasets.
     - **F1 Score**: Balances precision and recall, providing insight into the quality of the model’s positive predictions.
     - **F-Beta Score**: A custom metric with `beta=0.5` is used to give more weight to precision, which is crucial in sales predictions.

5. **Results and Model Insights**:
   - Models are compared based on F1 and accuracy scores, with further tuning and analysis to refine model selection.
   - Insights are drawn from model results to identify factors that contribute to successful medical sales outcomes, guiding future strategies.

## Results

After training and evaluating various models, we identified the **XGBoost Classifier** and **Random Forest Classifier** as top performers in terms of accuracy and F1 scores. These models demonstrated superior predictive power in classifying successful sales efforts, with F1 scores indicating a balanced performance in terms of precision and recall.

## Getting Started

### Prerequisites

To run this project locally, you will need the following Python packages:
- `numpy`
- `pandas`
- `scikit-learn`
- `xgboost`

Install the required libraries using:
```bash
pip install numpy pandas scikit-learn xgboost
```

### Running the Project

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Medical-Representative-Sales
   ```
3. Run the notebook or Python script to execute the model training and evaluation.

## Conclusion

This project successfully highlights the factors affecting sales success in the medical representative field using machine learning. By comparing multiple models and evaluating based on precision-oriented metrics, we provide a data-driven solution to enhance sales strategy.
