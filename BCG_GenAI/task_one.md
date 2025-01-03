## Task 1: Data Extraction and Initial Analysis

### Objective
To manually extract key financial data for the last three fiscal years from the 10-K filings of Microsoft, Tesla, and Apple. Following the data collection, perform an initial analysis focusing on trends and insights that could inform the development of an AI-powered financial chatbot.

### Techniques for extracting key financial data from 10-Ks
10-K reports are comprehensive annual reports filed with the SEC by publicly traded companies. They provide a detailed account of a company's financial performance, including audited financial statements, management's discussion and analysis (MD&A), and disclosures about market risk, controls, and legal proceedings.

Key sections to focus on for financial data extraction:

Income statement: This section provides information about the company's revenue, costs, and expenses over a specific period of time.
Key data points: Total revenue, cost of goods sold (COGS), operating expenses, and net income.
Extraction technique: Look for the income statement summary, typically in the early pages of the reports. Pay attention to year-over-year changes.
Balance sheet: This section outlines the company’s assets, liabilities, and the shareholders’ equity at a specific point in time.
Key data points: Current assets, long-term assets, current liabilities, long-term liabilities, and total shareholders’ equity.
Extraction technique: Focus on the balance sheet summary. Compare assets against liabilities to understand the company’s financial health and note any large changes in assets or liabilities.
Cash flow statement: This shows how changes to the balance sheet and income impact cash and cash equivalents.
Key data points: Cash from operating activities, investing activities, and financing activities.
Extraction technique: Analyze the cash flow statement to understand how the company generates and spends its cash. This can provide insights into a company's liquidity.
 
Effective techniques for data extraction:

Manual extraction: Start by manually reviewing the documents to understand their layout and where key information is typically found.
Highlight and annotate: Use digital tools to highlight and annotate key figures and notes for easy reference.
Excel and spreadsheet tools: For quantitative data, using Excel or similar spreadsheet tools can be effective. You can input key figures into a spreadsheet for analysis and comparison.
Automated extraction tools: For more advanced users, tools such as Python (in particular, libraries such as Beautiful Soup or Pandas) can automate the extraction of data from these documents, especially if they are available in digital formats.
By understanding the structure of 10-K reports and mastering these extraction techniques, you can efficiently gather the necessary financial data for analysis and further application in AI-driven tools.

### Task instructions
Your task is to manually extract key financial data for the last three fiscal years from the 10-K filings of Microsoft, Tesla, and Apple. Following the data collection, you will use Python to analyze this data, focusing on trends and insights that could inform the development of an AI-powered financial chatbot.

Step 1: Data extraction
Navigate to the SEC's EDGAR database:

Microsoft
Tesla
Apple
Manual extraction:

For each company, find the 10-K filings for the last three fiscal years.
Extract the following financial figures: Total Revenue, Net Income, Total Assets, Total Liabilities, and Cash Flow from Operating Activities.
Organize Your Data:

Compile the extracted data into an Excel spreadsheet for easy reference during your Python analysis.