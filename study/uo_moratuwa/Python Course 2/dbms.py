import pymysql

# open database connection
db_connection = pymysql.connect(
    host='localhost', user='root', passwd='Moon@Noon365', db='python_course_db')

# creating a cursor object
cursor = db_connection.cursor()

# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
# sql = """CREATE TABLE EMPLOYEE (
#    FIRST_NAME  CHAR(20) NOT NULL,
#    LAST_NAME  CHAR(20),
#    AGE INT,
#    SEX CHAR(1),
#    INCOME FLOAT )"""

# show table structure
# sql = """
#     show columns from EMPLOYEE
# """

# execute query
# cursor.execute("select version()")
# Prepare SQL query to INSERT a record into the database.

# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#    LAST_NAME, AGE, SEX, INCOME)
#    VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db_connection.commit()
# except:
#     # Rollback in case there is any error
#     db_connection.rollback()

# Prepare SQL query to INSERT a record into the database.
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#    LAST_NAME, AGE, SEX, INCOME) \
#    VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#     ('Mac', 'Mohan', 20, 'M', 2000)
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db_connection.commit()
# except:
#     # Rollback in case there is any error
#     db_connection.rollback()

# Prepare SQL query to view record from the database.

# sql = "SELECT * FROM EMPLOYEE \
#       WHERE INCOME > '%d'" % (1000)
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Fetch all the rows in a list of lists.
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # Now print fetched result
#         print("fname = %s,lname = %s,age = %d,sex = %s,income = %d" %
#               (fname, lname, age, sex, income))
# except:
#     print("Error: unable to fetch data")

# Prepare SQL query to UPDATE required records
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db_connection.commit()
# except:
#     # Rollback in case there is any error
#     db_connection.rollback()


# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db_connection.commit()
except:
    # Rollback in case there is any error
    db_connection.rollback()

# cursor.execute(sql)

# data = cursor.fetchall()
# print(data)

# disconnect from mysql server
db_connection.close()

# print the version executed above
# data = cursor.fetchall()
# print("Database version:", data[0][0])
