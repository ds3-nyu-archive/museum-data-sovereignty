# Museum Studies: Data sovereignty

- PIs: Jane Anderson and Deena Engel
- Student: Alene Rhea
- Advisor: Sinclert Pérez


## Project Description
Internationally, questions of ethics and equity, especially in relation to responsible sharing of data across multiple national platforms, are creating a new range of issues for researchers in the science, innovation and cultural heritage sectors. The Indigenous Data Sovereignty movement is at the forefront of asking what data ethics and equity means for Indigenous peoples. This project initiates the process of developing a means for Indigenous peoples to track and find their cultural heritage within museums, archives and libraries nationally and internationally.

Our pilot project examining over 4,000 public records on Native American cultural material from museums, libraries and archives nationally is geared towards building an Indigenous Data Detection Algorithm (IDDA) to assist Indigenous communities regain control and authority over their data, which in turn will also assist communities to locate the associated cultural materials.


## Goals
- Museum studies class will think about ethical issues (sensitive reports, ancestors information...).
- Jane will develop a protocol for thinking and sharing about information, using appropriate terms.


## Datasets

#### fulltext.csv
Full-text of Notices of Inventory Completion and Notices of Intent to Repatriate, compiled from JSON files in datasets/downloaded_entries/fulltext/ via main on 04/03/20. Three records have been removed because they were not relevant to NAGPRA. See Cleaning inv_url Title for details on record removal. See downloading_fulltext for details on attribute construction. The string "Null" is the null value placeholder. <br/>
**Rows: 3279**<br/>
**messy_full** - Type: str. Broad, catch-call category that contains all text present in notice, for all documents in the dataset. Except for key, all other attributes ought to be subsets of this one.<br/>
**agency1** - Type: str. From AGENCY tag in XML documents. Will be "Null" in old basic text documents.<br/>
**sub_agency1** - Type: str. From SUBAGY tag in XML documents. Will be "Null" in old basic text documents.<br/>
**dep_doc** - Type: str. From DEPDOC tag in XML documents. Will be "Null" in old basic text documents.<br/>
**subject** - Type: str. From SUBJECT tag in XML documents. Will be "Null" in old basic text documents.<br/>
**agency2** - Type: str. From AGY tag in XML documents. Will be "Null" in old basic text documents.<br/>
**action** - Type: str. From ACT tag in XML documents. Will be "Null" in old basic text documents.<br/>
**summary** - Type: str. From SUM tag in XML documents. Will be "Null" in old basic text documents.<br/>
**dates** - Type: str. From DATES tag in XML documents. Will be "Null" in old basic text documents.<br/>
**addresses** - Type: str. From ADD tag in XML documents. Will be "Null" in old basic text documents.<br/>
**signature_dated** - Type: str. From DATED tag in XML documents. Will be "Null" in old basic text documents.<br/>
**signature_name** - Type: str. From NAME tag in XML documents. Will be "Null" in old basic text documents.<br/>
**signature_title** - Type: str. From TITLE tag in XML documents. Will be "Null" in old basic text documents.<br/>
**fr_doc** - Type: str. From FRDOC tag in XML documents. Will be "Null" in old basic text documents.<br/>
**billing_code** - Type: str. From BILCOD tag in XML documents. Will be "Null" in old basic text documents.<br/>
**supp_info** - Type: str. Supplementary Information. Text and headings of all children of SUPLINF tag in XML documents, concatenated into a single string and separated by newline characters. consultation, h_d_r, h_d_ci, determinations, and a_r_d ought to be subsets of suppo_info. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full.<br/>
**consultation** - Type: str. Consultation. Begins after "Consultation" heading within Supplementary Information, if present. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full.<br/>
**h_d_r** - Type: str. History and Description of the Remains. Begins after "History and Description of the Remains" heading within Supplementary Information, if present. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full. Present only in Notices of Inventory Completion, will be "Null" in Notices of Intent to Repatriate.<br/>
**h_d_ci** - Type: str. History and Description of the Cultural Items. Begins after "History and Description of the Cultural Items" heading within Supplementary Information, if present. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full. Present only in Notices of Inventory Completion, will be "Null" in Notices of Intent to Repatriate.<br/>
**determinations** - Type: str. Determinations Made by [Institution]. Begins with "History and Description" heading within Supplementary Information, if present. Heading included because it varies. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full.<br/>
**a_r_d** - Type: str. Additional Requestors and Disposition. Begins after "Additional Requestors and Disposition" heading within Supplementary Information, if present. "Requesters" is also accepted. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full.<br/>
**key** - Type: str. Unique primary key consistent with fulltext.pckl.gz, metadata.pckl.gz, metadata.csv, inv_urls.csv, and repatriation_urls.csv.<br/>

