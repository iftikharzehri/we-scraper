import requests
from bs4 import BeautifulSoup

url = "https://unstats.un.org/sdgs/metadata/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

goals = soup.find_all('div', class_='panel panel-default')

for goal in goals:
    goal_title = goal.find('h4').text.strip()
    print(f"Goal: {goal_title}")
    
    targets = goal.find_all('h5')
    for target in targets:
        target_title = target.text.strip()
        print(f"  Target: {target_title}")
        
        indicators = target.find_next_siblings('ul')
        for indicator in indicators:
            indicator_title = indicator.find('strong').text.strip()
            print(f"    Indicator: {indicator_title}")
            
            metadata_links = indicator.find_all('a', href=True)
            for link in metadata_links:
                link_url = link['href']
                link_text = link.text.strip()
                print(f"      Metadata: {link_text} ({link_url})")  