import camelot
import shutil
import os

from camelot.utils import flag_font_size



files = [f for f in os.listdir('st_onge_pdf') if f.endswith('pdf')]
def move_pdf(files, columns):
    for file in files:
        print(file)
        month = file[1:3]
        day = file[3:5]
        year = '20' + file[5:7]
        tables = None
        try:
            tables = camelot.read_pdf(
                f'st_onge_pdf/{file}', 
                flavor='lattice',
                process_background=False, 
                line_scale=15, 
                split_text=False,
                pages='all'
                
                #line_tol=3,
                #joint_tol=5,
                #shift_text=['l']
            )
            if tables[0].shape[1] == columns:
                if not os.path.exists(f"st_onge_{columns}"):
                    os.makedirs(f"st_onge_{columns}")
                shutil.move(f"st_onge_pdf/{file}", f"st_onge_{columns}/{year}-{month}-{day}.pdf")
        except Exception as e:
            print(e)
            if tables is not None and tables.n > 0:
                print(f"Exception {file}: {tables[0].shape[0]}")
            else:
                print(f"Exception Reading {file}")
            

for i in range(5, 10):
    files = [f for f in os.listdir('st_onge_pdf') if f.endswith('pdf')]
    move_pdf(files, i)


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



