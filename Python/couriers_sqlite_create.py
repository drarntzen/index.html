"""Python script to create SQLite database for input/output.

    Rationale: SQLite is a light-weight alternative with a tiny footprint
    and works out-of-the-box, no install needed. Perfect for when your work
    uses a VPN to a central server and you can't install shit that would make
    your life easier :)

    Hopefully I will be able to EXEify the end product... otherwise, there
    are other ways to make it make my working life easier.

    And worst case, I learnt some Python along the way!
"""

import sqlite3
import csv


def createTable(tableName, conn):
    """Code to connect to a database object and make the table."""
    c = conn.cursor()
    c.execute('CREATE TABLE goods_outwards(ID INT PRIMARY KEY NOT NULL,\
              Date CHAR(10), Reference CHAR(15), Transport CHAR(20),\
              Consignment CHAR(20), Quantity INT)')
    conn.commit()


def insertRows(fileName, conn):
    """Code to insert rows from a CSV to the SQLite database table."""
    c = conn.cursor()
    lineNum = 0
    with open(fileName, 'rt') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        for row in lineReader:
            lineNum += 1
            if lineNum == 1.0:
                print("Skipping header row...")
                continue
            oneTuple = [row[0], row[1], row[2], row[3], row[4], row[5]]
            c.execute("INSERT INTO goods_outwards VALUES (?,?,?,?,?,?)",
                      oneTuple)
        conn.commit()
        print("Iteration complete.")

if __name__ == "__main__":
    conn = sqlite3.connect('couriers.sqlite')
    # Uncomment line if table not yet created
    # createTable('couriers.sqlite', conn)
    fileName = input("Enter CSV file to import: ")
    insertRows(fileName, conn)
    print("File import completed.")
