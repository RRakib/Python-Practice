import pymysql


connection = pymysql.connect('localhost', 'Rakib', 'password', 'TESTDB')
cursor = connection.cursor()

def handle_exception(e):
    print('Error Occured!''\n', e)
    connection.rollback()

def show_table():
    show_table = '''SHOW TABLES'''
    try:
        cursor.execute(show_table)
        st = cursor.fetchall()
        print('Table Found: ', st[0][0])
    except Exception as E:
        handle_exception('NO Table Found''\n')

def drop_existing_table():
    drop_existing_table = """DROP TABLE IF EXISTS EMPLOYEE"""
    try:
        cursor.execute(drop_existing_table)
        print('Table Dropped Successfully! ''\n')
    except Exception as E:
        handle_exception(E)

def create_table_employee():
    create_table = """CREATE TABLE EMPLOYEE(
                      first_name CHAR(20) NOT NULL,
                      last_name CHAR(20) NOT NULL,
                      gender CHAR(8) NOT NULL,
                      phone_number INT)"""
    try:
        cursor.execute(create_table)
        print('Table Created Successfully!''\n')
    except Exception as E:
        handle_exception(E)

def insert_data_into_employee():
    first_name = input('Enter Your First Name: ')
    last_name = input('Enter Your Last Name: ')
    gender = input('Enter Your Gender: ')
    phone_number = int(input('Enter Your Phone Number: '))
    insert_data = """INSERT INTO EMPLOYEE (first_name, last_name, gender, phone_number)
                     VALUES ('{}','{}','{}','{}')"""\
                    .format(first_name, last_name, gender, phone_number)
    try:
        cursor.execute(insert_data)
        print('Data Insertion Complete!''\n')
    except Exception as E:
        handle_exception(E)

def display_data():
    display_data = """SELECT * FROM EMPLOYEE"""
    try:
        cursor.execute(display_data)
        user_info = cursor.fetchall()
        print('User Data: ', user_info[0],'\n')
    except Exception as E:
        print('Error Occured!', E)
        connection.rollback()

print('\n''\n''Welcome To Nowhere! Please Choose One of The Option and Type It Down Below''\n')

while connection:
    options = ('1. Check if table already exists - CHECK_TABLE',
               '2. Drop existing table - DROP_TABLE',
               '3. Create new employee table - CREATE_TABLE',
               '4. Insert data into table - INSERT_DATA',
               '5. Display data available inside the table - DISPLAY_DATA',
               '6. Exit out - EXIT')

    for option in options:
        print(option, '\n')

    user_input = input('Your Choice: ')

    try:
        if user_input == 'CHECK_TABLE':
            show_table()
        elif user_input == 'DROP_TABLE':
            drop_existing_table()
        elif user_input == 'CREATE_TABLE':
            create_table_employee()
        elif user_input == 'INSERT_DATA':
            insert_data_into_employee()
        elif user_input == 'DISPLAY_DATA':
            display_data()
        elif user_input == 'EXIT':
            break
        else:
            print('Please type the correct keyword''\n')
    except Exception as E:
        print('Opps Something Went Wrong!', E)


connection.close()