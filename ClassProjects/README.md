# Read this for info about each project script and any updates there-in.
### Project 2 is an update of Project 1. Here is the run down:
This script will be used to ingest Word documents. It will scrape the ingested Word document for hyperlinks inside, and paste them into an .xls sheet.
### In order to run this python script you will need the following python dependencies: requests, docx and xlwt.

Updates of Proj1 in Proj2.py: 
Script is more user friendly. I added the requests module to list status codes of the scraped links within the user input word file. Status codes are now appended to the links in the terminal before creating the out_file.

Future updates: Planning to append status codes to links in the out_file itself. Will post more updates after learning more API calls.
