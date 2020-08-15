import sqlite3

#   get personal data from user
# firstName = input("Enter your first name:  ")
# lastName = input("Enter your last name:  ")
# age = int(input("Enter your age:  "))
# personData = (firstName, lastName, age)

#  execute insert statement for supplied person data
with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    #   c.execute("INSERT INTO People VALUES(?,?,?)", personData)
    #   c.execute("UPDATE People SET age=? WHERE firstName=? AND lastName=?", (45, 'Luigi', 'Vercotti'))
    #  connection.commit()

#   select all first and last names from people over age 30
#       query fetched all results into a list
#    c.execute("SELECT firstName, lastName FROM People WHERE Age > 30")
#   for row in c.fetchall():
 #       print (row)
# loop through returned list to parse the results
    c.execute("SELECT firstName, lastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print (row)
connection.close()
