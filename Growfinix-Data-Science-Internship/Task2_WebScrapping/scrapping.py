import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# outputs folder create karega agar nahi hai
os.makedirs("outputs", exist_ok=True)

# Website URL
url = "http://books.toscrape.com/"

# Request bhejna
response = requests.get(url)

# HTML parse karna
soup = BeautifulSoup(response.text, "html.parser")

books = []

# Books data extract karna
for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    books.append([title, price, availability])

# DataFrame banana
df = pd.DataFrame(
    books,
    columns=["Title", "Price", "Availability"]
)

# CSV save karna
df.to_csv("outputs/books_data.csv", index=False)

# Output dikhana
print(df.head())
print("\nTask 2 Completed Successfully!")