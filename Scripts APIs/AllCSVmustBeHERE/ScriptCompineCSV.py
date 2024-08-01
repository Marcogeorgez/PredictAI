# Importing the necessary libraries
from pathlib import Path
from timeit import default_timer as datetime

# Defining the directory path where the CSV files are located
mydir = Path(
    r"C:\Users\mrbro\Desktop\Graduation Project\#PredictAi Project\Scripts APIs\AllCSVmustBeHERE")

# Defining the company name variable to be used later
company_name = 'if we can add each company name here , then we can make it auto generator'

# Starting the timer
start = datetime()

# Looping through all CSV files in the directory
for file in mydir.glob('*.csv'):
    # Opening the CSV file and reading its contents
    with open(f'{file}', 'r') as original:
        # Cleaning up the data and formatting it as a list of strings
        dataa = [''.join([x.strip(), '\n']) for x in original.readlines()]
    # Looping through all TXT files in the directory
    for file1 in mydir.glob('*.txt'):
        # Opening the TXT file in append mode and writing the cleaned up CSV data
        with open(f'{file1}', 'a') as modified:
            modified.writelines(dataa)

# Ending the timer
end = datetime()

# Printing the time taken to complete the operation
print(f'{end-start} seecond')


# This code reads all CSV files in the specified directory,
# cleans up the data, and appends it to all TXT files in the same directory.
# The dataa variable stores the cleaned-up data as a list of strings.
# The cleaned-up data is written to each TXT file in append mode using the writelines() method.
