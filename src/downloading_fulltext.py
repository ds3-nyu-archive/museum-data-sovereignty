#!/usr/bin/env python

from bs4 import BeautifulSoup
import json
import pathlib
from os import path
from data_retrieval import open_url

def save_fulltext(url, index):
    
    '''
    Takes in fulltext URL and index.
    Saves .json file with full-text, in unparsed format and separated by heading.
    '''
    
    file_name = index+'.json'
    file_path = pathlib.Path.cwd().parent / 'datasets' / 'downloaded_entries'/ 'fulltext' /file_name

    if path.exists(file_path):
        return

    html = open_url(url)
    soup = BeautifulSoup(html, 'xml')
    
    # get full text, not seperated by heading
    # safest option, least likely to lose any info this way
    messy_full = soup.get_text()
    
    #initialize all heading sections to 'Null'
    agency1 = 'Null'
    sub_agency1 = 'Null'
    dep_doc = 'Null'
    subject = 'Null'
    agency2 = 'Null'
    action = 'Null'
    summary = 'Null'
    dates = 'Null'
    addresses = 'Null'
    signature_dated = 'Null'
    signature_name = 'Null'
    signature_title = 'Null'
    fr_doc = 'Null'
    billing_code = 'Null'
    supp_info = 'Null'
    consultation = 'Null'
    h_d_r = 'Null'
    h_d_ci = 'Null'
    determinations = 'Null'
    a_r_d = 'Null'
    
    if soup.find('AGENCY') != None:
        agency1 = soup.AGENCY.get_text() # difference between agency1 and agency2?
    if soup.find('SUBAGY') != None:
        sub_agency1 = soup.SUBAGY.get_text()
    if soup.find('DEPDOC')!= None:
        dep_doc = soup.DEPDOC.get_text()
    if soup.find('SUBJECT') != None:
        subject = soup.SUBJECT.get_text()
    if soup.find('AGY') != None:
        agency2 = soup.AGY.P.get_text() # difference between agency1 and agency2?
    if soup.find('ACT') != None:
        action = soup.ACT.P.get_text()
    if soup.find('SUM') != None:
        summary = soup.SUM.P.get_text()
    if soup.find('DATES') != None:
        dates = soup.DATES.P.get_text()
    if soup.find('ADD') != None:
        addresses = soup.ADD.P.get_text()
    if soup.find('DATED') != None:
        signature_dated = soup.DATED.get_text() # should we strip 'Dated: ' from beginning?      
    if soup.find('NAME') != None:
        signature_name = soup.NAME.get_text() 
    if soup.find('TITLE') != None:
        signature_title = soup.TITLE.get_text()
    if soup.find('FRDOC') != None:
        fr_doc = soup.FRDOC.get_text()
    if soup.find('BILCOD') != None:
        billing_code = soup.BILCOD.get_text()
        
    if soup.find('SUPLINF') != None:
        supp_info_list = soup.SUPLINF.children
        supp_info = ''
        for i, x in enumerate(supp_info_list):
            #get all text from headings and paragraphs
            #this should skip newline characters and signature info
            #may be missing important things here! should be preserved in messy_full
            if (x.name=='HD') or (x.name=='P'):
                supp_info+= x.get_text() + ' \n ' # concatenate supplementary info into single string
                                                # separate by newline character
                                                # does not remove special characters (eg bullet points)
    
    #populate 4 un-nested categories
                # 'Consultation' 
                # 'History and Description of the Remains' 
                # 'Determinations Made by __________'
                # 'Additional Requesters and Disposition'
    #makes potentially unsafe assumptions re format
    #could be functionized for easier editing
    if soup.find('HD')!=None:
            headings = soup.find_all('HD')
            for x in headings:
                if 'consultation' in x.string.lower():
                    consultation = ''
                    after_consultation = [x for x in list(x.next_siblings) if x.name=='P' or x.name=='HD']
                    for a in after_consultation:
                        if a.name=='P': 
                            consultation+=a.get_text()+' \n '
                            continue
                        if 'SOURCE' in a.attrs:
                            if a['SOURCE'] == "HD1":
                            #assume that "HD1" would mark new section
                            #should debug this with example
                                break
                        consultation+=a.get_text()+' \n '
                        
                if 'history and description of the remains' in x.string.lower():
                    h_d_r = ''
                    after_hdr = [x for x in list(x.next_siblings) if x.name=='P' or x.name=='HD']
                    for a in after_hdr:
                        if a.name=='P': 
                            h_d_r+=a.get_text()+' \n '
                            continue
                        if 'SOURCE' in a.attrs:
                            if a['SOURCE'] == "HD1":
                            #assume that "HD1" would mark new section
                            #should debug this with example
                                break
                        h_d_r+=a.get_text()+' \n '

                if 'history and description of the cultural items' in x.string.lower():
                    h_d_ci = ''
                    after_hdci = [x for x in list(x.next_siblings) if x.name=='P' or x.name=='HD']
                    for a in after_hdci:
                        if a.name=='P': 
                            h_d_ci+=a.get_text()+' \n '
                            continue
                        if 'SOURCE' in a.attrs:
                            if a['SOURCE'] == "HD1":
                            #assume that "HD1" would mark new section
                            #should debug this with example
                                break
                        h_d_ci+=a.get_text()+' \n '
                        
                if 'determinations made by' in x.string.lower():
                    determinations = x.get_text()+' \n ' #include heading because varies based on institution
                    after_det = [x for x in list(x.next_siblings) if x.name=='P' or x.name=='HD']
                    for a in after_det:
                        if a.name=='P': 
                            determinations+=a.get_text() +' \n '
                            continue
                        if 'SOURCE' in a.attrs:
                            if a['SOURCE'] == "HD1":
                            #assume that "HD1" would mark new section
                            #should debug this with example
                                break
                        determinations+=a.get_text() +' \n '
                        
                if 'additional requesters and disposition' in x.string.lower() \
                or 'additional requestors and disposition' in x.string.lower():
                    a_r_d = ''
                    after_ard = [x for x in list(x.next_siblings) if x.name=='P' or x.name=='HD']
                    for a in after_ard:
                        if a.name=='P': 
                            a_r_d+=a.get_text()+' \n '
                            continue
                        if 'SOURCE' in a.attrs:
                            if a['SOURCE'] == "HD1":
                            #assume that "HD1" would mark new section
                            #should debug this with example
                                break
                        a_r_d+=a.get_text()+' \n '
    entry = {'index': index, 'messy_full': messy_full, 'agency1': agency1, 'sub_agency1':sub_agency1, 
            'dep_doc': dep_doc, 'subject': subject, 
            'agency2': agency2, 'action': action, 'summary': summary, 
            'dates': dates, 'addresses': addresses, 
            'signature_dated': signature_dated, 'signature_name': signature_name, 
            'signature_title': signature_title, 
            'fr_doc': fr_doc, 'billing_code': billing_code, 'supp_info': supp_info, 
            'consultation': consultation, 'h_d_r': h_d_r, 'h_d_ci': h_d_ci,
            'determinations': determinations, 'a_r_d': a_r_d}

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entry, f, ensure_ascii=False)               
    return 