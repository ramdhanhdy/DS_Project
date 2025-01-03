import requests
import pandas as pd
from datetime import datetime, timedelta

def get_company_cik(ticker):
    url = f"https://www.sec.gov/files/company_tickers.json"
    response = requests.get(url, headers={'User-Agent': 'Your Name yourname@example.com'})
    data = response.json()
    for entry in data.values():
        if entry['ticker'] == ticker:
            return str(entry['cik_str']).zfill(10)
    return None

def get_latest_10k_filing(cik):
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    response = requests.get(url, headers={'User-Agent': 'Your Name yourname@example.com'})
    data = response.json()
    for filing in data['filings']['recent']:
        if filing['form'] == '10-K':
            return filing['accessionNumber']
    return None

def extract_financial_data(cik, accession_number):
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    response = requests.get(url, headers={'User-Agent': 'ramdhanhdy3@gmail.com'})
    data = response.json()

    metrics = {
        'Revenue': 'Revenues',
        'Net Income': 'NetIncomeLoss',
        'Total Assets': 'Assets',
        'Total Liabilities': 'Liabilities',
        'Cash Flow from Operating Activities': 'NetCashProvidedByUsedInOperatingActivities'
    }

    financial_data = {}
    for metric, fact_name in metrics.items():
        if 'us-gaap' in data['facts'] and fact_name in data['facts']['us-gaap']:
            units = data['facts']['us-gaap'][fact_name]['units']
            if 'USD' in units:
                values = units['USD']
                # Filter for annual data and sort by end date
                annual_values = [v for v in values if v['form'] == '10-K']
                annual_values.sort(key=lambda x: x['end'], reverse=True)
                if annual_values:
                    financial_data[metric] = annual_values[0]['val']

    return financial_data

def main():
    companies = {
        'MSFT': 'Microsoft',
        'TSLA': 'Tesla',
        'AAPL': 'Apple'
    }

    all_data = []

    for ticker, company_name in companies.items():
        cik = get_company_cik(ticker)
        if cik:
            accession_number = get_latest_10k_filing(cik)
            if accession_number:
                financial_data = extract_financial_data(cik, accession_number)
                for metric, value in financial_data.items():
                    all_data.append({
                        'Company': company_name,
                        'Metric': metric,
                        'Value': value
                    })
            else:
                print(f"No 10-K filing found for {company_name}")
        else:
            print(f"CIK not found for {company_name}")

    df = pd.DataFrame(all_data)
    df.to_csv('financial_data.csv', index=False)
    print("Financial data has been saved to 'financial_data.csv'")

if __name__ == "__main__":
    main()