from resources.regex_utils import *
import regex


def funds_extractor(text):
    """
    extracts funds with regex
    :param text:
    :return:
    """
    try:
        return regex.findall(str_money_regex, text)
    except:
        return ""


def url_extractor(text, url_matcher=url_matcher):
    """
    extracts url with regex
    :param text:
    :param url_matcher:
    :return:
    """
    try:
        return url_matcher.findall(text)[0]
    except:
        return ""


def series_extractor(text, series_matcher=series_matcher):
    """
    extract series with regex
    :param text:
    :param series_matcher:
    :return:
    """
    try:
        return series_matcher.findall(text)[0]
    except:
        return ""


def unit_extractor(text, unit_matcher=unit_matcher):
    """
    extract unit with regex
    :param text:
    :param unit_matcher:
    :return:
    """
    try:
        return unit_matcher.findall(text)[0]
    except:
        return ""


def amount_extractor(text, amount_matcher=amount_matcher):
    """
    extract amount of money with regex
    :param text:
    :param amount_matcher:
    :return:
    """
    try:
        return float(amount_matcher.findall(text)[0].replace(",", "."))
    except:
        return ""


def currency_extractor(text):
    """
    extract currency with regex
    :param text:
    :return:
    """
    try:
        return regex.findall(str_currency_regex, text)[0]
    except:
        return ""
