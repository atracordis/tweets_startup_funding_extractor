import re


str_url_regex = '(?:http[s]?)?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
url_matcher = re.compile(str_url_regex)

str_money_regex = r'\p{Sc}\s?\d+(?:\.\d+)?\s?(?:million|billion|M|m|B|b|Million|Billion)?(?:\s(?:dollars|euros|pounds|USD|EUR|GBP))?'

str_series_regex = 'seed|series [A-Z]|mezzanine|IPO|public'
series_matcher = re.compile(str_series_regex, re.IGNORECASE)

str_unit_regex = 'million|billion|M|B'
unit_matcher = re.compile(str_unit_regex, re.IGNORECASE)

str_amount_regex = '[0-9]+(?:,|\.)?[0-9]*'
amount_matcher = re.compile(str_amount_regex, re.IGNORECASE)

str_currency_regex = r'\p{Sc}|(?:dollars|euros|pounds|USD|EUR|GBP)'
