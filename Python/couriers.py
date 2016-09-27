"""Python script to interact with outgoing goods database.

    To be updated on an on-going basis as I learn more Python.
    Will initially read from a .csv
    First initial major goal is a sqlite database

    Goal is to make it searchable!

"""

# import required libraries
import csv


def openCSV(csvFile):
    """Function to open CSV file, Mark I."""
    lineNum = 0
    csvContents = []
    csvFile = open('couriers.csv', 'rt')
    lineReader = csv.reader(csvFile, delimiter=",")
    for row in lineReader:
        lineNum += 1
        if lineNum == 1.0:
            # First row is a header row!
            print("Skipping the header row")
            continue
        # Column 1 (Index 0) = Date goods sent
        dateSent = row[0]
        # Column 2 (Index 1) = Consignment reference (ex Company)
        salesReference = row[1]
        # Column 3 (Index 2) = Transport company
        transportCompany = row[2]
        # Column 4 (Index 3) = Transport company consignment reference
        transportConsignment = row[3]
        # Column 5 (Index 4) = Quantity sent (Usually 1, but not always!)
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
