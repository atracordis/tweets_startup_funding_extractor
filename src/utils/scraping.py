from datetime import datetime, timedelta
import GetOldTweets3 as got
from bs4 import BeautifulSoup
from selenium import webdriver
from resources.const import *

driver = webdriver.Chrome(path_to_driver)
driver.get("https://techcrunch.com/")
driver.find_element_by_name('agree').click()


def tweet_acquisition(row):
    """
    goes to twitter to rescrape tweets based on
    user, the first six words of a tweet
    and the tweet's date
    :param row:
    :return:
    """
    username = row["user"]
    text_query = " ".join(row["tweet"].split()[0:6])
    str_date_since = row["date"][0:10]
    str_date_until = add_days(str_date_since)

    count = 1

    tweet_criteria = (got.manager.TweetCriteria()
                     .setQuerySearch(text_query)
                     .setUsername(username)
                     .setSince(str_date_since)
                     .setUntil(str_date_until)
                     .setMaxTweets(count))
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweet_criteria)
    # Creating list of chosen tweet data
    text_tweets = {"tweet": tweet.text for tweet in tweets}.get("tweet", "")
    return text_tweets


def extract_body(str_url):
    """
    goes to url and scrapes article content, title and date from it
    designed to work on tech crunch. Could be generalized
    :param str_url:
    :return:
    """
    if str_url == "":
        return ""
    try:
        driver.get(str_url)
    except:
        return ""
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    title = soup.title
    try:
        body = soup.findAll(attrs={"class": "article-content"})[0].findAll("p")
    except:
        body = ""
    try:
        date_str = soup.findAll(attrs={"class": "full-date-time"})
    except:
        date_str = ""

    return {"body": body, "title": title, "date": date_str}


def add_days(str_date, days=1, date_format="%Y-%m-%d"):
    """
    silly utils function to add a number of days to a date
    in a string format
    :param str_date:
    :param days:
    :param date_format:
    :return:
    """
    date = datetime.strptime(str_date, date_format)
    modified_date = date + timedelta(days=days)
    return datetime.strftime(modified_date, date_format)
