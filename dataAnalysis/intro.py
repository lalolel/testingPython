# import a Python package that helps us connect to the new database
import sqlite3
import pandas as pd

# connect to the billing database
con = sqlite3.connect('billing.db')
cur = con.cursor()

# show us the three tables that exist there
table_list = [a[0] for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]

for table in table_list:
  print('Existing table named ' + table + '\n')

# build a query to create the new billing view

# first, we'll include some code that tells the database we're creating a new view of the data
query = 'CREATE VIEW billing AS'

# next, we'll tell the database which columns we want in our final table
query += ' SELECT BillingEvent.ID AS ID, username, Date, Event FROM BillingEvent'

# lastly, we'll explain how to connect the three tables
query += ' INNER JOIN Customer on BillingEvent.CustomerID = Customer.ID'
query += ' INNER JOIN BillingEventTypes on BillingEvent.EventType = BillingEventTypes.ID'

# now that the query in SQL is built, we'll use Python to send it to the database. We've added some code to catch an error if you run the exercise more than once!

print("Creating new billing view combining the three: ")
try:
  cur.execute(query)
except sqlite3.OperationalError:
  print("You've already run this exercise! Here's the table: ")
  
# finally, let's take a look at our table!
# we'll do this the way a data scientist might - using the package pandas!
billing = pd.read_sql('SELECT * FROM billing',con)
print(billing)

# close our connection to the database
con.close()
