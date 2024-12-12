import requests
import pandas as pd
import xml.etree.ElementTree as ET
import time
from sqlalchemy import create_engine

api_token = 'BLWxxWNOgwYzdktpkEPHiSRADAIdIivBbfxUdpes'
headers = {
    'Authorization': f'Discogs token={api_token}',
    'User-Agent': 'DiscogsETL/1.0'
}
base_url = 'https://api.discogs.com/labels'
request_delay = 1.2
db_url = 'postgresql+psycopg2://postgres:postgresql@localhost/postgres'

def extract_xml_from_url(url):
    response = requests.get(url)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    labels = []

    for label in root.findall('label'):
        label_data = {}
        for child in label:
            label_data[child.tag] = child.text
        labels.append(label_data)

    return pd.DataFrame(labels)

def fetch_all_releases(label_id, per_page=100):
    releases = []
    page = 1

    while True:
        url = f"{base_url}/{label_id}/releases"
        params = {"page": page, "per_page": per_page}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            releases.extend(data.get('releases', []))

            if page >= data.get('pagination', {}).get('pages', 1):
                break
            page += 1
        elif response.status_code == 429:
            time.sleep(request_delay * 2)
        else:
            break

        time.sleep(request_delay)

    return releases

def fetch_label_details_with_releases(label_id):
    try:
        releases = fetch_all_releases(label_id)

        release_years = [release.get('year') for release in releases if release.get('year')]

        return {
            "num_of_releases": len(releases),
            "min_release_year": min(release_years) if release_years else None,
            "max_release_year": max(release_years) if release_years else None
        }
    except Exception as e:
        return {"num_of_releases": None, "min_release_year": None, "max_release_year": None}

def labels_with_api_releases(df):
    api_results = []

    for index, row in df.iterrows():
        label_id = row['id']
        if pd.isnull(label_id):
            api_results.append({"num_of_releases": None, "min_release_year": None, "max_release_year": None})
            continue

        details = fetch_label_details_with_releases(label_id)
        api_results.append(details)

        time.sleep(request_delay)

    api_df = pd.DataFrame(api_results)
    return pd.concat([df.reset_index(drop=True), api_df], axis=1)

def load_to_postgres(df, db_url, table_name):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

def main():
    xml_url = "https://discogs-data-dumps.s3-us-west-2.amazonaws.com/data/2023/discogs_20230101_labels.xml.gz"
    df = extract_xml_from_url(xml_url)

    df_filtered = df[(df['data_quality'] == "Complete and Correct") & (df['contactinfo'].notna())]

    df_transformed = labels_with_api_releases(df_filtered)

    load_to_postgres(df_transformed, db_url, "labels")

if __name__ == "__main__":
    main()