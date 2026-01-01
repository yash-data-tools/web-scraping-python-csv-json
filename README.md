# Python Web Scraper

A Python-based web scraper that extracts structured product data from an e-commerce website.  
The scraper supports pagination and allows exporting the collected data to **CSV or JSON** format based on user choice.

---

## Features
- Scrapes product data such as title, price, availability, rating, and product link
- Handles multi-page pagination automatically
- Uses request headers to mimic a real browser
- Exports scraped data to **CSV or JSON**
- Stores data in a clean, structured format

---

## Technologies Used
- Python
- requests
- BeautifulSoup (bs4)
- csv
- json
- urllib

---

## Data Extracted
For each product, the scraper collects:
- Book Title
- Price
- Availability
- Rating
- Product Page Link

---

## How to Run
1. Make sure Python is installed on your system  
2. Install required libraries:pip install requests beautifulsoup4
3. Run the script:


---

## Example Output
- `Scraped_data.csv`
- `Scraped_data.json`

Both files contain structured product data ready for analysis or further processing.

---

## Use Cases
- Product data collection
- Price comparison datasets
- Web scraping practice
- Data analysis and cleaning with Pandas

---

## Notes
- The scraper respects pagination and stops automatically at the last page
- Designed for educational and data-processing purposes

---

## Author
Yash Kumar Shaw


