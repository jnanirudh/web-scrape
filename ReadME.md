# IMDb Top 250 Web Scraper

This is a Python script designed for web scraping, specifically for extracting data from the IMDb Top 250 movies list. The current implementation scrapes the IMDb website and produces a CSV file with 5 attributes for the top 100 movies. The script is flexible and can be modified for other web scraping purposes as needed.

---

## Features
- Scrapes IMDb's Top 250 movies page.
- Extracts detailed information for the top 100 movies.
- Generates a CSV file with 5 attributes for each movie.

---

## Output
The script generates a CSV file containing the following 5 attributes for each movie:
1. **Rank**: The movie's rank on the IMDb Top 250 list.
2. **Title**: The movie's name.
3. **Year**: The release year of the movie.
4. **Rating**: The IMDb rating of the movie.
5. **Number of Ratings**: The number of votes the movie has received.

---

## Prerequisites
To run the script, ensure you have the following installed:
- Python 3.7 or higher
- Required Python libraries: `requests`, `BeautifulSoup4`, `pandas`

You can install the dependencies using pip:
```bash
pip install requests beautifulsoup4 pandas