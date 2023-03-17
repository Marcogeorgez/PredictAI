from pathlib import Path
#  This folder has only 1 job
#   Merging all files in CSV to 1 file of Text
mydir = Path(r"C:\Users\kzaki\Desktop\PredictAi\Script\AllCSVmustBeHERE")
company_name = 'if we can add each company name here , then we can make it auto generator'
for file in mydir.glob('*.csv'):
    removecsv = file.name[:-4]
    print(removecsv)
    with open(f'{file}', 'r') as original:
        dataa = [''.join([x.strip(),'\n']) for x in original.readlines()]
    for file1 in mydir.glob('*.txt'):
        with open(f'{file1}', 'a') as modified:
            modified.writelines(dataa)
