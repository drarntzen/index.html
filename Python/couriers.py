"""Python script to interact with outgoing goods database.

    To be updated on an on-going basis as I learn more Python.
    Will initially read from a .csv
    First initial major goal is a sqlite database

"""

# import required libraries
import csv

csvContents = []
# First row is a header row!
# Column date for the CSV:
# Column 1 (Index 0) = Date goods sent
# Column 2 (Index 1) = Consignment reference (ex Company)
# Column 3 (Index 2) = Transport company
# Column 4 (Index 3) = Transport company consignment reference
# Column 5 (Index 4) = Quantity sent (Usually 1, but not always!)


def openCSV(csvFile):
    """Function to open CSV file, Mark I."""
    lineNum = 0
    csvFile =  open('couriers.csv', 'rt')
    lineReader = csv.reader(csvFile, delimiter=",")
    for row in lineReader:
        lineNum += 1
        if lineNum == 1.0:
            print("Skipping the header row")
            continue
        dateSent = row[0]
        salesReference = row[1]
        transportCompany = row[2]
        transportConsignment = row[3]
        quantitySent = row[4]
        oneResultRow = [dateSent, salesReference, transportCompany,
                        transportConsignment, quantitySent]
        csvContents.append(oneResultRow)
        print(dateSent, ",", salesReference, ",", transportCompany, ",",
              transportConsignment, ",", quantitySent)
    print("Iteration done.")

if __name__ == "__main__":
    dbFile = input("Enter database name: ")
    openCSV(dbFile)
    print("File Parsing complete.")
