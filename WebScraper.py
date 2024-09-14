import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the books website
URL = "http://books.toscrape.com/"  # Example books website
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Create/open a CSV file to store the scraped data
    with open('books_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the headers to the CSV file
        writer.writerow(['Title', 'Price', 'Availability', 'Rating'])
        
        # Find all book containers
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            # Get the title of the book
            title = book.h3.a['title']
            
            # Get the price of the book
            price = book.find('p', class_='price_color').text.strip()
            
            # Get the availability status of the book
            availability = book.find('p', class_='instock availability').text.strip()
            
            # Get the rating of the book
            rating_tag = book.find('p', class_='star-rating')
            rating = rating_tag['class'][1] if rating_tag else 'No Rating'
            
            # Write the book data to the CSV file
            writer.writerow([title, price, availability, rating])

    print("Data has been successfully scraped and saved to 'books_data.csv'")
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")

                 
