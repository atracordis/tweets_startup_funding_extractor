from process.edit_data import *
from process.parse_data import *
from resources.const import *
from utils.scraping import *
import pandas as pd

if __name__ == "__main__":
    df_tweets = pd.read_csv(path_to_raw, sep=";")
    # extract URLs to scrape
    df_tweets["urls"] = df_tweets.raw_tweets.apply(url_extractor)
    # scrape and extract bodies of articles
    df_tweets["bodies"] = df_tweets.urls.apply(extract_body)

    # parse bodies
    df_tweets["parsed_data"] = df_tweets["bodies"].apply(parse_metadata)
    df_tweets[list_cols_parsed].to_csv(path_to_parsed, index=False, sep=";")

    # extract information from parsed bodies
    df_tweets["edited_data"] = df_tweets["parsed_data"].apply(edit_metadata)
    df_tweets[list_cols_edited].to_csv(path_to_edited, index=False, sep=";")

    # format edited_data into staging_data data
    edited_data = df_tweets["edited_data"].apply(lambda x: dict(x) if type(x) == str else x)
    edited_data = pd.DataFrame(edited_data.to_list())
    staging_data = pd.concat([df_tweets, edited_data], axis=1)

    # export staging_data data
    staging_data[list_cols_staged].to_csv(path_to_staging, index=False, sep=";")
