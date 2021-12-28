import camelot
import os

df_list = []

files = [f for f in os.listdir('st_onge_7_column') if f.endswith('pdf')]
for file in files:
    try:
        tables = camelot.read_pdf(
            f'st_onge_7_column/{file}', 
            process_background=True, 
            line_scale=60, 
            split_text=True,
            line_tol=3,
            #joint_tol=5,
            shift_text=['l'],
            pages='all'
        )
        if tables[0].shape[1] == 7:
            df_list.append([j.df for j in tables])
        else: 
            raise Exception("Bad Shape Column Length")
    except Exception as e:
        print(e)
        if tables is not None and tables.n > 0:
            print(f"Exception {file}: {tables[0].shape[0]}")
        else:
            print(f"Exception Reading {file}")
        continue



import PyPDF2
pdfFileObj = open(f'st_onge_7_column/{file}', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
NumPages = pdfReader.numPages

i = 0
content = []
while (i<NumPages):
    text = pdfReader.getPage(i)
    content.append(text.extractText().splitlines())
    i +=1

import pandas as pd
df = pd.DataFrame(content)




import textract
text = textract.process(f'st_onge_7_column/{file}', method='tesseract')
print(text)
with open('textract-results.txt', 'w+') as f:
    f.write(str(text))