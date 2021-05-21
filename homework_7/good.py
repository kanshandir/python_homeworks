"""
Ready implementation of bad.py
See the task in good.py
"""
import logging
from collections import defaultdict
from typing import Dict, List

import requests

logging.basicConfig(level=logging.INFO)

# https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json


class SomeClass:
    def __init__(self, url, page=1):
        self.url = url
        self.page = page

    def __len__(self):
        return len(self.url)

    def __getitem__(self):
        responce = requests.get(f"{self.url}&page={self.page}")
        make_dict = responce.json()
        if not make_dict['Count']:
            raise StopIteration
        self.page += 1

    def create_country_make_dict(self, make_dict):
        country_manufacturers: Dict[str, List[str]] = defaultdict(list)
        for manufacturer in make_dict["Results"]:
            country = manufacturer["Country"]
            if country:
                country_manufacturers[country].append(manufacturer["Mfr_Name"])
            logging.info(f"Done with page {self.page}")
        return country_manufacturers