# -*- coding: utf-8 -*-
"""
@created on: 4/16/20,
@author: Shreesha N,
@version: v0.0.1
@system name: badgod
Description:

..todo::

"""

import json
import requests
import pandas as pd
from covid19.data_scrapers.data_sources import JHUTimeSeries

country = {

}

country_stats = {

}


def download_csv(url):
    try:
        df = pd.read_csv(url, error_bad_lines=False)
        if df is None or len(df) == 0:
            raise Exception("CSV downloaded from the URL is empty")
        return df
    except Exception as e:
        print(e)


def get_schema():
    pass


if __name__ == '__main__':
    confirmed_global = download_csv(JHUTimeSeries.CONFIRMED_GLOBAL)
    confirmed_us = download_csv(JHUTimeSeries.CONFIRMED_US)
    deaths_global = download_csv(JHUTimeSeries.DEATHS_GLOBAL)
    deaths_us = download_csv(JHUTimeSeries.DEATHS_US)
    recovered_global = download_csv(JHUTimeSeries.RECOVERED_GLOBAL)
