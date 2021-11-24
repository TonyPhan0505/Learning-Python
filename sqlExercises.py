import sqlite3
from sqlite3 import Error

def add_reminders(task, deadline, filepath = host + 'db_files/reminders.db'):
	
	try:
		conn = sqlite3.connect(filepath)
	
	except Error:
		print(Error)
	cursorObj = conn.cursor()

	cursorObj.execute("""
	INSERT INTO Schedule (task_description, date_time) VALUES (?,?)	
	""", (task, deadline))

	conn.commit()
	if conn:
		conn.close()

def refresh_reminder(filepath = host + 'db_files/reminders.db'):
	
	conn = sqlite3.connect(filepath)
	
	
	cursorObj = conn.cursor()
	cursorObj.execute("""DELETE FROM Schedule WHERE date_time = ?""", (time.strftime('%I:%M %p, %Y/%B/%d'),))
	conn.commit()

def schedule_report(filepath = host + 'db_files/reminders.db',):
	try:
		conn = sqlite3.connect(filepath)
	except Error:
		print(Error)
	
	conn.commit()
	cursorObj = conn.cursor()
	cursorObj.execute("SELECT * FROM Schedule")
	records = cursorObj.fetchall()

	day = time.strftime('%Y_%B_%d')
	
	try:
		with open('///Users/'+user_name+'/Desktop/Today_Schedule_'+day+'.txt', 'w') as f:
				f.close()
		for record in records:
			if record[1].split(', ')[1] == time.strftime('%Y/%B/') + str(int(time.strftime("%d"))):
				with open('///Users/'+user_name+'/Desktop/Today_Schedule_'+day+'.txt', 'w') as f:
					item = '{}: {}'.format(record[0], record[1].rsplit(', ')[0])
					f.write(item)
		
		
		return "Sir, your schedule is ready for you in your Desktop"
			
	except:
		return "Sir, the file corrupted. Please state your demand again and repeat the process with me."

def create_connect(db_name):
	try:
		filepath = db_name + '.db'
		sqlite_Connection = sqlite3.connect(filepath)
		conn = sqlite_Connection.cursor()
		sqlite_select_Query = 'select sqlite_version();'
		conn.execute(sqlite_select_Query)
		conn.close()
	except sqlite3.Error as error:
		print('Error while connecting to sqlite', error)
	finally:
		if sqlite_Connection:
			sqlite_Connection.close()

def create_table(filepath):

	def sql_connection(filepath):
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)

	def sql_table(conn):
		cursorObj = conn.cursor()
		cursorObj.execute('CREATE TABLE agent_master(agent_code char(6), agent_name char(40), working_area char(35),commission decimal(10,2),phone_no char(15) NULL);')
		conn.commit()
	
	sqllite_conn = sql_connection(filepath)
	sql_table(sqllite_conn)
	if sqllite_conn:
		sqllite_conn.close()
		print('\nThe SQLite connection is closed')

def get_tables(filepath):

	def sql_connection(filepath):
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)
	
	def sql_table(conn):
		cursorObj = conn.cursor()
		corsorObj.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
		print(cursorObj.fetchall())
		conn.commit()
	
	sqllite_conn = sql_connection(filepath)
	sql_table(sqllite_conn)
	if sqllite_conn:
		sqllite_conn.close()
		print('\nThe SQLite connection is closed')
	
def input_and_print_records(filepath):

	def sql_connection(filepath):
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)
	
	def sql_table(conn):
		cursorObj = conn.cursor()
		cursorObj.executescript("""
		INSERT INTO salesman VALUES(5001,'James Hoog', 'New York', 0.15);
   		INSERT INTO salesman VALUES(5002,'Nail Knite', 'Paris', 0.25);
   		INSERT INTO salesman VALUES(5003,'Pit Alex', 'London', 0.15);
   		INSERT INTO salesman VALUES(5004,'Mc Lyon', 'Paris', 0.35);
   		INSERT INTO salesman VALUES(5005,'Paul Adam', 'Rome', 0.45);
		""")
		conn.commit()
		cursorObj.execute("SELECT * FROM salesman")
		rows = cursorObj.fetchall()
		print("Agent details: ")
		for row in rows:
			print(row)
	
	sqllite_conn = sql_connection()
	sql_table(sqllite_conn)
	if (sqllite_conn):
		sqllite_conn.close()
		print("\nThe SQLite connection is closed.")
	
def createTableAndInputListOfRecords(filepath):

	def sql_connection(filepath):
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)

	def sql_table(conn, rows):
		cursorObj = conn.cursor()
		cursorObj.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
		sqlite_insert_query = """INSERT INTO salesman (salesman_id, name, city, commission)
		VALUES (?,?,?,?);"""
		cursorObj.executemany(sqlite_insert_query, rows)
		conn.commit()
	
	rows = [(5001,'James Hoog', 'New York', 0.15),
         (5002,'Nail Knite', 'Paris', 0.25),
         (5003,'Pit Alex', 'London', 0.15),
         (5004,'Mc Lyon', 'Paris', 0.35),
         (5005,'Paul Adam', 'Rome', 0.45)]

	sqllite_conn = sql_connection()
	sql_table(sqllite_conn, rows)

	if sqllite_conn:
		sqllite_conn.close()
		print("\nThe SQLITE connection is closed.")

