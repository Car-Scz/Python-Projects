'''
Python version:    3.8.2
Author:                   Carol Schultz
Purpose:                The Tech Academy - Python Course
            This script will create a database and then create a table with two fields.  Then an array
            will be processed and  those elements that end with '.txt' will be written to the table.  Once
            that is complete, a SELECT query will be run to print the resulting list.
'''

#   Import the sqlite3 module
import sqlite3

#   Create the database
connection = sqlite3.connect('SQLite_Python.db')
 
#   ----  Drop the table and then create or recreate the table ----
def createTable():
    try:

#   Obtain a cursor object
        cursor = connection.cursor()

#   drop table if is exists
        dropTable = "DROP TABLE IF EXISTS tbl_objList"
        cursor.execute(dropTable)

#   now (re)create the table
        crtTable = "CREATE TABLE IF NOT EXISTS tbl_objList(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, objName TEXT NOT NULL)"
        cursor.execute(crtTable)
        connection.commit()

    except sqlite3.Error as error:
        print("Error:  ", error)
    finally:
        if (connection):
            connection.close()
            print("The createTable function is complete")

#   Insert the date from the array into the table
def insertData():
    try:
        
#   Connect to SQLite db
        connection = sqlite3.connect('SQLite_Python.db')

        with connection:
            cursor = connection.cursor()
            
#   setup loop variables
            array = ('Information.docx', 'Hello.txt', 'myImage.png', \
                    'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
            insertStmt = """INSERT INTO tbl_objList(id, objName) VALUES(?, ?);"""

  # loop through array
            index = 0
            for names in array:
                if names.endswith('.txt'):
                    index += 1
                    data_row = (index, names)
                    cursor.execute(insertStmt, data_row)

 #  commit changes to db            
            connection.commit()
        
    except sqlite3.Error as error:
        print("Error:  ", error)
    finally:
        if (connection):
            connection.close()
            print("The insert function is complete")

#   Now run the query and display the results
def runQuery():
    try:
        
#   Connect to SQLite db
        connection = sqlite3.connect('SQLite_Python.db')
 
        with connection:
            cursor = connection.cursor()
            
#   Select from the file list table
            queryTable = "SELECT objName from tbl_objList"
            queryResults = cursor.execute(queryTable)

#   Print the list of object names
            print("\n\nObject Name")
            print("-------------------")
            for result in queryResults:
                print(*result)
        
    except sqlite3.Error as error:
        print("Error:  ", error)
    finally:
        if (connection):
            connection.close()
 
if __name__ == "__main__":
    createTable()
    insertData()
    runQuery()
