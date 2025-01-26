from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# IMDb Top 250 URL
IMDB_URL = "https://www.imdb.com/chart/top/"

# WebDriver set-up
driver = webdriver.Chrome()
driver.get(IMDB_URL)

# Wait for the page to load (adjust if needed)
time.sleep(3)

# Scrape movie titles and ratings
movies = driver.find_elements(By.XPATH, "//li[contains(@class, 'ipc-metadata-list-summary-item')]")[:100]

movie_list = []
for movie in movies:
    title = movie.find_element(By.XPATH, ".//h3").text  # Movie title
    rating_element = movie.find_elements(By.XPATH, ".//span[contains(@class, 'ipc-rating-star')]")
    rating = rating_element[0].text if rating_element else "N/A"  # Rating if available

    movie_list.append({"Title": title, "Rating": rating})

# Close the driver
driver.quit()

# Save to CSV
df = pd.DataFrame(movie_list, columns=["Title", "Rating"])
df.to_csv("IMDb_Top_100.csv", index=False)

print("Scraping completed! Data saved to IMDb_Top_100.csv")