#### fulltext.pckl.gz
Pandas DataFrame holding the data from fulltext.csv, pickled with gzip compression. Index has been set to key.<br/>
**Rows: 3279**<br/>
**Columns: messy_full, agency1, sub_agency1, dep_doc, subject, agency2, action, summary, dates, addresses, signature_dated, signature_name, signature_title, fr_doc, billing_code, supp_info, consultation, h_d_r, h_d_ci, determinations, a_r_d**<br/>

#### metadata.csv
Metadata for Notices of Inventory Completion and Notices of Intent to Repatriate, compiled from JSON files in datasets/downloaded_entries/metadata/ via main on 04/03/20. Three records have been removed because they were not relevant to NAGPRA. See Cleaning inv_url Title for details on record removal. All columns are original to Federal Register metadata, except for key, which is a unique primary key consistent with metadata.pckl.gz, fulltext.csv, fulltext.pckl.gz, inv_urls.csv, and repatriation_urls.csv.<br/>
**Rows: 3279**<br/>
**Columns: abstract, action, agencies, body_html_url, cfr_references, citation, comment_url, comments_close_on, correction_of, corrections, dates, disposition_notes, docket_ids, document_number, effective_on, end_page, executive_order_notes, executive_order_number, full_text_xml_url, html_url, images, json_url, mods_url, page_length, page_views, pdf_url, presidential_document_number, proclamation_number, public_inspection_pdf_url, publication_date, raw_text_url, regulation_id_number_info, regulation_id_numbers, regulations_dot_gov_info, regulations_dot_gov_url, significant, signing_date, start_page, subtype, title, toc_doc, toc_subject, topics, type, volume, key**<br/>

#### metadata.pckl.gz
Pandas DataFrame holding the data from metadata.csv, pickled with gzip compression. Index has been set to key.<br/>
**Rows: 3279**<br/>
**Columns: abstract, action, agencies, body_html_url, cfr_references, citation, comment_url, comments_close_on, correction_of, corrections, dates, disposition_notes, docket_ids, document_number, effective_on, end_page, executive_order_notes, executive_order_number, full_text_xml_url, html_url, images, json_url, mods_url, page_length, page_views, pdf_url, presidential_document_number, proclamation_number, public_inspection_pdf_url, publication_date, raw_text_url, regulation_id_number_info, regulation_id_numbers, regulations_dot_gov_info, regulations_dot_gov_url, significant, signing_date, start_page, subtype, title, toc_doc, toc_subject, topics, type, volume**<br/>

#### datasets/downloaded_entries/fulltext/
Holds 3282 individual JSON files with the full-text of each entry in inv_urls.csv and repatriation_urls.csv from the URLs stored in fulltext_url. Includes index field with primary key. Downloaded via main and downloading_fulltext, 3/20/20 - 3/21/20.<br/>

#### datasets/downloaded_entries/metadata/
Holds 3282 individual JSON files with the metadata of each entry in inv_urls.csv and repatriation_urls.csv from the URLs stored in json_url. Includes index field with primary key. Downloaded via main and downloading_metadata, 04/02/20.<br/>

