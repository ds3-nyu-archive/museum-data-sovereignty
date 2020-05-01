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
### datasets/downloaded_entries/fulltext
Contains individual JSON files with the full-text of each entry in 'inv_urls' and 'repatriation_urls.' Includes 'index' field with primary key. Downloaded via 'main.py' and 'downloading_fulltext.py' 3/20/20 - 3/21/20.

### datasets/downloaded_entries/metadata
Contains individual JSON files with the metadata of each entry in 'inv_urls' and 'repatriation_urls.' Includes 'index' field with primary key. Downloaded via 'main.py' and 'downloading_metadata.py' 04/02/20.

### fedreg_notices_of_inventory.csv
Notices of Inventory Completion, as downloaded directly from the Federal Register. Truncated; does not contain all records. Details in 'Building Notices of Inventory Completion URL Dataset.ipynb.' Downloaded from https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=national-park-service&conditions%5Bterm%5D=%22Inventory+Completion%22&conditions%5Btype%5D%5B%5D=NOTICE 2/13/20.<br/>
**Rows: 1000**<br/>
**Columns:'title', 'type', 'agency_names', 'abstract', 'document_number', 'html_url', 'pdf_url', 'publication_date'**

### fulltext.pckl.gz
Pickled Pandas DataFrame compiled from inventory and repatriation files in 'datasets/downloaded_entries/fulltext' 04/03/20. Three records have been removed because they were not relevant to NAGPRA (see 'Cleaning inv_url Title.ipynb').<br/>
**Rows:**<br/>
**Columns:**

### inv_urls
Each row represents one Notice of Inventory Completion published in the Federal Register and logged in the National Park Service website. Built in 'Building Notices of Inventory Completion URL Dataset.ipynb' with data accessed from https://www.nps.gov/subjects/nagpra/notices-of-inventory-completion.htm 2/13/20. (Source URL: https://www.nps.gov/common/uploads/sortable_dataset/nagpra/F8663396-E1B9-7C54-8C15C08D2D0702C4/F8663396-E1B9-7C54-8C15C08D2D0702C4.json.) Unique keys created via 'indexing.py' by appending "I_" to the dataframe's index. Three records have been removed because they were not relevant to NAGPRA (see 'Cleaning inv_url Title.ipynb').<br/>
**Rows: 2464**<br/>
**Columns:**<br/>
**'Publication Date'** - Type: str. Original column from NPS. Format: m/d/yyy<br/>
**'Title'** - Type: str. Original column from NPS. Standard format: [Institution], [City], [State, 2-letter abbreviation]. Format for older records: "Notice of Inventory Completion for Native American Human Remains and Associated Funerary Objects from [Geographic region of provenance] in the Possession of [Institution in Possession], [City], [State, 2-letter abbreviation], and in the Control of [Controlling Institution]"<br/>
**'Link'** - Type: str. Original column from NPS. Link to Federal Register document.<br/>
**'json_url'** - Type: str. Link to metadata in JSON format. Added via 'Building Notices of Inventory Completion URL Dataset.ipynb.' <br/>
**'fulltext_url'** - Type: str. Link to full-text data stored in XML or basic text format. Added via 'Building Notices of Inventory Completion URL Dataset.ipynb.'<br/>
**'key'** - Type: str. Primary key. Begins with 'I_' to distiguish from Notices of Intent to Repatriate. Added via 'indexing.py.' Number following 'I_' no longer matches iloc, records have been removed.<br/>
**'Institution'** - Type: str. Partially processed institutional information from 'Title.' Added via 'Cleaning inv_url Title.ipynb.' See notebook for outstanding issues.<br/>
**'City'** - Type: str. Partially processed information on location of 'Institution,' as derived from 'Title.' Added via 'Cleaning inv_url Title.ipynb.' See notebook for outstanding issues.<br/>
**'State'** - Type: str. U.S. state where 'Institution' is located, as derived from 'Title.'  Format: 2-letter abbreviation. Added via 'Cleaning inv_url Title.ipynb.'<br/>
**'Correction'** - Type: int. Correction status, as derived from 'Title.' Value of 0 indicates that notice is not a correction. Value of 1 indicates a first correction. Value of 2 indicates a second correction. Has not been checked against Federal Register documents or MODS. Added via 'Cleaning inv_url Title.ipynb.'

