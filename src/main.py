import click
import sys
import os
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
        url_df = pd.read_csv(data_path)
    if dataset=='repatriation':
        data_path = pathlib.Path.cwd().parent / 'datasets' / 'repatriation_urls.csv'
        url_df = pd.read_csv(data_path)
    if dataset=='fulltext':
        directory_path = pathlib.Path.cwd().parent / 'datasets/downloaded_entries/fulltext'
    if dataset=='metadata':
        directory_path = pathlib.Path.cwd().parent / 'datasets/downloaded_entries/metadata'
    
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

    if task=='collect':
        files = os.listdir(directory_path)
        out_file = pathlib.Path.cwd().parent / 'datasets' / (dataset+'.pckl.gz')
        df=pd.DataFrame()
        for i,f in enumerate(files):
            if f=='.DS_Store':
                continue
            in_file = directory_path / f
            data = pd.read_json(in_file, lines=True)
            df = df.append(data, ignore_index = True)
            print(str(i+1)+' out of '+str(len(files))+' files completed.')
        df.set_index('index', inplace=True)
        df.to_pickle(out_file, compression='gzip')
    