#### inv_urls
Each row represents one Notice of Inventory Completion published in the Federal Register and logged in the National Park Service website. Built in Building Notices of Inventory Completion URL Dataset with data accessed from https://www.nps.gov/subjects/nagpra/notices-of-inventory-completion.htm 2/13/20. (Source URL: https://www.nps.gov/common/uploads/sortable_dataset/nagpra/F8663396-E1B9-7C54-8C15C08D2D0702C4/F8663396-E1B9-7C54-8C15C08D2D0702C4.json.) Unique keys created via indexing by appending "I_" to the dataframes index. Three records have been removed because they were not relevant to NAGPRA (see Cleaning inv_url Title).<br/>
**Rows: 2464**<br/>
**Publication Date** - Type: str. Original column from NPS. Format: m/d/yyy<br/>
**Title** - Type: str. Original column from NPS. Standard format: [Institution], [City], [State, 2-letter abbreviation]. Format for older records: "Notice of Inventory Completion for Native American Human Remains and Associated Funerary Objects from [Geographic region of provenance] in the Possession of [Institution in Possession], [City], [State, 2-letter abbreviation], and in the Control of [Controlling Institution]"<br/>
**Link** - Type: str. Original column from NPS. Link to Federal Register document.<br/>
**json_url** - Type: str. Link to metadata in JSON format. Added via Building Notices of Inventory Completion URL Dataset. <br/>
**fulltext_url** - Type: str. Link to full-text data stored in XML or basic text format. Added via Building Notices of Inventory Completion URL Dataset.<br/>
**key** - Type: str. Primary key. Begins with "I_" to distiguish from Notices of Intent to Repatriate. Added via indexing. Number following "I_" no longer matches iloc, because records have been removed.<br/>
**Institution** - Type: str. Partially processed institutional information from Title. Added via Cleaning inv_url Title. See notebook for outstanding issues.<br/>
**City** - Type: str. Partially processed information on location of Institution, as derived from Title. Added via Cleaning inv_url Title. See notebook for outstanding issues.<br/>
**State** - Type: str. U.S. state where Institution is located, as derived from Title.  Format: 2-letter abbreviation. Added via Cleaning inv_url Title.<br/>
**Correction** - Type: int. Correction status, as derived from Title. Value of 0 indicates that notice is not a correction. Value of 1 indicates a first correction. Value of 2 indicates a second correction. Has not been checked against Federal Register documents or MODS. Added via Cleaning inv_url Title.<br/>

#### repatriation_urls
Each row represents one Notice of Intent to Repatriate published in the Federal Register and logged in the National Park Service website. Built using notices_of_repatriation.csv via Building Notices of Repatriation Dataset on 03/01/2020. Unique keys created via indexing by appending "R_" to the dataframes index.<br/>
**Rows: 815**<br/>
**Publication Date** - Type: str. Original column from NPS. Format: m/d/yyy<br/>
**Title** - Type: str. Original column from NPS. Approximate format: [Institution], [City], [State, 2-letter abbreviation]<br/>
**Link** - Type: str. Original column from NPS. Link to Federal Register document.<br/>
**json_url** - Type: str. Link to metadata in JSON format. Added via Building Notices of Inventory Completion URL Dataset.<br/>
**fulltext_url** - Type: str. Link to full-text data stored in XML or basic text format. Added via Building Notices of Inventory Completion URL Dataset.<br/> 
**key** - Type: str. Primary key. Begins with "R_" to distiguish from Notices of Inventory completion. Added via indexing.<br/>

#### notices_of_repatriation.csv
Downloaded from https://www.nps.gov/subjects/nagpra/notices-of-intent-to-repatriate.htm 03/01/2020.<br/>
**Rows: 815**<br/>
**Columns: Publication Date, Title, Link**<br/>

#### inventories_nps.csv
Records of inventories for which notices have not been published in the Federal Register. Downloaded directly from https://www.nps.gov/subjects/nagpra/inventories-database.htm 2/13/20.<br/>
**Rows: 14825**<br/>
**Columns: State, Museum or Federal Agency, MNI, AFO, CA, CUI, Geographic Area, County**<br/>

