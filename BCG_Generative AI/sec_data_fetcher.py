import requests
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_company_cik(ticker):
    """
    Retrieve the Central Index Key (CIK) for a given stock ticker.
    
    Args:
        ticker (str): Stock ticker symbol.
    
    Returns:
        str: Zero-padded 10-digit CIK or None if not found.
    """
    url = "https://www.sec.gov/files/company_tickers.json"
    response = requests.get(url, headers={'User-Agent': 'Your Name yourname@example.com'})
    data = response.json()
    for entry in data.values():
        if entry['ticker'].upper() == ticker.upper():
            return str(entry['cik_str']).zfill(10)
    return None

def get_latest_10k_filings(cik, count=3):
    """
    Fetch the latest 'count' 10-K filings for a given CIK, excluding future filings.
    
    Args:
        cik (str): Central Index Key of the company.
        count (int): Number of latest 10-K filings to retrieve.
    
    Returns:
        List of dictionaries containing accession numbers and filing dates.
    """
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    response = requests.get(url, headers={'User-Agent': 'Your Name yourname@example.com'})
    data = response.json()
    
    recent = data.get('filings', {}).get('recent', {})
    forms = recent.get('form', [])
    accession_numbers = recent.get('accessionNumber', [])
    filing_dates = recent.get('filingDate', [])
    
    filings = []
    today = datetime.today().date()
    
    for form, accession_number, filing_date in zip(forms, accession_numbers, filing_dates):
        if form == '10-K':
            try:
                filing_date_obj = datetime.strptime(filing_date, '%Y-%m-%d').date()
            except ValueError:
                print(f"Invalid filing date format: {filing_date}")
                continue
            if filing_date_obj <= today:
                filings.append({
                    'accession_number': accession_number,
                    'filing_date': filing_date
                })
                if len(filings) == count:
                    break
    return filings

def extract_financial_data(cik, filing_year):
    """
    Extract financial data for a specific fiscal year.
    
    Args:
        cik (str): Central Index Key of the company.
        filing_year (int): Fiscal year for which to extract financial data.
    
    Returns:
        Dict containing financial metrics.
    """
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    response = requests.get(url, headers={'User-Agent': 'ramdhanhdy3@gmail.com'})
    data = response.json()

    metrics = {
        'Revenue': ['Revenues', 'SalesRevenueNet', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'RevenueFromContractWithCustomerIncludingAssessedTax'],
        'Net Income': ['NetIncomeLoss'],
        'Total Assets': ['Assets'],
        'Total Liabilities': ['Liabilities'],
        'Cash Flow': ['NetCashProvidedByUsedInOperatingActivities']
    }

    financial_data = {}
    for metric, fact_names in metrics.items():
        financial_data[metric] = None
        for fact_name in fact_names:
            if 'us-gaap' in data.get('facts', {}) and fact_name in data['facts']['us-gaap']:
                units = data['facts']['us-gaap'][fact_name].get('units', {})
                if 'USD' in units:
                    values = units['USD']
                    # Filter for the specific fiscal year based on 'end' date
                    specific_values = []
                    for v in values:
                        end_date_str = v.get('end')
                        if end_date_str:
                            try:
                                end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
                                if end_date_obj.year == filing_year:
                                    specific_values.append(v)
                            except ValueError:
                                logging.warning(f"Invalid end date format: {end_date_str}")
                                continue
                    if specific_values:
                        # Assuming the first entry corresponds to the annual report
                        financial_data[metric] = specific_values[0].get('val', None)
                        logging.info(f"Found {metric} data using {fact_name}: {financial_data[metric]}")
                        break  # Break the loop if we found a value
                else:
                    logging.warning(f"No USD units found for {fact_name}")
            else:
                logging.warning(f"{fact_name} not found in us-gaap facts")
        
        if financial_data[metric] is None:
            logging.warning(f"No data found for {metric}")

    return financial_data