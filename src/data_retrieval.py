#!/usr/bin/env python

import requests

def open_url (url):
    
    '''
    Opens URL, returns HTML.
    '''
    
    test_response=requests.get(url) #open url
    html_page_source = str(test_response.content)[2:-1] #access html
    return html_page_source
