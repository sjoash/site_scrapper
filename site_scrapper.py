import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import fnmatch

def extract_video_links(folder_url):
    res = requests.get(folder_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # Assuming video links are identified by a specific class, e.g., 'video-link'
    video_links = [urljoin(folder_url, a['href']) for a in soup.select('.video-link')]
    return video_links

def filter_links_by_extension(links, extension):
    return [link for link in links if link.endswith(extension)]

# Function to extract links from a page
base_url = 'https://dagshub.com/DagsHub-Datasets/mevadata-dataset/src/main/s3:/mevadata-public-01'
res = requests.get(base_url)
soup = BeautifulSoup(res.text, 'html.parser')
path = soup.select('.name a')[:4]

# Add 'https://dagshub.com' to each path
paths_with_base_url = [urljoin(base_url, element['href']) for element in path]

# Print the modified paths
# print(paths_with_base_url)


for folder_link in paths_with_base_url:
    folder_urls = [folder_link]
    avi_links = []
    for folder_url in folder_urls:
        video_links_in_folder = extract_video_links(folder_url)
        avi_links.extend(filter_links_by_extension(video_links_in_folder, '.avi'))
    # print(folder_link)
    for link in avi_links:
        print(link)

# Print the filtered links
# for link in avi_links:
#     print(link)
# links = glob.glob(path + '/*.avi','.mp4')

    
    # List of video file extensions to check for
    
# links = []
    
# for link in soup.find_all('a'):
#     href = link.get('href')
#     if href:
#         full_url = urljoin(base_url, href)  # Make the URL absolute
#         print(full_url)
            # Check if the URL ends with any of the video extensions
        
    
# print(links)

# Base URL of the directory


# Initialize a list to store all the links
# video_extensions = ['.avi', '.mp4']
# all_links = []

# # Initial extraction from the base URL
# base_links = extract_links(base_url)
# print(base_links)
# all_links.extend(base_links)

# print(all_links)

# Now, all_links contains all the links ending with .avi

