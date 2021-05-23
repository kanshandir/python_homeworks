"""
NHTSA has a public api; the url we will be working with is
https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&page=1
This api endpoint returns JSON; it has the field 'Results' - a list of car manufacturers with details.
We want to create a dictionary with country as a key, and list of manufacturer names as a value, e.g:
{
    'USA': ['Tesla', 'Ford', ...],
    'Japan': ['Honda', 'Subaru', ...]
}
Use 'Mfr_Name' as a manufacturer name.
If 'Country' is empty - skip it. We should traverse through all pages of this api endpoint
bad.py has a finished implementation of this task. Your goal is to make this code better, in any
way you can think of. Put your solution in good.py
Some examples of what can be done:
- you can create your own iterator/generator to go through pages for you
- insertion of items into dictionary can be improved
Also, add more tests to the test_dict.py to check response content.
"""
import logging
from collections import defaultdict
from typing import Dict, List

import requests

logging.basicConfig(level=logging.INFO)

# https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json


class PagePaginator:
    def __init__(self, url):
        self.url = url
        self.page = 1
        self.stop = False

    def __getitem__(self, item):
        response = requests.get(f"{self.url}&page={self.page}")
        resp_dict = response.json()
        logging.info(f"Done with page {self.page}")
        if not resp_dict["Count"]:
            self.stop = True
        self.page += 1
        return resp_dict[item]


def create_country_make_dict(url: str):
    country_manufacturers: Dict[str, List[str]] = defaultdict(list)
    page_paginator = PagePaginator(url)
    while not page_paginator.stop:
        for manufacturer in page_paginator["Results"]:
            country = manufacturer["Country"]
            if country:
                country_manufacturers[country].append(manufacturer["Mfr_Name"])
    return country_manufacturers