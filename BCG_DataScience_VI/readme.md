# Customer Churn Prediction for PowerCo: Identifying Price-Sensitive Customers

## 1. Overview/Introduction

PowerCo, a major energy provider, faces the challenge of customer churn, particularly among price-sensitive customers. This project aims to develop a machine learning model to predict customer churn and identify the key factors driving it, with a specific focus on price sensitivity. By understanding these drivers, PowerCo can implement targeted retention strategies to reduce churn and improve customer loyalty.

This project follows a structured approach, encompassing:

*   **Exploratory Data Analysis (EDA):**  Understanding the data, identifying patterns, and gaining initial insights into potential churn drivers.
*   **Feature Engineering:** Creating relevant features from the raw data to improve model performance.
*   **Model Building and Evaluation:** Developing and evaluating machine learning models to predict customer churn, with a focus on recall to minimize false negatives (missed churners).

## 2. Notebook Summaries

### Task2\_EDA.ipynb - Exploratory Data Analysis

This notebook focuses on exploring and understanding the customer and price datasets. Key steps and findings include:

*   **Data Loading and Cleaning:** Loading the `client_data.csv` and `price_data.csv` datasets and performing initial data cleaning, such as handling missing values and data type conversions.
*   **Exploratory Data Analysis (EDA):**
    *   **Churn Rate Analysis:**  Observed a significant class imbalance in the target variable 'churn', with a low churn rate.
    *   **Customer Feature Distributions:** Examined the distributions of key customer features like consumption (`cons_12m`, `cons_gas_12m`), contract duration (`months_to_end`, `months_renewal`), and price sensitivity indicators.
    *   **Price Feature Analysis:** Analyzed price features, including price types (variable and fixed) and time periods (off-peak, peak, mid-peak), and explored price trends and volatility.
    *   **Visualizations:** Created various visualizations, including histograms, box plots, and summary tables, to understand feature distributions and relationships. For example, summary tables were generated to compare client and price data characteristics.
*   **Key Takeaways:** Initial EDA revealed class imbalance in churn, provided insights into feature distributions, and suggested potential relationships between price features and churn behavior.

### Task3\_feature\_engineering.ipynb - Feature Engineering

This notebook focuses on creating new features from the existing data to improve the predictive power of machine learning models. Key feature engineering steps include:

*   **Off-peak Price Difference (December vs. January):** Calculated the difference in off-peak variable and fixed prices between December and January to capture seasonal price changes, using the function `calculate_offpeak_diff(price_df)`.
*   **Mean and Maximum Monthly Price Differences:** Computed mean price differences between off-peak, peak, and mid-peak periods (variable and fixed prices) and determined the maximum monthly price differences for each period combination to identify significant price fluctuations, using the function `calculate_mean_max_diff(price_df)`.
*   **Tenure Calculation:** Calculated customer tenure in years from the difference between `date_end` and `date_activ`, using the function `calculate_tenure(df)`.
*   **Channel Sales Categorization:** Categorized 'channel\_sales' values with counts below a threshold into 'OTHER' to group low-frequency channels, using the function `categorize_low_counts(df, column_name, threshold=11, other_label='OTHER')`.
*   **Dummy Variables for Categorical Features:** Created dummy variables (one-hot encoding) for 'channel\_sales' and 'origin\_up' columns, dropping the most common category and dummy variables for very low count categories to avoid multicollinearity and reduce dimensionality, using the function `create_dummy_variables(df, column_name, prefix, low_count_categories=None)`.
*   **Log Transformation of Numerical Features:** Applied log base 10 transformation to skewed numerical features (`cons_12m`, `cons_gas_12m`, `cons_last_month`, `forecast_cons_12m`, `forecast_cons_year`, `forecast_meter_rent_12m`, `imp_cons`) to normalize data and reduce outlier impact, using the function `apply_log10_transformation(df, columns)`.
*   **Feature Selection - Correlation Analysis:** Analyzed the correlation matrix to identify and reduce highly correlated features (threshold > 0.8), removing one feature from each highly correlated pair to reduce dimensionality and potential multicollinearity, using the function `reduce_correlated_features(df, high_corr_pairs, correlation_threshold=0.8)`.

### Task4\_Modeling.ipynb - Model Building and Evaluation

