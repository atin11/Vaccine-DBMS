import mysql.connector
from tkinter import ttk, messagebox

#NOTES:
#house
#name
#gender
#dob
#email
#phone
#vaccination day

def connect():
    try:
        conn=mysql.connector.connect(user='root',password='12345678',host='localhost',database='school_management')
        cur=conn.cursor()
    except:
        messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

    cur.execute("CREATE TABLE IF NOT EXISTS vaccinations (house char(20) not null , name char(20) , gender char(10) , dob char(20) , day char(30) , phone char(11) , center char(20) , primary key (house))")
    conn.commit()

####################################################### SHOW_ALL ##################################################################

def show_all_data(tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345678',host='localhost',database='school_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

	cur.execute("SELECT * FROM vaccinations")
	data_rows = cur.fetchall()
	tree_table.delete(*tree_table.get_children())
	for row in data_rows:
		tree_table.insert('','end',values=(row))

####################################################################################################################################

########################################################## ADD #####################################################################

def add(house,name,gender,dob,day,phone,center,tree_table):
	#try:
	if (house and name and gender and dob and day and phone and center) != '':
		try:
			conn=mysql.connector.connect(user='root',password='12345678',host='localhost',database='school_management')
			cur=conn.cursor()
		except:
			messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

		cur.execute("INSERT INTO vaccinations (house,name,gender,dob,day,phone,center) VALUES ('%s','%s','%s','%s','%s','%s', '%s')"%(house,name,gender,dob,day,phone,center))
		conn.commit()
		show_all_data(tree_table)
	#except:
	#	messagebox.showerror('Error','An item with this ID already exists')

###################################################################################################################################

####################################################### DELETE ####################################################################

def delete(delete_id,tree_table):
	try:
		try:
			conn=mysql.connector.connect(user='root',password='12345678',host='localhost',database='school_management')
			cur=conn.cursor()
		except:
			messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

		delete_id = delete_id['values'][0]
		cur.execute("DELETE FROM vaccinations WHERE house='%s'"%(str(delete_id)))
		conn.commit()
		show_all_data(tree_table)
	except:
		pass

####################################################################################################################################

####################################################### UPDATE #####################################################################

def update(house,name,gender,dob,day,phone,center,tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345678',host='localhost',database='school_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

	cur.execute("UPDATE vaccinations SET name = '%s', gender = '%s', dob = '%s', day = '%s',phone = '%s', center = '%s' WHERE house = '%s'"%(name,gender,dob,day,phone,house, center))
	conn.commit()
	show_all_data(tree_table)

####################################################################################################################################

####################################################### SEARCH BY/FOR ##############################################################

def set_search_by_option(search_parameter,tree_table,search_parameter_entry):

	try:
		conn=mysql.connector.connect(user='root',password='12345678',host='localhost',database='school_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

	if search_parameter == 'house No.':
		search_parameter = 'house'
	if search_parameter == 'Name':
		search_parameter = 'name'
	if search_parameter == 'Gender':
		search_parameter = 'gender'
	if search_parameter == 'Date of Birth':
		search_parameter = 'dob'
	if search_parameter == 'Day':
		search_parameter = 'day'
	if search_parameter == 'Phone No.':
		search_parameter = 'phone'

	cur.execute("SELECT * FROM vaccinations WHERE %s = '%s'"%(search_parameter,search_parameter_entry))
	data_rows = cur.fetchall()
	tree_table.delete(*tree_table.get_children())
	for row in data_rows:
		tree_table.insert('','end',values=(row))

####################################################################################################################################

connect()
