# Power BI Sales Data Dashboard

This repository contains the materials and resources for the Power BI Sales Data Dashboard Project

## Description

This project involves the use of Power BI to analyze and visualize sales data, providing insights into various metrics and KPIs. In addition, statistical analysis was carried out using R programming language.

This repository includes a Power BI report file (.pbix), a YAML file containing the linguistic schema, datasets, and R notebook.

![Power BI Report Screenshot](images\sales_dashboard_red.png)

## Analysis Summary:

The analysis explores a monthly dataset covering the period from 2019 to 2021, examining the correlation between budget allocation and revenue fluctuations within a business context. The dataset contains essential variables, including Total Revenue, Total Quantity Sold, Total Budget, Sales Person, Supervisor, Manager, Product Name, and Product Category.

The primary objective was to understand the impact of budget adjustments on revenue over time. Correlation analyses were conducted with one-month and two-month lags to assess whether budget changes have an immediate or delayed effect on revenue. Additionally, correlations between revenue and other factors, such as salesperson performance and product categories, were examined to identify potential driving influences.

Key Insights:

1. Immediate Impact: The analysis with a one-month lag revealed an extremely weak and statistically insignificant correlation between budget changes and revenue fluctuations, suggesting that the budget's effect on revenue is unlikely to be immediate.

2. Short-Term Influence: With a two-month lag, a slight positive correlation between budget adjustments and revenue fluctuations was observed. However, the correlation remained statistically insignificant, indicating that the budget's impact diminishes over a short timeframe.

3. Seasonal Patterns: Correlation analyses between revenue and other variables highlighted seasonal patterns. Notably, a strong correlation between Total Quantity Sold and Total Revenue indicates a close relationship between sales volume and revenue.

4. Budget Allocation Strategies: Given the short-term impact of budget adjustments on revenue, businesses should prioritize agile budget allocation strategies. Timely adjustments aligned with revenue goals are crucial for achieving sustained growth.

## Contents

- `sales_data_analysis.pbix`: This is the Power BI report file. It contains the data model, queries, visualizations, and reports.
- `SalesDashboard.lsdl.yaml`: This YAML file contains the linguistic schema used in the project.
- `data/`: This directory contains the datasets used in the project. It includes:
  - `SalesData.xlsx`: The main sales data.
  - `Product.xlsx`: The product information data.
  - `Budget.xlsx`: The budget data.
  - `Photos.xlsx`: The photos data.
- `sales_analysis/`: This directory contains the R code used for statistical analysis.
  - `SalesDataAnalysis.nb.html`: This is the HTML version of the R notebook.
  - `SalesDataAnalysis.Rmd`: This is the R notebook file. It contains the R code used in the project.
- `images/`: This directory contains the images used in the project.



## Usage

To view and interact with the report:

**Dashboard**
1. Open the `sales_data_analysis.pbix` file in Power BI Desktop.
2. Use the slicers and controls in the report to filter and drill down into the data.

**R Notebook**
1. Open the `SalesDataAnalysis.Rmd` file in RStudio.
2. Run the code chunks to reproduce the analysis.




