import sqlite3

conn = sqlite3.connect('problem2.db')

c = conn.cursor()

# Create table
c.execute("DROP TABLE IF EXISTS Customers")
c.execute('''CREATE TABLE Customers
             (CustomerId real, Name text)''')

customers = [(1, "Paul Novak"),
             (2, "Terry Neils"),
             (3, "Jack Fonda"),
             (4, "Tom Willis")
            ]
c.executemany('INSERT INTO Customers VALUES (?,?)', customers)

c.execute("DROP TABLE IF EXISTS Reservations")
c.execute('''CREATE TABLE Reservations
             (Id real, CustomerId real, Day text)''')

reservations = [(1, 1, "2009−22−11"),
             (2, 2, "2009−28−11"),
             (3, 2, "2009−29−11"),
             (4, 1, "2009−29−11"),
             (5, 3, "2009−02−12")
            ]
c.executemany('INSERT INTO Reservations VALUES (?,?,?)', reservations)

# Question 2
print("Answer to Question 2:")
c.execute('''SELECT Name, Day FROM Customers AS C 
	JOIN Reservations AS R ON C.CustomerId = R.CustomerId''')
rt1 = c.fetchall()
for rt in rt1:
	print(rt)
print("")

# Question 3
print("Answer to Question 3:")
c.execute('''SELECT Name, Day FROM Customers LEFT JOIN Reservations
	ON Customers.CustomerId = Reservations.CustomerId''')
rt2 = c.fetchall()
for rt in rt2:
	print(rt)
print("")

conn.close()
