# Price Optimization Project for Company ABC

This repository contains all the materials related to the Price Optimization project for Company ABC as part of Amazon Data Science Challenge. The main goal of the project is to determine the optimum price for the company's product to increase revenue.

## Project Description

Company ABC performed a pricing experiment where users were divided into two groups: Group A (66% of users) were offered a lower price, and Group B (33% of users) were offered a higher price. The purpose of this project is to analyze the experiment data and provide actionable insights.

## Repository Structure

```
.
├── data                    # Folder for raw and processed data
├── notebooks               # Jupyter notebooks for analysis
├── reports                 # Generated analysis reports and plots
├── src                     # Source code for use in this project
├── README.md               # The top-level README for developers using this project
└── .gitignore              # Specifies intentionally untracked files to ignore when using Git
```

## Data Description

The project uses two datasets: `test_results` and `user_table`.

`test_results` contains data about user behavior on the website, the source of traffic, the device used, the price shown to the user, and whether they bought the product.

`user_table` contains the geographic information about the user, including city and country.

## Project Steps

1. **Data Cleaning and Preprocessing**
2. **Exploratory Data Analysis (EDA)**
3. **Hypothesis Testing and Confidence Interval Estimation**
4. **Price Optimization**
5. **User Behavior Analysis**
6. **Test Duration Optimization**
7. **Actionable Insights**

Each step has its own dedicated Jupyter notebook, located in the `notebooks` directory.

## Usage

1. Clone the repository: `git clone https://github.com/yourusername/price-optimization.git`
2. Navigate into the directory: `cd price-optimization`
3. Install dependencies: `pip install -r requirements.txt`
4. Open Jupyter Notebook: `jupyter notebook`

## Dependencies

The project requires the following Python libraries: pandas, numpy, scipy, matplotlib, seaborn. A complete list of dependencies can be found in the `requirements.txt` file.

## Authors

Muhammad Ramdhan Hidayat

## License

This project is licensed under the MIT License. See `LICENSE` for more information.


