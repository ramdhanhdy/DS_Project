## DataFrame Overview
Dataset with 2240 observations and 29 columns

- **Numerical** columns:

	| column_name | type | min | max | number NaN | number unique | sample unique |
	| :-------------  | :-------------  | :-------------  | :-------------  | :-------------  | :-------------  |
	| ID | int64 | 0 | 11191 | 0 | 2240 | [5524 2174 4141 6182 5324] |
	| Year_Birth | int64 | 1893 | 1996 | 0 | 59 | [1957 1954 1965 1984 1981] |
	| Income | float64 | 1730.0 | 666666.0 | 24 | 1974 | [58138. 46344. 71613. 26646. 58293.] |
	| Kidhome | int64 | 0 | 2 | 0 | 3 | [0 1 2] |
	| Teenhome | int64 | 0 | 2 | 0 | 3 | [0 1 2] |
	| Recency | int64 | 0 | 99 | 0 | 100 | [58 38 26 94 16] |
	| MntWines | int64 | 0 | 1493 | 0 | 776 | [635  11 426 173 520] |
	| MntFruits | int64 | 0 | 199 | 0 | 158 | [88  1 49  4 43] |
	| MntMeatProducts | int64 | 0 | 1725 | 0 | 558 | [546   6 127  20 118] |
	| MntFishProducts | int64 | 0 | 259 | 0 | 182 | [172   2 111  10  46] |
	| MntSweetProducts | int64 | 0 | 263 | 0 | 177 | [88  1 21  3 27] |
	| MntGoldProds | int64 | 0 | 362 | 0 | 213 | [88  6 42  5 15] |
	| NumDealsPurchases | int64 | 0 | 15 | 0 | 15 | [3 2 1 5 4] |
	| NumWebPurchases | int64 | 0 | 27 | 0 | 15 | [8 1 2 5 6] |
	| NumCatalogPurchases | int64 | 0 | 28 | 0 | 14 | [10  1  2  0  3] |
	| NumStorePurchases | int64 | 0 | 13 | 0 | 14 | [ 4  2 10  6  7] |
	| NumWebVisitsMonth | int64 | 0 | 20 | 0 | 16 | [7 5 4 6 8] |
	| Z_CostContact | int64 | 3 | 3 | 0 | 1 | [3] |
	| Z_Revenue | int64 | 11 | 11 | 0 | 1 | [11] |


- **Categorical** columns:

	| column_name | type | min | max | number NaN | number unique | sample unique |
	| :-------------  | :-------------  | :-------------  | :-------------  | :-------------  | :-------------  |
	| Education | object | 2n Cycle | PhD | 0 | 5 | ['Graduation' 'PhD' 'Master' 'Basic' '2n Cycle'] |
	| Marital_Status | object | Absurd | YOLO | 0 | 8 | ['Single' 'Together' 'Married' 'Divorced' 'Widow'] |
	| Dt_Customer | object | 01-01-2013 | 31-12-2013 | 0 | 663 | ['04-09-2012' '08-03-2014' '21-08-2013' '10-02-2014' '19-01-2014'] |


- **Dummy** columns:

	| column_name | type | min | max | number NaN | number unique | sample unique |
	| :-------------  | :-------------  | :-------------  | :-------------  | :-------------  | :-------------  |
	| AcceptedCmp3 | int64 | 0 | 1 | 0 | 2 | [0 1] |
	| AcceptedCmp4 | int64 | 0 | 1 | 0 | 2 | [0 1] |
	| AcceptedCmp5 | int64 | 0 | 1 | 0 | 2 | [0 1] |
	| AcceptedCmp1 | int64 | 0 | 1 | 0 | 2 | [0 1] |
	| AcceptedCmp2 | int64 | 0 | 1 | 0 | 2 | [0 1] |
	| Complain | int64 | 0 | 1 | 0 | 2 | [0 1] |
	| Response | int64 | 0 | 1 | 0 | 2 | [1 0] |


