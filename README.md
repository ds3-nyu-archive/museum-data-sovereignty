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


## Results and Findings

- #### NAGPRA Database Schema.pdf
   Map of NAGPRA databases.

- #### NAGPRA Database Constellation.key
   Slidedeck with information on NAGPRA databases.

- #### Repeated_Values_Report.pdf
   Report on unexpected text recycling in Notices of Inventory Completion and Notices of Intent to Repatriate.


## Scripts and Notebooks

- #### Controlled Vocabulary Text Mining.ipynb
Get document frequency, context samples, and temporal plots for controlled vocabulary items from Jane. Preliminary stemming analysis of "unidentifiable human remains."

- #### Cleaning inv_url Title.ipynb
Attemps to split inv_urls.csv Title into Institution, City, and State. Three documents dropped from dataset because they are not related to NAGPRA. Cleaned dataset saved. Outstanding issues discussed at end of notebook.

- #### Data_Profiling_and_Cleaning.ipynb
Basis of Repeated_Values_Report.pdf. Runs Pandas Profiling reports on fulltext.pckl.gz and metadata.pckl.gz. Explores corrections and corrections_of columns. Cleans action column of metadata and rewrites cleaned version. Detailed investigation into recycled text.

- #### main.py
Downloads full-text and metadata, saves as individual JSON files. Collects individual JSON files into two dataframes. For downloading, use the option "--dataset" and pass either "inventory" or "repatriation" as an argument. Main will use downloading_fulltext to open, parse, and save the pages at the URLs stored in the fulltext_url column in either inv_urls.csv or repatriation_urls.csv. The script will also use downloading_metadata to open and save the JSON files located at the URLs stored in the json_url column in either inv_urls.csv or repatriation_urls.csv. Downloads are performed in paralell with multiprocessing, and results are stored as individual JSON files in datasets/downloaded_entries/. The keys assigned by indexing.py are preserved. For collecting the individual JSON files, use the option "--type" and pass either "fulltext" or "metadata" as an argument. Main will traverse either datasets/downloaded_entries/fulltext or datasets/downloaded_entries/metadata, opening each JSON file and collecting them into a single dataframe. Results are saved as either metadata.pckl.gz or fulltext.pckl.gz.

- #### Building Notices of Inventory Completion URL Dataset.ipynb 
Builds a dataframe with the 2467 records in the Notices of Inventory Completion table on the National Park Service website, accessed 2/13/20. Adds columns for JSON and full-text URLs by parsing the HTML of each Federal Register document page. The final result is saved as inv_urls.csv.

- #### Building Notices Of Repatriation Dataset.ipynb 
Builds a dataframe with the 815 records in notices_of_repatriation.csv. Adds columns for JSON and full-text URLs by parsing the HTML of each Federal Register document page. The final result is saved as repatriation_urls.csv.

- #### downloading_fulltext.py 
Takes in a URL and a key, and saves a JSON file with the full-text in datasets/downloaded_entries/fulltext/.

- #### downloading_metadata.py 
Takes in a URL and a key, and saves a JSON file with the metadata in datasets/downloaded_entries/metadata/.

- #### indexing.py 
Takes the index of inv_urls.csv, appends each entry with "I_" and saves this key as a new column called key. The resulting dataframe is saved to inv_urls.csv. It does the same to repatriation_urls.csv using "R_" as the prefix for the key.

- #### data_retrieval.py
Takes in a URL and returns the page's HTML.

- #### urlgetter.py
Parses HTML to return URLs of interest.

- #### json keys.ipynb
Loads sample notices via Federal Register API and explores metadata keys.


## Datasets

- #### fulltext.csv
   Full-text of Notices of Inventory Completion and Notices of Intent to Repatriate, compiled from JSON files in datasets/downloaded_entries/fulltext/ via main on 04/03/20. Three records have been removed because they were not relevant to NAGPRA. See Cleaning inv_url Title for details on record removal. See downloading_fulltext for details on attribute construction. The string "Null" is the null value placeholder.

- #### fulltext.pckl.gz
   Pandas DataFrame holding the data from fulltext.csv, pickled with gzip compression. Index has been set to key.

- #### metadata.csv
   Metadata for Notices of Inventory Completion and Notices of Intent to Repatriate, compiled from JSON files in datasets/downloaded_entries/metadata/ via main on 04/03/20. Three records have been removed because they were not relevant to NAGPRA. See Cleaning inv_url Title for details on record removal. All columns are original to Federal Register metadata, except for key, which is a unique primary key consistent with metadata.pckl.gz, fulltext.csv, fulltext.pckl.gz, inv_urls.csv, and repatriation_urls.csv.

- #### metadata.pckl.gz
   Pandas DataFrame holding the data from metadata.csv, pickled with gzip compression. Index has been set to key.

- #### datasets/downloaded_entries/fulltext/
   Holds 3282 individual JSON files with the full-text of each entry in inv_urls.csv and repatriation_urls.csv from the URLs stored in fulltext_url. Includes index field with primary key. Downloaded via main and downloading_fulltext, 3/20/20 - 3/21/20.

- #### datasets/downloaded_entries/metadata/
   Holds 3282 individual JSON files with the metadata of each entry in inv_urls.csv and repatriation_urls.csv from the URLs stored in json_url. Includes index field with primary key. Downloaded via main and downloading_metadata, 04/02/20.

- #### inv_urls
   Each row represents one Notice of Inventory Completion published in the Federal Register and logged in the National Park Service website. Built in Building Notices of Inventory Completion URL Dataset with data accessed from https://www.nps.gov/subjects/nagpra/notices-of-inventory-completion.htm 2/13/20. (Source URL: https://www.nps.gov/common/uploads/sortable_dataset/nagpra/F8663396-E1B9-7C54-8C15C08D2D0702C4/F8663396-E1B9-7C54-8C15C08D2D0702C4.json.) Unique keys created via indexing by appending "I_" to the dataframes index. Three records have been removed because they were not relevant to NAGPRA (see Cleaning inv_url Title).

- #### repatriation_urls
   Each row represents one Notice of Intent to Repatriate published in the Federal Register and logged in the National Park Service website. Built using notices_of_repatriation.csv via Building Notices of Repatriation Dataset on 03/01/2020. Unique keys created via indexing by appending "R_" to the dataframes index.

- #### notices_of_repatriation.csv
   Downloaded from https://www.nps.gov/subjects/nagpra/notices-of-intent-to-repatriate.htm 03/01/2020.

- #### inventories_nps.csv
   Records of inventories for which notices have not been published in the Federal Register. Downloaded directly from https://www.nps.gov/subjects/nagpra/inventories-database.htm 2/13/20.

- #### fedreg_notices_of_inventory.csv
   Notices of Inventory Completion, as downloaded directly from the Federal Register. Truncated; does not contain all records. Details in Building Notices of Inventory Completion URL Dataset. Downloaded from https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=national-park-service&conditions%5Bterm%5D=%22Inventory+Completion%22&conditions%5Btype%5D%5B%5D=NOTICE on 2/13/20.


