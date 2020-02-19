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
Saving Notices of Inventory Completion.ipynb will call Downloading_JSON.py and Downloading_fulltext.py.
Download_JSON.py will take in page source HTML for Notice of Inventory in Federal Register, and return a 1x?  numpy array with JSON metadata for single record.
Downloading_fulltext.py will will take in page source HTML for Notice of Inventory in Federal Register, and return a 1x? numpy array with full-text for single record.
Saving Notices of Inventory Completion.ipynb will take the outputs from Downloading_JSON.py and Downloading_fulltext.py to build a dataframe.