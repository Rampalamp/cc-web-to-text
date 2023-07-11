import requests
from .text_extractor import TextExtractor


class SingleScrape:
    def get_text(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return TextExtractor.extract_text(response.text)
            else:
                print(f"Error: Failed to fetch data from {url}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to fetch data from {url} : {e}")
            return None
