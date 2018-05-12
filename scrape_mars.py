
import os
from bs4 import BeautifulSoup as bs
from splinter import Browser
import random
import time

# The bs object:
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://mars.nasa.gov/news/'


#visit the url
browser.visit(url)

#set up html and the soup
html = browser.html
soup = bs(html, 'lxml')

#get news title and teaser paragraph
news_content_title = soup.find('div', class_='content_title')
teaser_body_content = soup.find(class_='article_teaser_body')
latest_title = news_content_title.find('a').get_text()

teaser_body = teaser_body_content.text
teaser_body


# Part 2: Getting featured image with use of splinter
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)



#visit img url & saving the html
browser.visit(url)
featured_image = browser.find_by_id('full_image')
featured_image.click()
time.sleep(5)
more_info = browser.click_link_by_partial_text('more info')
#more_info.click()
html=browser.html
img_soup = bs(html,'lxml')


featured_image = img_soup.find('figure', class_='lede')

# print(featured_image)
latest_image = "https://www.jpl.nasa.gov" + featured_image.find('a')['href']

# Twitter weather
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
time.sleep(random.random()*3)
html = browser.html
tweet_soup = bs(html, 'lxml')

tweet = tweet_soup.find('p', class_='TweetTextSize')
weather_tweet = tweet.get_text()

weather_tweet



# Facts about Mars with the use of pandas
import pandas as pd



df = pd.read_html('https://space-facts.com/mars/')[0]



df.columns = ['Mars:', 'Fact']


df.set_index('Mars:', inplace=True)
df

table = df.to_html()

table

table = table.replace("\n", "")
table


# Hemispheres
url ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


browser.visit(url)
html = browser.html
h_soup = bs(html,'lxml')


hemisphere = h_soup.find_all('a', class_='itemLink')


hemispheres = []
for i in hemisphere:
    browser.visit('https://astrogeology.usgs.gov'+i['href'])
    image = browser.find_by_text('Sample').first
    hemispheres.append(image['href'])
    browser.back()
    

hemispheres

