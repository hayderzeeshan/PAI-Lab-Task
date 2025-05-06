import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def extract_emails_from_url(url):
    emails = set()
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            # Simple regex for email
            found_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
            emails.update(found_emails)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return list(emails)

def main():
    # Load URLs from CSV
    df = pd.read_csv('websites.csv')
    all_results = {}

    for index, row in df.iterrows():
        url = row['url']
        print(f"Scanning: {url}")
        emails = extract_emails_from_url(url)
        all_results[url] = emails

    # Output result
    for site, emails in all_results.items():
        print(f"\n{site} => {emails if emails else 'No emails found'}")

if __name__ == "__main__":
    main()
