import string

path_to_driver = 'C:/Users/Thrall/chromedriver/chromedriver.exe'
path_to_raw = "../data/raw_data/scraped_tweets.csv"
path_to_parsed = "../data/parsed_data/scraped_tweets.csv"
path_to_edited = "../data/edited_data/scraped_tweets.csv"
path_to_staging = "../data/staging_data/scraped_tweets.csv"

letters = {"series {}".format(letter): number for letter, number in zip(string.ascii_lowercase, range(1, 28))}

series_converter = {
    "seed": 0,
    "mezzanine": 27,
    "ipo": 28,
    "public": 29
}

series_converter.update(letters)

inv_series_converter = {v: k for k, v in series_converter.items()}

units_converter = {
    "billion": 1000000000,
    "b": 1000000000,
    "million": 1000000,
    "m": 1000000,
}

list_cols_parsed = ["date", "user", "parsed_data"]

list_cols_edited = ["date", "user", "edited_data"]

list_cols_staged = ["date", "user", "date_scraped", "company_name", "series", "raised_funds", "investors", "date"]
