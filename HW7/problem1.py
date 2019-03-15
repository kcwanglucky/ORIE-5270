import requests
import sqlite3
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# get the web data with requests
page = requests.get(url)
page_text = page.text

lines = page_text.split("\n")
columns = ["ID", "SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Class"]

data = []		# to store the relevant data in the form of list
idx = 1

for line in lines:
	delimitedLine = line.split(",")
	if len(delimitedLine) > 1:
		tempData = [idx] + delimitedLine
		#print(tempData)
		idx += 1
		data.append(tempData)

# Convert list into pandas dataframe
df = pd.DataFrame(data, columns = columns)

# Create a connection object that represents the database.
conn = sqlite3.connect('problem1.db')

# use the to_sql function to transform and put the dataframe into database
df.to_sql("Iris", conn, if_exists="replace", index = False)

#conn = sqlite3.connect('problem1.db')		# To Delete
c = conn.cursor()

# Question 3
print("")
print("Answer to Question 3:")
c.execute("SELECT Max(SepalWidth), Min(SepalWidth), Avg(SepalWidth) FROM Iris")

statSW = c.fetchall()
cols3 = ["Max SepalWidth", "Min SepalWidth", "Avg SepalWidth"]
df3 = pd.DataFrame(statSW, columns = cols3, index = ["Result         "])# extra whitespace for alignment purpose
print(df3)
print("")

# Question 4
print("Answer to Question 4:")

# Add the "GROUP BY" to provide results based on groups
c.execute("SELECT Class, Max(SepalWidth), Min(SepalWidth), Avg(SepalWidth) FROM Iris GROUP BY Class")
statSWGroup = c.fetchall()
cols4 = ["Class", "Max SepalWidth", "Min SepalWidth", "Avg SepalWidth"]

df4 = pd.DataFrame(statSWGroup, columns = cols4)
# Use "Class" column as index
df4 = df4.set_index('Class')
print(df4)
print("")
conn.close()