#### fedreg_notices_of_inventory.csv
Notices of Inventory Completion, as downloaded directly from the Federal Register. Truncated; does not contain all records. Details in Building Notices of Inventory Completion URL Dataset. Downloaded from https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=national-park-service&conditions%5Bterm%5D=%22Inventory+Completion%22&conditions%5Btype%5D%5B%5D=NOTICE on 2/13/20.<br/>
**Rows: 1000**<br/>
**Columns:title, type, agency_names, abstract, document_number, html_url, pdf_url, publication_date**<br/><br/>




## Scripts and Notebooks

#### Controlled Vocabulary Text Mining.ipynb
Get document frequency, context samples, and temporal plots for controlled vocabulary items from Jane. Preliminary stemming analysis of "unidentifiable human remains."

#### Cleaning inv_url Title.ipynb
Attemps to split inv_urls.csv Title into Institution, City, and State. Three documents dropped from dataset because they are not related to NAGPRA. Cleaned dataset saved. Outstanding issues discussed at end of notebook.

#### Data_Profiling_and_Cleaning.ipynb
Basis of Repeated_Values_Report.pdf. Runs Pandas Profiling reports on fulltext.pckl.gz and metadata.pckl.gz. Explores corrections and corrections_of columns. Cleans action column of metadata and rewrites cleaned version. Detailed investigation into recycled text.

#### main.py
Downloads full-text and metadata, saves as individual JSON files. Collects individual JSON files into two dataframes. For downloading, use the option "--dataset" and pass either "inventory" or "repatriation" as an argument. Main will use downloading_fulltext to open, parse, and save the pages at the URLs stored in the fulltext_url column in either inv_urls.csv or repatriation_urls.csv. The script will also use downloading_metadata to open and save the JSON files located at the URLs stored in the json_url column in either inv_urls.csv or repatriation_urls.csv. Downloads are performed in paralell with multiprocessing, and results are stored as individual JSON files in datasets/downloaded_entries/. The keys assigned by indexing.py are preserved. For collecting the individual JSON files, use the option "--type" and pass either "fulltext" or "metadata" as an argument. Main will traverse either datasets/downloaded_entries/fulltext or datasets/downloaded_entries/metadata, opening each JSON file and collecting them into a single dataframe. Results are saved as either metadata.pckl.gz or fulltext.pckl.gz.

#### Building Notices of Inventory Completion URL Dataset.ipynb 
Builds a dataframe with the 2467 records in the Notices of Inventory Completion table on the National Park Service website, accessed 2/13/20. Adds columns for JSON and full-text URLs by parsing the HTML of each Federal Register document page. The final result is saved as inv_urls.csv.

#### Building Notices Of Repatriation Dataset.ipynb 
Builds a dataframe with the 815 records in notices_of_repatriation.csv. Adds columns for JSON and full-text URLs by parsing the HTML of each Federal Register document page. The final result is saved as repatriation_urls.csv.

#### downloading_fulltext.py 
Takes in a URL and a key, and saves a JSON file with the full-text in datasets/downloaded_entries/fulltext/.

#### downloading_metadata.py 
Takes in a URL and a key, and saves a JSON file with the metadata in datasets/downloaded_entries/metadata/.

#### indexing.py 
Takes the index of inv_urls.csv, appends each entry with "I_" and saves this key as a new column called key. The resulting dataframe is saved to inv_urls.csv. It does the same to repatriation_urls.csv using "R_" as the prefix for the key.

#### data_retrieval.py
Takes in a URL and returns the page's HTML.

#### urlgetter.py
Parses HTML to return URLs of interest.

#### json keys.ipynb
Loads sample notices via Federal Register API and explores metadata keys.


## Results and Findings

#### NAGPRA Database Schema.pdf
Map of NAGPRA databases.

#### NAGPRA Database Constellation.key
Slidedeck with information on NAGPRA databases.

#### Repeated_Values_Report.pdf
Report on unexpected text recycling in Notices of Inventory Completion and Notices of Intent to Repatriate.