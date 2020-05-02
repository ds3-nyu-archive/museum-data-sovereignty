# Datasets

### fulltext.csv
Full-text of Notices of Inventory Completion and Notices of Intent to Repatriate, compiled from JSON files in downloaded_entries/fulltext/ via main on 04/03/20. Three records have been removed because they were not relevant to NAGPRA. See Cleaning inv_url Title for details on record removal. See downloading_fulltext for details on attribute construction. The string "Null" is the null value placeholder. <br/>
**Rows: 3279**
- **messy_full**: Broad, catch-call category that contains all text present in notice, for all documents in the dataset. Except for key, all other attributes ought to be subsets of this one. Type: str<br/>
- **agency1**: From AGENCY tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **sub_agency1**: From SUBAGY tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **dep_doc**: From DEPDOC tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **subject**: From SUBJECT tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **agency2**: From AGY tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **action**: From ACT tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **summary**: From SUM tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **dates**: From DATES tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **addresses**: From ADD tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **signature_dated**: From DATED tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **signature_name**: From NAME tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **signature_title**: From TITLE tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **fr_doc**: From FRDOC tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **billing_code**: From BILCOD tag in XML documents. Will be "Null" in old basic text documents. Type: str<br/>
- **supp_info**: Supplementary Information. Text and headings of all children of SUPLINF tag in XML documents, concatenated into a single string and separated by newline characters. consultation, h_d_r, h_d_ci, determinations, and a_r_d ought to be subsets of suppo_info. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full. Type: str<br/>
- **consultation**: Consultation. Begins after "Consultation" heading within Supplementary Information, if present. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full. Type: str<br/>
- **h_d_r**: History and Description of the Remains. Begins after "History and Description of the Remains" heading within Supplementary Information, if present. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full. Present only in Notices of Inventory Completion, will be "Null" in Notices of Intent to Repatriate. Type: str<br/>
- **h_d_ci**: History and Description of the Cultural Items. Begins after "History and Description of the Cultural Items" heading within Supplementary Information, if present. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full. Present only in Notices of Inventory Completion, will be "Null" in Notices of Intent to Repatriate. Type: str<br/>
- **determinations**: Determinations Made by [Institution]. Begins with "History and Description" heading within Supplementary Information, if present. Heading included because it varies. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full. Type: str<br/>
- **a_r_d**: Additional Requestors and Disposition. Begins after "Additional Requestors and Disposition" heading within Supplementary Information, if present. "Requesters" is also accepted. Next paragraphs and headings all concatenated, separated by newline charactesr, until next Heading 1. Note that these formatting assumptions may be unsafe. This attribute has not been rigorously tested, and may be missing or partial, even in XML documents. Will be "Null" in old basic text documents. All information should be preserved in messy_full. Type: str<br/>
- **key**: Unique primary key consistent with fulltext.pckl.gz, metadata.pckl.gz, metadata.csv, inv_urls.csv, and repatriation_urls.csv. Type: str<br/>

### fulltext.pckl.gz
Pandas DataFrame holding the data from fulltext.csv, pickled with gzip compression. Index has been set to key.<br/>
**Rows: 3279**<br/>
**Columns: messy_full, agency1, sub_agency1, dep_doc, subject, agency2, action, summary, dates, addresses, signature_dated, signature_name, signature_title, fr_doc, billing_code, supp_info, consultation, h_d_r, h_d_ci, determinations, a_r_d**<br/>

### metadata.csv
Metadata for Notices of Inventory Completion and Notices of Intent to Repatriate, compiled from JSON files in downloaded_entries/metadata/ via main on 04/03/20. Three records have been removed because they were not relevant to NAGPRA. See Cleaning inv_url Title for details on record removal. All columns are original to Federal Register metadata, except for key, which is a unique primary key consistent with metadata.pckl.gz, fulltext.csv, fulltext.pckl.gz, inv_urls.csv, and repatriation_urls.csv.<br/>
**Rows: 3279**<br/>
**Columns: abstract, action, agencies, body_html_url, cfr_references, citation, comment_url, comments_close_on, correction_of, corrections, dates, disposition_notes, docket_ids, document_number, effective_on, end_page, executive_order_notes, executive_order_number, full_text_xml_url, html_url, images, json_url, mods_url, page_length, page_views, pdf_url, presidential_document_number, proclamation_number, public_inspection_pdf_url, publication_date, raw_text_url, regulation_id_number_info, regulation_id_numbers, regulations_dot_gov_info, regulations_dot_gov_url, significant, signing_date, start_page, subtype, title, toc_doc, toc_subject, topics, type, volume, key**<br/>

### metadata.pckl.gz
Pandas DataFrame holding the data from metadata.csv, pickled with gzip compression. Index has been set to key.<br/>
**Rows: 3279**<br/>
**Columns: abstract, action, agencies, body_html_url, cfr_references, citation, comment_url, comments_close_on, correction_of, corrections, dates, disposition_notes, docket_ids, document_number, effective_on, end_page, executive_order_notes, executive_order_number, full_text_xml_url, html_url, images, json_url, mods_url, page_length, page_views, pdf_url, presidential_document_number, proclamation_number, public_inspection_pdf_url, publication_date, raw_text_url, regulation_id_number_info, regulation_id_numbers, regulations_dot_gov_info, regulations_dot_gov_url, significant, signing_date, start_page, subtype, title, toc_doc, toc_subject, topics, type, volume**<br/>

