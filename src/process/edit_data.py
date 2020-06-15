from utils.parsing import *
from resources.const import *


def edit_metadata(parsed_metadata):
    if parsed_metadata == "":
        return ""
    edited_metadata = {}

    funds_not_found = True
    series_not_found = True
    just_found_series = False
    company_name = None
    if 1 in parsed_metadata.keys():
        company_name = parsed_metadata[1].get("name_candidates")

    for i in range(1, max(parsed_metadata.keys()) + 1):
        just_found_series = False
        funds = parsed_metadata[i].get("funds")
        series = parsed_metadata[i].get("series")
        investors = parsed_metadata[i].get("investors")
        if not company_name:
            list_all_investors = []
            for key in parsed_metadata.keys():
                list_all_investors.extend(parsed_metadata[key].get("investors", []))
            list_all_investors = [investor.split("’s")[0] for investor in list_all_investors if len(investor) > 2]
            company_name = max(set(list_all_investors), key=list_all_investors.count)

        if series and series_not_found:
            just_found_series = True
            series_not_found = False
            series = [series_converter[serie.lower()] for serie in series]
            edited_metadata["series"] = inv_series_converter[max(series)]

        if funds and funds_not_found and just_found_series:
            units = [(amount_extractor(fund), unit_extractor(fund), currency_extractor(fund)) for fund in funds]
            units = [(unit[0] * units_converter[unit[1].lower()], unit[2]) for unit in units if
                     unit[0] != "" and unit[1] != ""]
            if units:
                min_amount = min(units)[0]
                min_currency = [unit[1] for unit in units if unit[0] == min_amount][0]
                raised_funds = "{} {}".format(str(min_amount), min_currency)
                edited_metadata["raised_funds"] = raised_funds
                funds_not_found = False
            else:
                series_not_found = True

        if investors and just_found_series:
            investors = [investor.split("’s")[0] for investor in investors if
                         investor != company_name and investor != "IPO" and len(investor) > 2]
            edited_metadata["investors"] = set(investors)

    edited_metadata["date_scraped"] = parsed_metadata[0]["date"]
    if company_name:
        edited_metadata["company_name"] = company_name
    return edited_metadata
