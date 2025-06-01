import re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

urls = [
"https://cdn.pornkeen.net/2022/12/14/",
"https://cdn.pornkeen.net/2022/12/15/",
"https://cdn.pornkeen.net/2022/12/16/",
"https://cdn.pornkeen.net/2022/12/17/",
"https://cdn.pornkeen.net/2022/12/18/",
"https://cdn.pornkeen.net/2022/12/19/",
"https://cdn.pornkeen.net/2022/12/20/",
"https://cdn.pornkeen.net/2022/12/21/",
"https://cdn.pornkeen.net/2022/12/22/",
# add more cdns here
  

]

all_matching_links = set()

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        content = response.text

        soup = BeautifulSoup(content, "html.parser")

  
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

   
        matches = [link for link in links if re.search(r'dimple', link, re.IGNORECASE)] #in place of dimple you can enter the name of the actress you want only one name

        all_matching_links.update(matches)

    except Exception as e:
        print(f"Failed to process {url}: {e}")

print(',\n'.join(f'"{link}"' for link in sorted(all_matching_links)))
