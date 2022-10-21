import requests
from bs4 import BeautifulSoup
import json


all_info_shop = []

for i in range(7):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={i + 1}' # Makes a url that goes through 7 sites
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml') # Outputs the entire html code in a beautiful form from the url
    dress = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4') # Outputs the div and the specified class from the html code
    description = soup.find_all('h4', class_='card-title') # Searches for div and specified class from html code

    
    for not_link in description:
        for link in not_link.find_all('a'): # I am looking for the <a> tag in the html code passed through the cycle
            link_text = link.get('href') # I'm looking for a string in the <a> tag
            url_input = f'https://scrapingclub.com{link_text}' # I write this thread in 2 urls
            response_link = requests.get(url_input)
            soup_link = BeautifulSoup(response_link.text, 'lxml') # Outputs the second url in html code  
            info = soup_link.find_all('div', class_='card-body') # Searches for div and specified class from html code
            for all_info in info:
                for text in all_info.find_all('h3'): # Searches for the specified tag from the div class
                    text_json = [text.text]
                for cost in all_info.find_all('h4'): # Searches for the specified tag from the div class
                    cost_json = cost.text
                for title in all_info.find_all('p', class_='card-text'): # Searches for the specified tag from the div class
                    title_json = title.text
            text_json.append(cost_json)
            text_json.append(title_json)
            all_info_shop.append(text_json)
            
            with open('shop.json', 'w', encoding='UTF-8') as data:
                json.dump(all_info_shop, data, indent=4)
