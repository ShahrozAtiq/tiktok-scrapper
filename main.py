from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# specify the search parameter
search_param = "cats"

# set up driver
driver = webdriver.Chrome()

# navigate to tiktok search page
driver.get(f"https://www.tiktok.com/tag/{search_param}")

# scroll down to load more videos
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# find all video elements
videos = driver.find_elements_by_xpath('//div[@class="video-feed-item-wrapper"]')

# initialize empty list to store video data
video_data = []

# scrape data for each video
for video in videos:
    # scrape video description
    desc = video.find_element_by_xpath('.//p[@class="video-feed-item-description"]').text
    
    # scrape number of likes
    likes = video.find_element_by_xpath('.//span[@class="video-feed-item-info-count"]').text
    
    # scrape number of comments
    comments = video.find_element_by_xpath('.//span[@class="video-feed-item-info-count"]'
                                           '/following-sibling::span').text
    
    # scrape user profile info
    username = video.find_element_by_xpath('.//h3[@class="video-feed-item-username"]').text
    userhandle = video.find_element_by_xpath('.//h4[@class="video-feed-item-user-handle"]').text
    
    # append data to list
    video_data.append([desc, likes, comments, username, userhandle])

# write data to csv file
with open(f"{search_param}_tiktok_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Description", "Likes", "Comments", "Username", "User Handle"])
    writer.writerows(video_data)

# close driver
driver.quit()