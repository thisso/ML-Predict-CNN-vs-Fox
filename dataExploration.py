import pandas as pd
import numpy as np
from urllib.parse import urlparse

# Load CSV
df = pd.read_csv('url_only_data.csv')

# Preview the data
print("First few rows:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic stats
print("\nNumber of URLs:", len(df))

# Extract features from URLs
def extract_parts(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    path_parts = parsed.path.strip("/").split("/")
    section = path_parts[0] if len(path_parts) > 0 else None
    slug = path_parts[-1] if len(path_parts) > 1 else None
    return pd.Series([domain, section, slug])

df[['domain', 'section', 'slug']] = df['url'].apply(extract_parts)

# Show the processed data
print("\nExtracted URL parts:")
print(df[['url', 'domain', 'section', 'slug']].head())

# Optional: Save the processed version
df.to_csv('processed_url_data.csv', index=False)