def inputRecordsFromUserInputs(filepath):
	conn = sqlite3.connect(filepath)
	cursor = conn.cursor()
	s_id = input('Salesman ID: ')
	s_name = input('Name: ')
	s_city = input("City: ")
	s_commission = input("Commission: ")

	cursor.execute("""
	INSERT INTO salesman(salesman_id, name, city, commission)
	VALUES (?,?,?,?)""", (s_id, s_name, s_city, s_commission))

	conn.commit()
	print("Data entered successfully.")
	conn.close()
	if conn:
		conn.close()
		print("\nThe SQLite connection is closed.")

def number_of_records(filepath):

	def sql_connection(filepath):
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)
	
	def sql_table(conn):
		cursorObj = conn.cursor()
		cursorObj.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
		print("Number of records before inserting rows:")
		cursor = cursorObj.execute('select * from salesman;')
		print(len(cursor.fetchall()))

		cursorObj.executescript("""
		INSERT INTO salesman VALUES(5001,'James Hoog', 'New York', 0.15);
    		INSERT INTO salesman VALUES(5002,'Nail Knite', 'Paris', 0.25);
    		INSERT INTO salesman VALUES(5003,'Pit Alex', 'London', 0.15);
    		INSERT INTO salesman VALUES(5004,'Mc Lyon', 'Paris', 0.35);
    		INSERT INTO salesman VALUES(5005,'Paul Adam', 'Rome', 0.45);
		""")

		conn.commit()
		print("\nNumber of records after inserting rows:")
		cursor = cursorObj.execute('select * from salesman;')
		print(len(cursor.fetchall()))
	
	sqllite_conn = sql_connection()
	sql_table(sqllite_conn)

	if sqllite_conn:
		sqllite_conn.close()
		print("\nThe SQLite connection is closed")

def updateColumnValuesOfaRecord(filepath):
	def sql_connection(filepath):
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)
	def sql_table(conn):
		cursorObj = conn.cursor()
		cursorObj.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
		cursorObj.executescript("""
    		INSERT INTO salesman VALUES(5001,'James Hoog', 'New York', 0.15);
    		INSERT INTO salesman VALUES(5002,'Nail Knite', 'Paris', 0.25);
    		INSERT INTO salesman VALUES(5003,'Pit Alex', 'London', 0.15);
    		INSERT INTO salesman VALUES(5004,'Mc Lyon', 'Paris', 0.35);
   		INSERT INTO salesman VALUES(5005,'Paul Adam', 'Rome', 0.45);
    		""")    
		cursorObj.execute("SELECT * FROM salesman")
		rows = cursorObj.fetchall()
		print("Agent details: ")
		for row in rows:
			print(row)
		print("\nUpdate commission .15 to .45 where id is 5003:")
		sql_update_query = """Update salesman set commission = .45 where salesman_id = 5003"""
		cursorObj.execute(sql_update_query)
		conn.commit()
		print("Record Updated successfully ")    
		cursorObj.execute("SELECT * FROM salesman")
		rows = cursorObj.fetchall()
		print("\nAfter updating Agent details:")
		for row in rows:
			print(row)
	sqllite_conn = sql_connection()
	sql_table(sqllite_conn)
	if (sqllite_conn):
  		sqllite_conn.close()
  		print("\nThe SQLite connection is closed.")

def updateAllValuesOfColumn(filepath):

	def sql_connection(filepath):
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)
		
	def update(conn):
		cursorObj = conn.cursor()
		sql_update_query = """Update salesman set commission = .55"""
		cursorObj.execute(sql_update_query)
		conn.commit()
	
	sqllite_conn = sql_connection()
	update(sqllite_conn)
	if sqllite_conn:
		sqllite_conn.close()
		print('\nThe SQLite connection is closed.')

def delete_record(filepath):

	def sql_connection(filepath):
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)
		
	def delete(conn):
		cursorObj = conn.cursor()
		s_id = 5003
		cursorObj.execute("""DELETE FROM salesman WHERE salesman_id = ?""", (s_id,))
		conn.commit()
	
	sqllite_conn = sql_connection(filepath)
	delete(sqllite_conn)
	if sqllite_conn:
		sqllite_conn.close()
		print("\nThe SQLite connection is closed.")
	
def add_column(filepath):
	
	def sql_connection():
		try:
			conn = sqlite3.connect(filepath)
			return conn
		except Error:
			print(Error)
	
	def add_column(conn):
		cursorObj = conn.cursor()
		cursorObj.execute("""ALTER TABLE agent_master
		ADD COLUMN FLAG BOOLEAN;
		""")
		conn.commit()

	sqllite_conn = sql_connection()
	add_column(sqllite_conn)
	if sqllite_conn:
		sqllite_conn.close()
		print("\nThe SQLite connection is closed")
