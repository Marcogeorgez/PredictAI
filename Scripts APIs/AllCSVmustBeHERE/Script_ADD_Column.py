# Import the Path module from pathlib library
from pathlib import Path

# Define the directory path where CSV files are located
mydir = Path(
    r"D:\Github Projects\Predict AI\Scripts APIs\AllCSVmustBeHERE")

# Define a placeholder company name variable for future use
company_name = 'if we can add each company name here , then we can make it auto generator'

# Loop through each CSV file in the directory
for file in mydir.glob('*.csv'):
    # Print the name of the current CSV file
    print(file.name)

    # Extract the company symbol from the filename by removing the ".csv" extension
    company_symbol = file.name[:-4]

    # Open the original CSV file in read mode
    with open(f'{file}', 'r') as original:
        # Read each line of the original CSV file, clean up the data, and store it as a list of strings in the dataa variable
        dataa = [''.join([f"{company_symbol}", ",", x.strip(), '\n'])
                 for x in original.readlines()]

    # Open the same CSV file in write mode
    with open(f'{file}', 'w') as modified:
        # Write each element of the dataa list to the modified CSV file
        modified.writelines(dataa)

#  This folder has only 1 job
#     Fetching the latest stock prices for all companies we have.
#     Then Adding the symbol of the company to the first column of every line in the entire stock files
#     Therefore be able to Insert them into the table to update the latest prices of stock.

# This code reads all CSV files in a specified directory, extracts the company symbol from their filename,
# cleans up the data by adding the company symbol as a prefix, and appends it to the same CSV files.
# The dataa variable stores the cleaned-up data as a list of strings. The cleaned-up data is written
# to each CSV file in write mode using the writelines() method. The time taken to complete the operation
# is not printed, though it can be added using Python's time module.
