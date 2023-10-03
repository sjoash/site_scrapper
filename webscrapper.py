import requests
from bs4 import BeautifulSoup
import pprint

# Function to create a custom dictionary with links and their text
def create_custom_hn(links):
    dataSets_links = []

    for item in links:
        # Find the 'a' tag within the 'item'
        link_tag = item.find('a')
        
        if link_tag:
            # Check if 'a' tag exists
            link = link_tag.get('href')
            link = 'https://dagshub.com'+ link
            text = link_tag.text
            dataSets_links.append({'text': text, 'link': link})
        else:
            print("No 'a' tag found in this element")
    
    return dataSets_links

# Dictionary for the main links and their text
main_links_dict = {}

res = requests.get('https://dagshub.com/DagsHub-Datasets/mevadata-dataset/src/main/s3:/mevadata-public-01')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.name')[:4]
main_links_dict['links'] = links

# Separate dictionaries for link1, link2, link3, and their text
link1_dict = {}
link2_dict = {}
link3_dict = {}

res1 = requests.get('https://dagshub.com/DagsHub-Datasets/mevadata-dataset/src/main/s3:/mevadata-public-01/drop-4-hadcv22')
soup1 = BeautifulSoup(res1.text, 'html.parser')
link1 = soup1.select('.name')
link1_dict['link1'] = link1

res2 = requests.get('https://dagshub.com/DagsHub-Datasets/mevadata-dataset/src/main/s3:/mevadata-public-01/drop-5-mevid')
soup2 = BeautifulSoup(res2.text, 'html.parser')
link2 = soup2.select('.name')
link2_dict['link2'] = link2

res3 = requests.get('https://dagshub.com/DagsHub-Datasets/mevadata-dataset/src/main/s3:/mevadata-public-01/drops-123-r13')
soup3 = BeautifulSoup(res3.text, 'html.parser')
link3 = soup3.select('.name')
link3_dict['link3'] = link3

# Combine the dictionaries
combined_dict = {
    'main_links_dict': main_links_dict,
    'link1_dict': link1_dict,
    'link2_dict': link2_dict,
    'link3_dict': link3_dict
}

# pprint.pprint(create_custom_hn(combined_dict['main_links_dict']['links']))

# To access link1, link2, link3 and their text, you can use:
# pprint.pprint(create_custom_hn(combined_dict['link1_dict']['link1']))
pprint.pprint(create_custom_hn(combined_dict['link2_dict']['link2']))
# pprint.pprint(create_custom_hn(combined_dict['link3_dict']['link3']))
