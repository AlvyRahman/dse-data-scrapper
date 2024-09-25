import requests
import csv
from bs4 import BeautifulSoup

URL = "https://www.dsebd.org/market-statistics.php"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

content = soup.find('pre')

# print the content
for row in content:
    print(row)

# save the content in a txt file
filename = 'Market_Statistics.txt'
with open(filename, 'w', newline='') as f:
    for row in content:
        f.writelines(row)