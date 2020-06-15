from utils.parsing import *

from bs4 import BeautifulSoup

from functools import reduce
from operator import iconcat
import spacy

nlp = spacy.load("en_core_web_sm")


def parse_metadata(raw_metadata):
    parsed_metadata = {}
    i = 1
    if raw_metadata == "":
        return ""
    for p in raw_metadata["body"]:
        parsed_metadata[i] = {}
        if i == 1:
            try:
                parsed_metadata[i]["name_candidates"] = p.find("a").contents[0].text
            except:
                pass

        parsed_investors = parse_investors(p)
        if parsed_investors:
            parsed_metadata[i]["investors"] = parsed_investors

        funds = parse_funds(p)
        if funds:
            parsed_metadata[i]["funds"] = funds

        series = parse_series(p)
        if series:
            parsed_metadata[i]["series"] = series

        i = i + 1
    parsed_metadata[0] = parse_datetitle(raw_metadata)

    return parsed_metadata


def parse_investors(p):
    investors = p.findAll(attrs={"class": "crunchbase-link", "data-type": "organization"})

    spacy_labels = [ent.text.strip() for ent in nlp(p.text).ents if ent.label_ in ["ORG", "PERSON"]]

    parsed_investors = []
    if investors:
        parsed_investors.extend([j.contents[0].split(",")[0].strip() for j in investors])
    if spacy_labels:
        parsed_investors.extend(spacy_labels)
    if not parsed_investors:
        return False
    return parsed_investors


def parse_funds(p):
    funds = [funds_extractor(text) for text in p.contents]
    funds = reduce(iconcat, funds, [])
    return funds


def parse_series(p):
    series = [series_extractor(text) for text in p.contents]
    series = [serie for serie in series if serie != ""]
    return series


def parse_datetitle(raw_metadata):
    try:
        date_temp = raw_metadata["date"][0]["datetime"]
    except:
        date_temp = ""
    return {
        "date": date_temp,
        "title": raw_metadata["title"].text
    }
