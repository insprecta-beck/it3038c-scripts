##unfinished updating this script to import pdfs too
# importing dependencies for word doc
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT


# importing dependencies for excel sheet
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("scraped_links")

#specifying style
style = xlwt.easyxf('font: bold 1')


print("\n This program changes the hyperlinks detected in a word .docx file \n")
print("Document must be in Downloads folder.\n")

docx_file = input(" Please input docx filename (without .docx): ")

document = Document("/Users/lukeb/Downloads/" + docx_file + ".docx")

out_file = input(" Please enter the name of excel file (without .xls): ")

rels = document.part.rels
links = []

for rel in rels:
    if rels[rel].reltype == RT.HYPERLINK and "http" in rels[rel]._target:
       # print ("\n Original link id -", rel, "with detected URL: ", chrels[rel]._target)
        links.append(rels[rel]._target)

for idx, val in enumerate(links):
    print (idx, val)

    sheet.write(idx, 0, val)
    workbook.save(out_file+".xls")


print("\n There are ", len(links), "hyperlinks in this document.")


print("\n File saved to:", out_file + ".xls")
