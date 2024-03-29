# importing dependencies for PDFs
import PyPDF2
import re
# Open The File in the Command
file = open("/Users/lukeb/Downloads/McNayBibliography.pdf", 'rb')
readPDF = PyPDF2.PdfFileReader(file)
def find_url(string):
   #Find all the String that matches with the pattern
   regex = r"(https?://\S+)"
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
# CLost the file
file.close()