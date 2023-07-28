library(ggplot2)
library(dplyr)
library(ggstatsplot)
library(lubridate)
library(readr)

dataset <- read_csv("~/GitHub/DS_Project/Sales Dashboard/data/processed/monthly_sales.csv", 
                    col_types = cols(Supervisor = col_factor(levels = c("Diego Araujo", "Sofia Ribeiro", "Diogo Carvalho")), 
                                    Manager = col_factor(levels = c("Gabriel Azevedo", "Victor Castro"))))
glimpse(monthly_sales)

correlation_numerical <- cor(monthly_sales[c("TotalRevenue", "TotalBudget", "TotalQuantity")])
print(correlation_numerical)


#TotalRevenue anova 
revenue_anova <- aov(TotalRevenue ~ Month + Salesperson + Supervisor + Manager, data = monthly_sales)
# Print the ANOVA result
print(summary(revenue_anova))

monthly_sales %>%
  na.omit() %>%
  aov(TotalRevenue ~ Month + Salesperson + Supervisor + Manager, data = .) %>%
  summary()

#TotalRevenue anova 
revenue_anova <- aov(TotalRevenue ~ Year + Month + Salesperson + Supervisor + Manager, data = monthly_sales)
# Print the ANOVA result
print(summary(revenue_anova))
