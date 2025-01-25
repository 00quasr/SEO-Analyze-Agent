# Website Scraper Logic

import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    """
    Scrapes the given website URL and extracts meta tags, headings, and images.

    Args:
        url (str): The website URL to scrape.

    Returns:
        dict: A dictionary containing the extracted data.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract meta tags
        meta_title = soup.title.string if soup.title else "No title found"
        meta_description = "No description found"
        meta_keywords = "No keywords found"

        for tag in soup.find_all('meta'):
            if tag.get('name') == 'description':
                meta_description = tag.get('content', "No description")
            if tag.get('name') == 'keywords':
                meta_keywords = tag.get('content', "No keywords")

        # Extract headings
        headings = {
            'h1': [h.get_text(strip=True) for h in soup.find_all('h1')],
            'h2': [h.get_text(strip=True) for h in soup.find_all('h2')],
            'h3': [h.get_text(strip=True) for h in soup.find_all('h3')]
        }

        # Extract images
        images = [
            {
                'src': img.get('src', 'No source'),
                'alt': img.get('alt', 'No alt text')
            }
            for img in soup.find_all('img')
        ]

        # Compile results
        result = {
            'url': url,
            'meta': {
                'title': meta_title,
                'description': meta_description,
                'keywords': meta_keywords
            },
            'headings': headings,
            'images': images
        }

        return result

    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def save_to_json(data, filename):
    """
    Saves the scraped data to a JSON file.

    Args:
        data (dict): The data to save.
        filename (str): The name of the JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
if __name__ == "__main__":
    url = input("Bitte geben sie die URL ein: ")
    scraped_data = scrape_website(url)
    save_to_json(scraped_data, "scraped_data.json")
    print(f"Scraped data saved to scraped_data.json")
