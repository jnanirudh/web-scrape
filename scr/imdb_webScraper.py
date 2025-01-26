from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# imdb Top 250 URL
IMDB_URL = "https://www.imdb.com/chart/top/"

# WebDriver set-up
driver = webdriver.Chrome()
driver.get(IMDB_URL)

# wait for page to load
time.sleep(3)

# scrape movie titles, rankings, ratings, years, and number of ratings
movies = driver.find_elements(By.XPATH, "//li[contains(@class, 'ipc-metadata-list-summary-item')]")[:100]

movie_list = []
for movie in movies:
    # Movie title and ranking
    title_ranking = movie.find_element(By.XPATH, ".//h3").text
    ranking, title = title_ranking.split(". ", 1)  # Split ranking and title

    # Rating and number of ratings
    rating_element = movie.find_elements(By.XPATH, ".//span[contains(@class, 'ipc-rating-star')]")
    if rating_element:
        rating_text = rating_element[0].text  # e.g., "9.3 (3M)"
        rating, num_ratings = rating_text.split(" ")
        num_ratings = num_ratings.strip("()")  # Remove parentheses
    else:
        rating = "N/A"
        num_ratings = "N/A"

    # Year
    year_element = movie.find_elements(By.XPATH, ".//span[contains(@class, 'titleColumn')]/span")
    year = year_element[0].text.strip("()") if year_element else "N/A"

    movie_list.append({
        "Ranking": ranking,
        "Title": title,
        "Year": year,
        "Rating": rating,
        "Number of Ratings": num_ratings
    })

# Close the driver
driver.quit()

# Save to CSV
df = pd.DataFrame(movie_list, columns=["Ranking", "Title", "Year", "Rating", "Number of Ratings"])
df.to_csv("IMDb_Top_100.csv", index=False)

print("Scraping completed! Data saved to IMDb_Top_100.csv")
