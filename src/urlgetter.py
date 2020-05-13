#!/usr/bin/env python

from bs4 import BeautifulSoup
#import sys
#html_page_source=sys.argv[1]

def get_urls (html):
    '''
    Parses HTML to return URLs of interest
    (i.e., links to pages with JSON and with full text)
    '''
    soup = BeautifulSoup(html, "html.parser")
    fulltext_url = None
    json_url = None
    for link in soup.find_all('a'):
        if link.string == None:
            continue
        if fulltext_url != None and json_url != None:
            break
        if link.string == 'JSON: Normalized attributes and metadata':
            json_url = link.get('href')

        '''
        could refine logic here. "text" covers 
        "XML: Original full text XML" 
        as well as "basic text format"
        '''
        if 'text' in link.string.lower():
            fulltext_url = link.get('href')
    return json_url, fulltext_url