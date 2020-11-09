# Python request_test.py 
import requests
import urllib
import sys
import os
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
from bs4 import BeautifulSoup

# Get the url of the directory hosting the page
parent_url = "/".join(sys.argv[1].split("/")[:-1])
print(parent_url + "\n")

# Find the links to each unique .pdf document on the page
response = requests.get(sys.argv[1])

soup = BeautifulSoup(response.text, features="html.parser")

pdf_links = soup.find_all('a', href=re.compile(r'(.pdf)'))

pdf_urls = []

temp_pdfs = '.\\temp_pdfs\\'

try:
    os.mkdir(temp_pdfs)
except:
    print("There was an error creating a temporary working file.")

for pdf in pdf_links:
    if pdf['href'] not in os.listdir(temp_pdfs):
        pdf_name = pdf['href'].split("/")[-1]
        r = requests.get(parent_url + "/" + pdf['href'], allow_redirects=True)
        with open(temp_pdfs + pdf_name, 'wb') as this_pdf:
            this_pdf.write(r.content)
        
        



# read each pdf and then write it into the master file

with open(sys.argv[2] + ".pdf", 'wb') as combined_pdf:
    pdf_writer = PdfFileWriter()
    for each in os.listdir(temp_pdfs):
        pdf_reader = PdfFileReader(each)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    
    pdf_writer.write(combined_pdf)

os.walk(temp_pdfs, topdown=False)
    