# Garment Employee Productivity Prediction

## Overview

This project analyzes and predicts the productivity of garment employees using a dataset from the UCI Machine Learning Repository. The dataset contains various attributes related to garment manufacturing processes and employee productivity.

## Objective

The main objective of this project is to analyze factors affecting garment employee productivity and develop a model to predict productivity based on various features.

## Research Questions

1. In general, what factors contribute to productivity?
2. Do the factors contributing to productivity differ across different teams?
3. Are the factors consistent across quarters?
4. What are the suggestions to improve the productivity of the teams?

## Dataset

The dataset used is the "Productivity Prediction of Garment Employees" from UCI. It includes:

- 1197 instances
- 15 features including the target variable
- Features related to date, department, team, work conditions, and productivity metrics

## Project Structure

```
Productivity Prediction/
│Research Questions:
- In general, what factors contribute to productivity?
- Are the factors contributing to productivity differ accross different team?
- Are the factors consistent across quarters?
- What are the suggestions to improve the productivity of the team?
├── README.md
└── productivity_eda.ipynb
```

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Required libraries: pandas, ucimlrepo

### Installation

1. Clone this repository
2. Install required libraries:
   ```
   pip install pandas ucimlrepo jupyter
   ```

### Usage

Open and run the `productivity_eda.ipynb` notebook in Jupyter to explore the dataset and perform initial analysis.

## Data Loading and Exploration

The notebook `productivity_eda.ipynb` contains the initial data loading and exploration steps:

1. Import required libraries (pandas and ucimlrepo)
2. Fetch the dataset using `fetch_ucirepo(id=597)`
3. Load the data into a pandas DataFrame
4. Display the first few rows of the dataset
5. Print metadata and variable information

## Features

The dataset includes the following features:

- date: Date in MM-DD-YYYY format
- day: Day of the Week
- quarter: Portion of the month (divided into four quarters)
- department: Associated department
- team: Team number
- no_of_workers: Number of workers in each team
- no_of_style_change: Number of changes in product style
- targeted_productivity: Targeted productivity set by the Authority
- smv: Standard Minute Value (allocated time for a task)
- wip: Work in progress (number of unfinished items)
- over_time: Amount of overtime in minutes
- incentive: Financial incentive in BDT
- idle_time: Time when production was interrupted
- idle_men: Number of idle workers due to production interruption
- actual_productivity: Actual productivity delivered (ranges from 0-1)

## Future Work

- Perform more in-depth exploratory data analysis
- Handle missing values in the 'wip' column
- Develop predictive models for employee productivity
- Evaluate and compare different machine learning algorithms

## License

[Include appropriate license information]

## Acknowledgments

- UCI Machine Learning Repository for providing the dataset
- Original dataset creators: Abdullah Al Imran, Md Shamsur Rahim, Tanvir Ahmed
- Dataset publication: "Mining the productivity data of the garment industry" in the International Journal of Business Intelligence and Data Mining (2021)