### downloaded_entries/fulltext/
Holds 3282 individual JSON files with the full-text of each entry in inv_urls.csv and repatriation_urls.csv from the URLs stored in fulltext_url. Includes index field with primary key. Downloaded via main and downloading_fulltext, 3/20/20 - 3/21/20.<br/>

### downloaded_entries/metadata/
Holds 3282 individual JSON files with the metadata of each entry in inv_urls.csv and repatriation_urls.csv from the URLs stored in json_url. Includes index field with primary key. Downloaded via main and downloading_metadata, 04/02/20.<br/>

### inv_urls
Each row represents one Notice of Inventory Completion published in the Federal Register and logged in the National Park Service website. Built in Building Notices of Inventory Completion URL Dataset with data accessed from https://www.nps.gov/subjects/nagpra/notices-of-inventory-completion.htm 2/13/20. (Source URL: https://www.nps.gov/common/uploads/sortable_dataset/nagpra/F8663396-E1B9-7C54-8C15C08D2D0702C4/F8663396-E1B9-7C54-8C15C08D2D0702C4.json.) Unique keys created via indexing by appending "I_" to the dataframes index. Three records have been removed because they were not relevant to NAGPRA (see Cleaning inv_url Title).<br/>
**Rows: 2464**
- **Publication Date**: Original column from NPS. Format: m/d/yyyy, Type: str<br/>
- **Title**: Original column from NPS. Standard format: [Institution], [City], [State, 2-letter abbreviation]. Format for older records: "Notice of Inventory Completion for Native American Human Remains and Associated Funerary Objects from [Geographic region of provenance] in the Possession of [Institution in Possession], [City], [State, 2-letter abbreviation], and in the Control of [Controlling Institution]," Type: str<br/>
- **Link**: Original column from NPS. Link to Federal Register document. Type: str<br/>
- **json_url**: Link to metadata in JSON format. Added via Building Notices of Inventory Completion URL Dataset. Type: str<br/>
- **fulltext_url**: Link to full-text data stored in XML or basic text format. Added via Building Notices of Inventory Completion URL Dataset. Type: str<br/>
- **key**: Primary key. Begins with "I_" to distiguish from Notices of Intent to Repatriate. Added via indexing. Number following "I_" no longer matches iloc, because records have been removed. Type: str<br/>
- **Institution**: Partially processed institutional information from Title. Added via Cleaning inv_url Title. See notebook for outstanding issues. Type: str<br/>
- **City**: Partially processed information on location of Institution, as derived from Title. Added via Cleaning inv_url Title. See notebook for outstanding issues. Type: str<br/>
- **State**: U.S. state where Institution is located, as derived from Title.  Format: 2-letter abbreviation. Added via Cleaning inv_url Title. Type: str<br/>
- **Correction**: Correction status, as derived from Title. Value of 0 indicates that notice is not a correction. Value of 1 indicates a first correction. Value of 2 indicates a second correction. Has not been checked against Federal Register documents or MODS. Added via Cleaning inv_url Title. Type: str<br/>

### repatriation_urls
Each row represents one Notice of Intent to Repatriate published in the Federal Register and logged in the National Park Service website. Built using notices_of_repatriation.csv via Building Notices of Repatriation Dataset on 03/01/2020. Unique keys created via indexing by appending "R_" to the dataframes index.<br/>
**Rows: 815**
- **Publication Date**: Original column from NPS. Format: m/d/yyyy, Type: str<br/>
- **Title**: Original column from NPS. Approximate format: [Institution], [City], [State, 2-letter abbreviation], Type: str<br/>
- **Link**: Original column from NPS. Link to Federal Register document. Type: str<br/>
- **json_url**: Link to metadata in JSON format. Added via Building Notices of Inventory Completion URL Dataset. Type: str<br/>
- **fulltext_url**: Link to full-text data stored in XML or basic text format. Added via Building Notices of Inventory Completion URL Dataset. Type: str<br/> 
- **key**: Primary key. Begins with "R_" to distiguish from Notices of Inventory completion. Added via indexing. Type: str<br/>

### notices_of_repatriation.csv
Downloaded from https://www.nps.gov/subjects/nagpra/notices-of-intent-to-repatriate.htm 03/01/2020.<br/>
**Rows: 815**<br/>
**Columns: Publication Date, Title, Link**<br/>

### inventories_nps.csv
Records of inventories for which notices have not been published in the Federal Register. Downloaded directly from https://www.nps.gov/subjects/nagpra/inventories-database.htm 2/13/20.<br/>
**Rows: 14825**<br/>
**Columns: State, Museum or Federal Agency, MNI, AFO, CA, CUI, Geographic Area, County**<br/>

### fedreg_notices_of_inventory.csv
Notices of Inventory Completion, as downloaded directly from the Federal Register. Truncated; does not contain all records. Details in Building Notices of Inventory Completion URL Dataset. Downloaded from https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=national-park-service&conditions%5Bterm%5D=%22Inventory+Completion%22&conditions%5Btype%5D%5B%5D=NOTICE on 2/13/20.<br/>
**Rows: 1000**<br/>
**Columns: title, type, agency_names, abstract, document_number, html_url, pdf_url, publication_date**<br/><br/>