### inventories_nps.csv
Records of inventories for which notices have not been published in the Federal Register. Downloaded from https://www.nps.gov/subjects/nagpra/inventories-database.htm 2/13/20.<br/>
**Rows: 14825**<br/>
**Columns: 'State', 'Museum or Federal Agency', 'MNI', 'AFO', 'CA', 'CUI', 'Geographic Area', 'County'**

### metadata.pckl.gz
Pickled Pandas DataFrame compiled from inventory and repatriation files in 'datasets/downloaded_entries/metadata' 04/03/20. Three records have been removed because they were not relevant to NAGPRA (see 'Cleaning inv_url Title.ipynb').<br/>
**Rows:**<br/>
**Columns:**

### notices_of_repatriation.csv
[description] [source/url] [download date]<br/>
**Rows: 825**<br/>
**Columns: 'Publication Date', 'Title', 'Link'**

### repatriation_urls
Each row represents one Notice of Intent to Repatriate published in the Federal Register and logged in the National Park Service website. Built in 'Building Notices of Inventory Completion URL Dataset.ipynb' with data accessed from https://www.nps.gov/subjects/nagpra/notices-of-intent-to-repatriate.htm on [date]. (Source URL: [url].) Unique keys created via 'indexing.py' by appending "R_" to the dataframe's index.<br/>
**Rows: 815**<br/>
**Columns:**<br/>
**'Publication Date'** - Type: str. Original column from NPS. Format: m/d/yyy<br/>
**'Title'** - Type: str. Original column from NPS. Approximate format: [Institution], [City], [State, 2-letter abbreviation]<br/>
**'Link'** - Type: str. Original column from NPS. Link to Federal Register document.<br/>
**'json_url'** - Type: str. Link to metadata in JSON format. Added via 'Building Notices of Inventory Completion URL Dataset.ipynb.'<br/>
**'fulltext_url'** - Type: str. Link to full-text data stored in XML or basic text format. Added via 'Building Notices of Inventory Completion URL Dataset.ipynb.'<br/> 
**'key'** - Type: str. Primary key. Begins with 'R_' to distiguish from Notices of Inventory completion. Added via 'indexing.py.'<br/>


## Scripts and Notebooks
'Building Notices of Inventory Completion URL Dataset.ipynb' builds a dataframe with the 2467 records in the Notices of Inventory table on the National Park Service website, accessed 2/13/20. It then calls urlgetter.py to add columns for JSON and full text URLs. The final result is saved as 'inv_urls.csv.'

'Building Notices Of Repatriation Dataset.ipynb' [functional explanation]

'indexing.py' takes the index of 'inv_urls.csv,' appends each entry with 'I_,' and saves this key as a new column called 'key.' The resulting dataframe is saved to 'inv_urls.csv.' It does the same to 'repatriation_urls.csv' using 'R_' as the prefix for the key.

'main.py' takes 2 arguments, task and dataset. If the dataset argument is given as 'inventory,' the script reads in 'inv_urls.csv.' If the dataset argument is given as 'repatriation,' the script reads in 'repatriation_urls.csv.' If the task argument is given as 'fulltext,' the script passes each entry's key and full-text URL to 'downloading_fulltext.py.' If the task argument is given as 'metadata,' the script passes each entry's key and JSON URL to 'downloading_json.py.' If task is given as 'collect', and the dataset is given as 'fulltext', then downloaded JSON files from the 'fulltext' task, for both inventory and repatriation, are compiled into a single DataFrame and saved as 'fulltext.pckl.gz.' If task is given as 'collect', and the dataset is given as 'metadata', then downloaded JSON files from the 'metadata' task, for both inventory and repatriation, are compiled into a single DataFrame and saved as 'metadata.pckl.gz.' 

'downloading_metadata.py' takes in a URL and a key, and saves a JSON file with the metadata in 'datasets/downloaded_entries/metadata.'

'downloading_fulltext.py' takes in a URL and a key, and saves a JSON file with the full-text in 'datasets/downloaded_entries/fulltext.'

'data_retrieval.py' takes in a URL and returns the page's HTML.