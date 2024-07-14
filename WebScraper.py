import requests
from bs4 import BeautifulSoup
import csv
import os

# URL of the website to scrape
url = 'https://bluebirdarts.pk/product/signatureacrylics/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the container that holds the data (in this case, paint details)
    paints = soup.find_all('div', class_='paint-item')
    
    # Create a list to store the extracted data
    paint_datalist = []

    # Extract the desired data for each paint item
    for paint in paints:
        name = paint.find('h2', class_='paint-name').text.strip()
        color_code = paint.find('span', class_='color-code').text.strip()
        price = paint.find('span', class_='price').text.strip()
        
        # Append the data to the list
        paint_datalist.append([name, price, color_code])

    # Define the CSV file headers
    headers = ['Name', 'Price', 'Color Code']

    # Print the current working directory
    print("Current working directory:", os.getcwd())

    # Write the data to a CSV file
    with open('paints.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(paint_datalist)

    print("Data has been successfully written to paints.csv")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

print("Hello")  # Just an additional message to check script execution
