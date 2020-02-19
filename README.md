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

## Dataset-Building Workflow
'Building Notices of Inventory Completion URL Dataset.ipynb' builds a dataframe with the 2467 records in the Notices of Inventory table on the National Park Service website, accessed 2/13/20. It then calls urlgetter.py to add columns for JSON and full text URLs. The final result is saved as 'inv_urls.csv.'

Downloading_JSON.py [not yet created] will read in 'inv_urls.csv' and load fields of interest into the dataframe. It will save the result as 'inv_meta.csv.' This script should be flexible enough to work on the Notices of Intent to Repatriate dataset as well.

Downloading_fulltext.py [not yet created on master] will read in 'inv_urls.csv' and load the full text into the dataframe. It will save the result as 'inv_full.csv.' This script should be flexible enough to work on the Notices of Intent to Repatriate dataset as well.

The results of Downloading_JSON.py and Downloading_fulltext.py could eventually be merged. We should keep the index consistent in case we keep them as separate tables.

This process will be repeated for Notices of Intent to Repatriate.