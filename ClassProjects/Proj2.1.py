##This script ingests .docx files, scrapes hyperlinks, 
# and appends them to .xls files

#importing requests module for status codes
import requests
from requests import head

# importing dependencies for word doc
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

# importing dependencies for PDFs
import PyPDF2
import re

print("\nThis program scrapes hyperlinks from either a word .DOCX file, or a .PDF file.\n")
FileType = input("Are we working with a '.pdf' or a '.docx' file? ")
if(FileType == '.pdf'):
    print("\nYou'll need to type out the entire filepath where your .pdf file is located. i.e - /Users/Username/Downloads/Filename.pdf\n")
    pdf_file = input(" Please type the full filepath of the .docx file you are looking to scrape.\n")
    else if(FileType == '.docx'):
    print("\nYou'll need to type out the entire filepath where your .docx file is located. i.e - /Users/Username/Downloads/Filename.docx\n")
    docx_file = input(" Please type the full filepath of the .docx file you are looking to scrape.\n")
    else:
    print("Cannot ingest that file. Please pick either a '.docx' or '.pdf' file.")

# Open The File in the Command
file = open
readPDF = PyPDF2.PdfFileReader(file)
def find_url(string):
   #Find all the String that matches with the pattern
   regex = r"(https?://)"
   url = re.findall(regex,string)
   for url in url:
      return url
# Iterating over all the pages of File
for page_no in range(readPDF.numPages):
   page=readPDF.getPage(page_no)
   #Extract the text from the page
   text = page.extractText()
   # Print all URL
   print(find_url(text))
   
# Close the file
file.close()

# importing dependencies for excel sheet
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("scraped_links")

#specifying style
style = xlwt.easyxf('font: bold 1')

print("\nThis program scrapes hyperlinks in a word .docx file, and puts them into a spreadsheet.\n")
print("\nYou'll need to type out the entire filepath where your .docx file is located. i.e - /Users/Username/Downloads/Filename.docx\n")
docx_file = input(" Please type the full filepath of the .docx file you are looking to scrape.\n")

document = Document(docx_file)

out_file = input(" Please enter the name of excel file (without .xls): ")

rels = document.part.rels
links = []

for rel in rels:
    if rels[rel].reltype == RT.HYPERLINK and "http" in rels[rel]._target:
       # print ("\n Original link id -", rel, "with detected URL: ", chrels[rel]._target)
        links.append(rels[rel]._target)
        try:
            r = requests.head(rels[rel]._target)
            print(r.status_code)
        # prints the int of the status code. Find more at httpstatusrappers.com :)
        except requests.ConnectionError:
            print("failed to connect")

for idx, val in enumerate(links):
    print (idx, val, r.status_code)

    sheet.write(idx, 0, val)
    workbook.save(out_file+".xls")

print("\n There are ", len(links), "hyperlinks in this document.")

print("\n File saved to:", out_file + ".xls")

exit()