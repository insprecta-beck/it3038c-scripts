#This script ingests .docx files, scrapes hyperlinks & appends them to.xls files
#View the README.md page in ClassProjects for more on how to use this script.

# importing dependencies for word doc
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

#importing requests module for status codes
import requests
from requests import head

# importing dependencies for excel sheet
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("scraped_links")

#specifying style
style = xlwt.easyxf('font: bold 1')

print("\n This program scrapes hyperlinks in a word .docx file, and puts them into a spreadsheet.\n")
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
