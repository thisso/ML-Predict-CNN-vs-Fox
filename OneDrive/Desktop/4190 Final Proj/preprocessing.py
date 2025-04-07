# this file preprocesses and adds labels to the orginal csv 
import pandas as pd
from urllib.parse import urlparse

# Load the raw URL data
df = pd.read_csv("url_only_data.csv")

# Safety check for column name
if 'url' not in df.columns:
    raise ValueError("Expected a column named 'url' in the CSV")

# Extract meaningful parts of the URL
def extract_url_parts(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    path_parts = parsed.path.strip("/").split("/")
    section = path_parts[0] if len(path_parts) > 0 else ""
    slug = path_parts[-1] if len(path_parts) > 1 else ""
    return pd.Series([domain, section, slug])

df[['domain', 'section', 'slug']] = df['url'].apply(extract_url_parts)

# Create label column for training later
def assign_label(url):
    if 'foxnews' in url:
        return 'fox'
    elif 'cnn' in url:
        return 'nbc'
    else:
        return 'unknown'

df['label'] = df['url'].apply(assign_label)

# drop rows that aren't Fox or CNN
df = df[df['label'].isin(['fox', 'nbc'])]

# Save to a new CSV
df.to_csv("preprocessed_training.csv", index=False)

print(" Preprocessing complete. Saved to preprocessed_urls.csv")
#give you a sample of the pre processed training data 
print(df.sample(5))