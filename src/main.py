import click
import sys
import numpy as np
import pandas as pd
import pathlib
import requests
import json
from data_retrieval import open_url
from downloading_fulltext import save_fulltext
from downloading_metadata import save_json
import multiprocessing

task = sys.argv[1]
dataset = sys.argv[2]

if __name__ == "__main__":
    if dataset=='inventory':
            data_path = pathlib.Path.cwd().parent / 'datasets' / 'inv_urls.csv'
    if dataset=='repatriation':
            data_path = pathlib.Path.cwd().parent / 'datasets' / 'repatriation_urls.csv'
    url_df = pd.read_csv(data_path)
    if task=='fulltext':
        input = list(zip(url_df['fulltext_url'], url_df['key']))
        workers = multiprocessing.cpu_count()*2
        chunksize = int(len(input)/workers)
        p = multiprocessing.Pool(workers)
        p.starmap(save_fulltext, input, chunksize)
        p.close
    if task=='metadata':
        input = list(zip(url_df['json_url'], url_df['key']))
        workers = multiprocessing.cpu_count()*2
        chunksize = int(len(input)/workers)
        p = multiprocessing.Pool(workers)
        p.starmap(save_json, input, chunksize)
        p.close
    

