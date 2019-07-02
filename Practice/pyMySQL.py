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
insert_data = """INSERT INTO EMPLOYEE(FIRST_NAME , LAST_NAME, AGE, SEX, INCOME) 
                 VALUES('RAKIB','UDDIN','23','M','20000')"""
fetch_all_data = """SELECT * FROM EMPLOYEE"""

try:
    cursor.execute(delete_exixting_table)
    print('Existing table has been deleted')
    cursor.execute(create_new_table)
    print('New table has been created')
    cursor.execute(insert_data)
    print('Insertion of data completed')
    cursor.execute(fetch_all_data)
    data_storage = cursor.fetchall()
    print('First Name:' ,data_storage[0][0])
    print('Last Name:' , data_storage[0][1])
except Exception as e:
    print('Exception is:' , e)

db.close()