This notebook focuses on building and evaluating machine learning models to predict customer churn. Key steps and findings include:

*   **Model Selection:** Trained and evaluated four models: Logistic Regression, Decision Tree, Random Forest, and XGBoost.
*   **Initial Model Evaluation:** Used cross-validation and ROC AUC as the primary evaluation metric due to class imbalance. Initial results showed high accuracy but low recall across all models, indicating poor identification of churn cases. XGBoost performed best among the initial models.
*   **Addressing Class Imbalance and Overfitting:** Implemented SMOTE to address class imbalance and used learning curves to diagnose and mitigate overfitting.
*   **Hyperparameter Tuning (XGBoost):** Performed hyperparameter tuning for XGBoost using Bayesian optimization (Hyperopt) to maximize recall, which is crucial for minimizing false negatives in churn prediction.
*   **Optimized XGBoost Model:** Evaluated the optimized XGBoost model, which showed significantly improved recall (62%) compared to the baseline models, at the cost of slightly reduced precision and overall accuracy. The optimized model was deemed more effective for churn prediction due to its ability to identify a larger proportion of churners.
*   **Feature Importance Analysis:** Analyzed feature importance from the optimized XGBoost model to identify key drivers of churn. Found that 'origin\_up\_lxidpiddsbxsbosboudacockeimpuepw' (contract origin/type), price sensitivity features (e.g., 'offpeak\_diff\_dec\_january\_power'), and customer tenure ('tenure') were among the most important predictors.
*   **Conclusion:** The optimized XGBoost model is effective for predicting churn, with price sensitivity being a significant driver, along with contract characteristics, customer tenure, and service usage patterns.

## 3. Conclusion

This project successfully developed a machine learning model to predict customer churn for PowerCo, with a focus on identifying price-sensitive customers. The optimized XGBoost model demonstrated a significant improvement in recall, enabling better identification of customers at risk of churning. Feature importance analysis confirmed that price sensitivity is indeed a crucial factor influencing churn, but it is intertwined with other factors such as contract origin/type, customer tenure, and service usage patterns.

While the optimized model sacrifices some overall accuracy for improved recall, this trade-off is beneficial for PowerCo, as it prioritizes minimizing missed churn cases and allows for more effective implementation of retention strategies.

## 4. Recommendations for PowerCo

Based on the findings of this project, the following recommendations are made to PowerCo:

*   **Focus on Targeted Retention Strategies for Price-Sensitive Customers:** Develop specific retention programs tailored to customers identified as price-sensitive. This could include offering dynamic pricing plans, discounts, or value-added services.
*   **Consider Customized Pricing Plans or Discounts:** Proactively offer customized pricing plans or discounts to customers identified as high-churn risk, especially those exhibiting price sensitivity.
*   **Pay Attention to Contract Types and Customer Origin:** Recognize 'origin\_up\_lxidpiddsbxsbosboudacockeimpuepw' (contract origin/type) as a strong predictor of churn and investigate further to understand why certain contract types or customer origins are more prone to churn. Tailor strategies accordingly.
*   **Monitor Customer Tenure and Engagement:** Continuously monitor customer tenure and engagement metrics to identify customers who may be at risk of churning early in their lifecycle. Implement proactive engagement strategies for these customers.
*   **Further Investigate Sales Channels:** Analyze the impact of different sales channels ('channel\_sales') on churn likelihood and optimize channel strategies to improve customer retention.

By implementing these recommendations, PowerCo can leverage the churn prediction model to proactively address customer churn, particularly among price-sensitive segments, and enhance customer retention efforts.

## 5. File Structure

```
d:/DS_Project/BCG_DataScience_VI/
├── data/
│   ├── clean_data_after_eda.csv
│   ├── client_data.csv
│   ├── Data Description.pdf
│   ├── data_for_predictions.csv
│   └── price_data.csv
├── images/
│   ├── client_df_summary_table.html
│   ├── price_df_summary_table.html
│   └── summary table.jpeg
├── readme.md
├── Task2_EDA.ipynb
├── Task3_feature_engineering.ipynb
├── Task4_Modeling.ipynb
├── data_summary.py
└── utils.py
```

## 6. Dependencies

*   pandas
*   numpy
*   matplotlib
*   seaborn
*   scikit-learn (sklearn)
*   imblearn
*   xgboost
*   hyperopt
