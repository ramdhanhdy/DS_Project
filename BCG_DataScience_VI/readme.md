# PowerCo Customer Churn Analysis

## Project Overview
This repository contains the data science project files for analyzing customer churn at PowerCo, a major gas and electricity utility company. The goal of this project is to investigate the key factors driving customer churn and identify at-risk customers to help PowerCo reduce churn rates, with a specific focus on understanding the impact of price sensitivity on customer churn.

## Data
The data used in this project includes three datasets provided by PowerCo:
- Historical customer data: Customer information such as usage, sign up date, forecasted usage, etc.
- Historical pricing data: Variable and fixed pricing data
- Churn indicator: Whether each customer has churned or not

## Methodology
The project follows a structured data science approach:

1. Exploratory Data Analysis (EDA)
   - Analyzing data types of each column
   - Generating descriptive statistics
   - Visualizing distributions of relevant columns

2. Feature Engineering
   - Removing irrelevant or redundant columns
   - Creating new features from existing columns
   - Combining related columns to create more meaningful features
   - Merging datasets based on a common key column

3. Predictive Modeling
   - Training a Random Forest classifier to predict customer churn
   - Evaluating the model's performance using appropriate evaluation metrics

4. Findings and Recommendations
   - Summarizing key insights from the analysis
   - Presenting results in a clear, non-technical manner
   - Relating findings to PowerCo's business context
   - Providing actionable recommendations based on the insights gained

## Files
- `data/`: Contains the raw datasets provided by PowerCo
- `notebooks/`: Contains Jupyter notebooks for data exploration, analysis, feature engineering, and modeling
- `reports/`: Contains the executive summary slide presenting the findings and recommendations
- `requirements.txt`: Lists the required Python libraries and dependencies

## Usage
1. Clone the repository: `git clone https://github.com/username/powerco-churn-analysis.git`
2. Install the required libraries: `pip install -r requirements.txt`
3. Navigate to the `notebooks/` directory and run the Jupyter notebooks for data exploration, analysis, feature engineering, and modeling


## Acknowledgments
- PowerCo for providing the data and business context
- BCG GAMMA for the project guidance and methodology

## License
This project is licensed under the [MIT License](LICENSE).