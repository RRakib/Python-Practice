import pymysql
db = pymysql.connect("localhost","Rakib","password","TESTDB" )
cursor = db.cursor()

delete_exixting_table = "drop table if exists EMPLOYEE "

create_new_table = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

try:
    cursor.execute(delete_exixting_table)
    print('Existing table has been deleted')
    cursor.execute(create_new_table)
    print('New table has been created')
except Exception as e:
    print('Exception is:' , e)

db.close()