import pymysql
db = pymysql.connect("localhost","Rakib","k9AfcdFi","TESTDB" )
cursor = db.cursor()

delete_exixting_table = "drop table if exists EMPLOYEE "

create_new_table = """create table EMPLOYEE (
    _id int auto_increment primary key,
    name varchar(20) not null
)"""

try:
    cursor.execute(delete_exixting_table)
    print('Existing table has been deleted')
    cursor.execute(create_new_table)
    print('New table has been created')
except Exception as e:
    print('Exception is:' , e)

db.close()