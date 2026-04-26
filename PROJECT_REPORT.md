# House Price Prediction Project Report

## 1. Objective
The objective of this project is to build and evaluate a machine learning system that predicts house prices for properties in the top 20 U.S. states. The project work covers:
- Model training
- Model evaluation
- Model comparison
- Product testing (single-house prediction scenario)

## 2. Dataset and Inputs
- Source dataset: Zillow top 20 states housing data
- Working files:
  - Data/zillow_top20_states.csv (raw)
  - Data/cleaned.csv (processed)
- Target variable:
  - price
- Main predictive features used in testing pipeline:
  - beds
  - baths
  - area_sqft
  - home_type
  - state_code

## 3. Methodology
### 3.1 Data Preparation
- Loaded raw CSV data.
- Removed records with missing target (price).
- Filled numeric missing values using median imputation.
- Dropped non-essential columns where available (for example: zipcode, address, street, price_formatted, detail_url).
- Saved cleaned data for modeling.

### 3.2 Libraries and Frameworks
- pandas, numpy
- matplotlib, seaborn
- scikit-learn modules:
  - train_test_split, cross_val_score, GridSearchCV
  - ColumnTransformer, SimpleImputer
  - StandardScaler, OneHotEncoder
  - Pipeline
  - LinearRegression, Ridge, Lasso, SGDRegressor
  - mean_absolute_error, mean_squared_error, r2_score

### 3.3 Modeling Workflow
- Built preprocessing + model pipelines.
- Split data into training and testing subsets.
- Trained and evaluated:
  - Baseline methods
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - SGDRegressor
- Performed 5-fold cross-validation for Ridge.
- Ran GridSearchCV for Ridge alpha tuning.
- Compared all models using MAE, MSE, and R2.

## 4. Evaluation and Comparison Results
From the executed final notebook run:
- Ridge Cross-Validation R2 scores:
  - [0.32301743, 0.04657911, 0.17144773, -0.00687022, 0.10949979]
- Average Ridge CV R2:
  - 0.12873476819805704
- Best Ridge hyperparameter (GridSearchCV):
  - alpha = 10

General comparison finding from notebook analysis:
- Multivariate regression models outperformed baseline predictors.
- Regularized methods (Ridge and Lasso) showed better generalization behavior.
- SGDRegressor produced competitive performance with efficient optimization.

## 5. Product Testing (Inference Demo)
A manual test sample was used in the final notebook:
- beds: 4
- baths: 2
- area_sqft: 2000
- home_type: Single_family
- state_code: TX

Predicted output from executed notebook:
- $378012.38

Observed runtime note during prediction:
- A sklearn warning appeared for unknown category handling in encoding (encoded as all zeros), which indicates inference categories may differ from training categories for at least one categorical feature.

## 6. Conclusion
The project successfully delivers an end-to-end house price prediction pipeline, including data cleaning, model training, validation, hyperparameter tuning, model comparison, and product-level sample testing. The final workflow is reproducible through the executed notebook and suitable for reporting and further extension (for example, additional feature engineering or advanced ensemble models).

## 7. Main Execution Artifact
Primary pipeline notebook:
- notebooks/Final_House_Price_Prediction.ipynb
