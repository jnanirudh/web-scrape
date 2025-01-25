from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# WebDriver set-up
driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top/")

# Scrape data
movies = driver.find_elements(By.CSS_SELECTOR, "td.titleColumn")
ratings = driver.find_elements(By.CSS_SELECTOR, "td.imdbRating strong")

data = []
for movie, rating in zip(movies, ratings):
    title = movie.find_element(By.TAG_NAME, "a").text
    year = movie.find_element(By.TAG_NAME, "span").text.strip("()")
    rank = movie.text.split(".")[0]
    imdb_rating = rating.text
    data.append([int(rank), title, int(year), float(imdb_rating)])

# conversion
df = pd.DataFrame(data, columns=["Ranking", "Title", "Release Year", "IMDb Rating"])
df.to_csv("IMDb_Top_250.csv", index=False)

driver.quit()
print("Data saved to IMDb_Top_250.csv")
