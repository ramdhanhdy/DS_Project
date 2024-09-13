# Feature Engineering

Now it’s time for feature engineering
Well done for your analysis on the influence of price sensitivity relative to churn!

Estelle reviewed your work with the AD and Estelle has come up with an idea to enrich the dataset when trying to predict churn:

“I think that the difference between off-peak prices in December and January the preceding year could be a significant feature when predicting churn”

As the Data Scientist on the team, you need to investigate this question. So, in this task you’ll be responsible for completing feature engineering for the dataset.

Task: Build from the difference between off-peak prices in December and January the preceding year to generate new features that could be relevant to predict churn.

# Data Profile

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 14606 entries, 0 to 14605
Data columns (total 44 columns):
 #   Column                          Non-Null Count  Dtype         
---  ------                          --------------  -----         
 0   id                              14606 non-null  object        
 1   channel_sales                   14606 non-null  object        
 2   cons_12m                        14606 non-null  int64         
 3   cons_gas_12m                    14606 non-null  int64         
 4   cons_last_month                 14606 non-null  int64         
 5   date_activ                      14606 non-null  datetime64[ns]
 6   date_end                        14606 non-null  datetime64[ns]
 7   date_modif_prod                 14606 non-null  datetime64[ns]
 8   date_renewal                    14606 non-null  datetime64[ns]
 9   forecast_cons_12m               14606 non-null  float64       
 10  forecast_cons_year              14606 non-null  int64         
 11  forecast_discount_energy        14606 non-null  float64       
 12  forecast_meter_rent_12m         14606 non-null  float64       
 13  forecast_price_energy_off_peak  14606 non-null  float64       
 14  forecast_price_energy_peak      14606 non-null  float64       
 15  forecast_price_pow_off_peak     14606 non-null  float64       
 16  has_gas                         14606 non-null  object        
 17  imp_cons                        14606 non-null  float64       
 18  margin_gross_pow_ele            14606 non-null  float64       
 19  margin_net_pow_ele              14606 non-null  float64       
 20  nb_prod_act                     14606 non-null  int64         
 21  net_margin                      14606 non-null  float64       
 22  num_years_antig                 14606 non-null  int64         
 23  origin_up                       14606 non-null  object        
 24  pow_max                         14606 non-null  float64       
 25  var_year_price_off_peak_var     14606 non-null  float64       
 26  var_year_price_peak_var         14606 non-null  float64       
 27  var_year_price_mid_peak_var     14606 non-null  float64       
 28  var_year_price_off_peak_fix     14606 non-null  float64       
 29  var_year_price_peak_fix         14606 non-null  float64       
 30  var_year_price_mid_peak_fix     14606 non-null  float64       
 31  var_year_price_off_peak         14606 non-null  float64       
 32  var_year_price_peak             14606 non-null  float64       
 33  var_year_price_mid_peak         14606 non-null  float64       
 34  var_6m_price_off_peak_var       14606 non-null  float64       
 35  var_6m_price_peak_var           14606 non-null  float64       
 36  var_6m_price_mid_peak_var       14606 non-null  float64       
 37  var_6m_price_off_peak_fix       14606 non-null  float64       
 38  var_6m_price_peak_fix           14606 non-null  float64       
 39  var_6m_price_mid_peak_fix       14606 non-null  float64       
 40  var_6m_price_off_peak           14606 non-null  float64       
 41  var_6m_price_peak               14606 non-null  float64       
 42  var_6m_price_mid_peak           14606 non-null  float64       
 43  churn                           14606 non-null  int64         
dtypes: datetime64[ns](4), float64(29), int64(7), object(4)
memory usage: 4.9+ MB

