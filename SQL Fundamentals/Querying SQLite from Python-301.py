## 3. Connecting to the Database ##

import sqlite3
conn = sqlite3.connect("jobs.db")

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
query = "SELECT Major FROM recent_grads;"
majors = cursor.execute(query).fetchall()
print(majors[0:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
query = "SELECT Major, Major_category FROM recent_grads"
five_results = cursor.execute(query).fetchmany(5)
print(five_results)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3
conn = sqlite3.connect("jobs2.db")
query = "SELECT Major FROM recent_grads ORDER BY Major DESC"
reverse_alphabetical = conn.execute(query).fetchall()
print(reverse_alphabetical)
conn.close()