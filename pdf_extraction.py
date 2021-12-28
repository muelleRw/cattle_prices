import camelot
import shutil
import os

files = [f for f in os.listdir('ST Onge PDF') if f.endswith('pdf')]
for file in files:
    month = file[1:3]
    day = file[3:5]
    year = '20' + file[5:7]
    tables = None
    try:
        tables = camelot.read_pdf(
            f'ST Onge PDF/{file}', 
            process_background=True, 
            line_scale=60, 
            split_text=True,
            line_tol=3,
            #joint_tol=5,
            shift_text=['l']
        )
        if tables[0].shape[1] == 7:
            shutil.move(f"ST Onge PDF/{file}", f"st_onge_7_column/{year}-{month}-{day}.pdf")
    except Exception as e:
        print(e)
        if tables is not None and tables.n > 0:
            print(f"Exception {file}: {tables[0].shape[0]}")
        else:
            print(f"Exception Reading {file}")
        continue

files = [f for f in os.listdir('ST Onge PDF') if f.endswith('pdf')]
for file in files:
    month = file[1:3]
    day = file[3:5]
    year = '20' + file[5:7]
    tables = None
    try:
        tables = camelot.read_pdf(
            f'ST Onge PDF/{file}', 
            process_background=False, 
            line_scale=60, 
            split_text=True,
            line_tol=3,
            #joint_tol=5,
            shift_text=['l']
        )
        if tables[0].shape[1] == 7:
            shutil.move(f"ST Onge PDF/{file}", f"st_onge_7_column_false/{year}-{month}-{day}.pdf")
    except Exception as e:
        print(e)
        if tables is not None and tables.n > 0:
            print(f"Exception {file}: {tables[0].shape[0]}")
        else:
            print(f"Exception Reading {file}")
        continue


files = [f for f in os.listdir('ST Onge PDF') if f.endswith('pdf')]
for file in files:
    month = file[1:3]
    day = file[3:5]
    year = '20' + file[5:7]
    tables = None
    try:
        tables = camelot.read_pdf(
            f'ST Onge PDF/{file}', 
            #process_background=True, 
            line_scale=60, 
            split_text=True,
            line_tol=3,
            #joint_tol=5,
            shift_text=['l']
        )
        if tables[0].shape[1] == 6:
            shutil.move(f"ST Onge PDF/{file}", f"st_onge_6_column/{year}-{month}-{day}.pdf")
    except Exception as e:
        print(e)
        if tables is not None and tables.n > 0:
            print(f"Exception {file}: {tables[0].shape[0]}")
        else:
            print(f"Exception Reading {file}")
        continue

files = [f for f in os.listdir('ST Onge PDF') if f.endswith('pdf')]
for file in files:
    month = file[1:3]
    day = file[3:5]
    year = '20' + file[5:7]
    tables = None
    try:
        tables = camelot.read_pdf(
            f'ST Onge PDF/{file}', 
            #process_background=True, 
            line_scale=60, 
            split_text=True,
            line_tol=3,
            #joint_tol=5,
            shift_text=['l']
        )
        if tables[0].shape[1] == 5:
            shutil.move(f"ST Onge PDF/{file}", f"st_onge_5_column/{year}-{month}-{day}.pdf")
    except Exception as e:
        print(e)
        if tables is not None and tables.n > 0:
            print(f"Exception {file}: {tables[0].shape[0]}")
        else:
            print(f"Exception Reading {file}")
        continue


camelot.plot(tables[0], kind='grid').show()
df=tables[0].df
df.to_csv('foo.csv')
tables[0].to_csv('foo.csv')

tables
tables.export('foo.csv', f='csv', compress=True)
tables[0]
tables[0].parsing_report
tables[0].to_csv('foo.csv')

df = tables[0].df.replace(r'\n', '', regex=True)
df.to_csv('foo.csv')



