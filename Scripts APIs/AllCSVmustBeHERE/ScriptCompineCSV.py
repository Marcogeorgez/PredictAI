from pathlib import Path
from timeit import default_timer as datetime

# Compine multiple CSV files to create one large txt file, we use this to combine all companies data to be easier to
# insert it into the SQL database.

mydir = Path(r"C:\Users\mrbro\Desktop\Graduation Project\#PredictAi Project\Scripts APIs\AllCSVmustBeHERE")
company_name = 'if we can add each company name here , then we can make it auto generator'
start = datetime()
for file in mydir.glob('*.csv'):
    with open(f'{file}', 'r') as original:
        dataa = [''.join([x.strip(), '\n']) for x in original.readlines()]
    for file1 in mydir.glob('*.txt'):
        with open(f'{file1}', 'a') as modified:
            modified.writelines(dataa)
end = datetime()

print(f'{end-start} seecond')
