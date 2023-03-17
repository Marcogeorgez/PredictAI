from pathlib import Path
#  This folder has only 1 job
#     Fetching the latest stock prices for all companies we have.
#     Then Adding the symbol of the company to the first column of every line in the entire stock files
#     Therefore be able to Insert them into the table to update the latest prices of stock.
mydir = Path(r"C:\Users\kzaki\Desktop\PredictAi\Script\AllCSVmustBeHERE")
company_name = 'if we can add each company name here , then we can make it auto generator'
for file in mydir.glob('*.csv'):
    print(file.name)
    removecsv = file.name[:-4]
    print(removecsv)
    with open(f'{file}', 'r') as original:
        dataa = [''.join([f"{removecsv}",",", x.strip(),'\n']) for x in original.readlines()]
    with open(f'{file}', 'w') as modified:
        modified.writelines(dataa)
    # do your stuff
