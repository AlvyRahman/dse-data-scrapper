import requests
import csv
import re
from bs4 import BeautifulSoup

URL = "https://www.dsebd.org/latest_share_price_scroll_by_ltp.php"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

content = soup.find('div', attrs = {'class':'table-responsive inner-scroll'})

ths = content.findAll('th')
headers = []
for th in ths:
    headers.append(th.text)

'''
for header in headers:
    print(header)

headersStr = "  ".join(headers) # for printing in single line, seperated by space.
print(headersStr)
'''

#tbodys = content.find_all('tbody')
#trs = content.findAll('tr')
tds = content.findAll('td')
rows = [td.get_text(strip=True) for td in tds]
tempData = []
data = []
counter = 0
for row in rows:
    tempData.append(row)
    counter += 1
    if(counter == 11):
        di = dict(zip(headers, tempData))
        data.append(di)
        tempData = []
        counter = 0

for row in data:
    print(row)



'''
CHATGPT CODE
# Write the list of dictionaries to a CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=column_names)
    
    # Write the header
    csv_writer.writeheader()
    
    # Write each dictionary (row) to the CSV file
    csv_writer.writerows(data_dict_list)

print(f'Data has been successfully saved to {csv_file_path}.')
'''