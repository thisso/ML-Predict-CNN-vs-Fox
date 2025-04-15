import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Load the preprocessed CSV with 'url' and 'label'
df = pd.read_csv("preprocessed_training.csv")

# Function to fetch the <h1> title from a webpage
def fetch_title(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Customize this per domain if needed
        title_tag = soup.find('h1')
        return title_tag.get_text().strip() if title_tag else ""
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# Apply fetching titles one by one (slow, safe)
titles = []
for idx, row in df.iterrows():
    url = row['url']
    title = fetch_title(url)
    titles.append(title)
    time.sleep(1)  # Be nice to servers

# Add titles as a new column
df['title'] = titles

# Save the combined dataset
df.to_csv("titles and labels.csv", index=False)
print("Scraping and labeling complete. Saved to articles_with_titles.csv.")
