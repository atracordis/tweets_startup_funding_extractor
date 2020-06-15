from resources.regex_utils import *
import regex


def funds_extractor(text):
    try:
        return regex.findall(str_money_regex, text)
    except:
        return ""


def url_extractor(text, url_matcher=url_matcher):
    try:
        return url_matcher.findall(text)[0]
    except:
        return ""


def series_extractor(text, series_matcher=series_matcher):
    try:
        return series_matcher.findall(text)[0]
    except:
        return ""


def unit_extractor(text, unit_matcher=unit_matcher):
    try:
        return unit_matcher.findall(text)[0]
    except:
        return ""


def amount_extractor(text, amount_matcher=amount_matcher):
    try:
        return float(amount_matcher.findall(text)[0].replace(",", "."))
    except:
        return ""


def currency_extractor(text):
    try:
        return regex.findall(str_currency_regex, text)[0]
    except:
        return ""
