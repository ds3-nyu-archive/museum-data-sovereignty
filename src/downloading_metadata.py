import json
import pathlib
from data_retrieval import open_url

def save_json(url, index):
    html = open_url(url)
    entry = json.loads(html.replace('\\', ''), strict=False) #remove json escape characters
    file_name = index+'.json'
    file_path = pathlib.Path.cwd().parent / 'datasets' / 'downloaded_entries'/ 'metadata' /file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entry, f, ensure_ascii=False)               
    return 