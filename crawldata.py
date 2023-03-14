import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the web page
response = requests.get('https://ta.vietstock.vn/Customer?lang=vi',verify=False)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the relevant data from the web page
data_rows = soup.find_all('tr', {'class': 'odd'}) + soup.find_all('tr', {'class': 'even'})

# Create a list to store the extracted data
data_list = []

# Extract the Volume and Close price of the stock for the past 2 years
for row in data_rows:
    cells = row.find_all('td')
    if len(cells) > 3:
        date = cells[0].text.strip()
        if '2020' in date or '2021' in date:
            volume = cells[3].text.strip()
            close_price = cells[4].text.strip()
            data_list.append([date, volume, close_price])

# Write the data to a CSV file
with open('stock_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Volume', 'Close Price'])
    for data in data_list:
        writer.writerow(data)
