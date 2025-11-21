# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# We will scrape data from http://books.toscrape.com (safe practice site)
names = []   # To store product names
prices = []  # To store product prices
ratings = [] # To store product ratings

# Loop through first 3 pages (you can increase this number if you want)
for page in range(1, 4):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    # Parse the webpage
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all product items on the page
    products = soup.find_all("article", class_="product_pod")

    # Extract details from each product
    for product in products:
        # Get the book title
        name = product.h3.a["title"]
        # Get the price
        price = product.find("p", class_="price_color").text
        # Get the rating (hidden in class name)
        rating = product.p["class"][1]

        # Append data to our lists
        names.append(name)
        prices.append(price)
        ratings.append(rating)

# Store the data into a DataFrame
df = pd.DataFrame({
    "Name": names,
    "Price": prices,
    "Rating": ratings
})

# Save the data into a CSV file
df.to_csv("products.csv", index=False)

print("✅ Data scraped and saved into products.csv")
