import pandas as pd
import pathlib

inv_path = pathlib.Path.cwd().parent / 'datasets' / 'inv_urls.csv'
inv_urls = pd.read_csv(inv_path)

inv_urls['key'] = inv_urls.index
inv_urls['key'] = 'I_'+inv_urls['key'].astype('str')

#overwrite inv_urls.csv with new index column
inv_urls.to_csv(inv_path, index=False)

repat_path = pathlib.Path.cwd().parent / 'datasets' / 'repatriation_urls.csv'
repat_urls = pd.read_csv(repat_path)

repat_urls['key'] = repat_urls.index
repat_urls['key'] = 'R_'+repat_urls['key'].astype('str')

#overwrite repatriation_urls.csv with new index column
repat_urls.to_csv(repat_path, index=False)