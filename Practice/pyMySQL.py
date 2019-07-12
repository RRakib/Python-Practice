import pymysql

connection = pymysql.connect('localhost', 'Rakib', 'password', 'TESTDB')
cursor = connection.cursor()

first_name = input('Enter Your First Name: ')
last_name = input('Enter Your Last Name: ')
gender = input('Enter Your Gender: ')
phone_number = int(input('Enter Your Phone Number: '))

drop_existing_table = """DROP TABLE IF EXISTS EMPLOYEE"""
create_table = """CREATE TABLE EMPLOYEE(
                  first_name CHAR(20) NOT NULL,
                  last_name CHAR(20) NOT NULL,
                  gender CHAR(8) NOT NULL,
                  phone_number INT)"""
insert_data = """INSERT INTO EMPLOYEE (first_name, last_name, gender, phone_number)
                 VALUES ('{}','{}','{}','{}')""".format(first_name, last_name, gender, phone_number)
display_data = """SELECT * FROM EMPLOYEE"""

try:
    cursor.execute(drop_existing_table)
    cursor.execute(create_table)
    cursor.execute(insert_data)
    cursor.execute(display_data)
    print(cursor.fetchall())
    print('Table Created')
except Exception as E:
    print('Error Occured', E)
    connection.rollback()

connection.close()