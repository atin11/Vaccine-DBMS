from tkinter import *
from tkinter import ttk, messagebox
import AD_backend##table name is vaccinationa

class Student:
	def __init__(self,win):
		self.win = win
		self.win.title('Vaccination Management System')
		self.win.geometry('1000x600+150+40')
		self.bg = 'gray13'
		self.fg = 'red2'
		self.win["bg"] = self.bg

		##############FUNCTIONS#############################
		def clear():
			self.VAR_phone_no.set("")
			self.VAR_house_no.set("")
			self.VAR_name.set("")
			self.VAR_gender.set("")
			self.VAR_dob.set("")
			self.VAR_day.set("")
			self.VAR_center.set("")
                
		def on_click(*args):
			try:
				data = (self.table.item(self.table.focus()))['values']
				self.VAR_phone_no.set(data[5])
				self.VAR_house_no.set(data[0])
				self.VAR_name.set(data[1])
				self.VAR_gender.set(data[2])
				self.VAR_dob.set(data[3])
				self.VAR_day.set(data[4])
				self.VAR_center.set(data[6])
			except:
				messagebox.showerror('Error','Please select a relevent ID')
		####################################################
		
		##############HEADER#############
		header = Label(self.win,text="Vaccination Management System",font=('algerian',40,''),bg=self.bg,fg=self.fg)
		header.pack(side=TOP,fill=X)
		#################################

		##########ALL-VARIABLES#########
		self.VAR_house_no = StringVar()
		self.VAR_name = StringVar()
		self.VAR_gender = StringVar()
		self.VAR_dob = StringVar()
		self.VAR_day = StringVar()
		self.VAR_phone_no = StringVar()
		self.VAR_center = StringVar()
		################################

		########ENTRY-FIELD-FRAME########
		field_frame = Frame(self.win,bd=5,relief=RIDGE,bg=self.bg)
		field_frame.place(x=20,y=80,width=370,height=510)

		####HEAD####
		head = Label(field_frame,text='Information Form',bg=self.bg,fg=self.fg,font=('times',25,'bold underline'))
		head.grid(row=0,columnspan=2,padx=47)
		############

		###LABELS###
		L_name = Label(field_frame,text='Name',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_name.grid(row=1,column=0,pady=10,sticky='w',padx=20)
		L_house_no = Label(field_frame,text='House No.',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_house_no.grid(row=2,column=0,pady=10,sticky='w',padx=20)
		L_gender = Label(field_frame,text='Gender',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_gender.grid(row=3,column=0,pady=10,sticky='w',padx=20)
		L_dob = Label(field_frame,text='Date of birth',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_dob.grid(row=4,column=0,pady=10,sticky='w',padx=20)
		L_day = Label(field_frame,text='Day',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_day.grid(row=5,column=0,pady=10,sticky='w',padx=20)
		L_phone_no = Label(field_frame,text='Phone No.',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_phone_no.grid(row=6,column=0,pady=10,sticky='w',padx=20)
		L_center = Label(field_frame,text='Center',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_center.grid(row=7,column=0,pady=10,sticky='w',padx=20)
		############

		###ENTRY###
		E_name = Entry(field_frame,textvariable=self.VAR_name,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_name.grid(row=1,column=1,pady=10,sticky='w')
		E_house_no = Entry(field_frame,textvariable=self.VAR_house_no,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_house_no.grid(row=2,column=1,pady=10,sticky='w')
		E_gender = ttk.Combobox(field_frame,textvariable=self.VAR_gender,font=('times',20,'bold'),width=9,state='readonly')
		E_gender['values'] = ('Male','Female','Other')
		E_gender.grid(row=3,column=1,pady=10,sticky='w')
		E_dob = Entry(field_frame,textvariable=self.VAR_dob,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_dob.grid(row=4,column=1,pady=10,sticky='w')
		E_day = Entry(field_frame,textvariable=self.VAR_day,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_day.grid(row=5,column=1,pady=10,sticky='w')
		E_phone_no = Entry(field_frame,textvariable=self.VAR_phone_no,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_phone_no.grid(row=6,column=1,pady=10,sticky='w')
		E_center = Entry(field_frame,textvariable=self.VAR_center,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_center.grid(row=7,column=1,pady=10,sticky='w')
		###########

		##BUTTONS##
		B_add = Button(field_frame,text='Add',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',15,'bold'),width=15,bd=10,command=lambda:AD_backend.add(E_house_no.get(),E_name.get(),E_gender.get(),E_dob.get(),E_day.get(),E_phone_no.get(),E_center.get(),self.table))
		B_add.grid(row=8,column=0,padx=15,sticky='w')
		B_delete = Button(field_frame,text='Delete',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',15,'bold'),width=15,bd=10,command=lambda:AD_backend.delete(self.table.item(self.table.focus()),self.table))
		B_delete.grid(row=8,column=1,sticky='w',padx=15)
		B_update = Button(field_frame,text='Update',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',15,'bold'),width=15,bd=10,command=lambda:AD_backend.update(E_house_no.get(),E_name.get(),E_gender.get(),E_dob.get(),E_day.get(),E_phone_no.get(),E_center.get(),self.table))
		B_update.grid(row=9,column=0,pady=5,padx=15,sticky='w')
		B_clear = Button(field_frame,text='Clear',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',15,'bold'),width=15,bd=10,command=clear)
		B_clear.grid(row=9,column=1,pady=5,padx=15,sticky='w')
		###########

		#################################

		########INFORMATION-FRAME########
		info_frame = Frame(self.win,bd=5,relief=RIDGE,bg=self.bg)
		info_frame.place(x=410,y=80,width=570,height=510)

		####HEAD####
		search_by = Label(info_frame,text='Search By',bg=self.bg,fg=self.fg,font=('times',15,'bold underline'))
		search_by.grid(row=0,column=0)
		search_by_options = ttk.Combobox(info_frame,font=('times',11,'bold'),width=9,state='readonly')
		search_by_options['values'] = ('Name','House No.','Gender','Date of Birth','Day','Phone No.')
		search_by_options.grid(row=0,column=1,pady=10,sticky='w',padx=3)
		E_search_by = Entry(info_frame,bg='gray30',fg=self.fg,font=('times',12,'bold'),width=20,bd=2)
		E_search_by.grid(row=0,column=3,pady=10,sticky='w')
		B_search_by = Button(info_frame,text='Search',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',9,'bold'),width=20,bd=3,command=lambda:AD_backend.set_search_by_option(search_by_options.get(),self.table,E_search_by.get()))
		B_search_by.grid(row=0,column=4,pady=10,padx=5,sticky='w')
		B_showall = Button(info_frame,text='Show All',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',9,'bold'),width=30,bd=3,command=lambda:AD_backend.show_all_data(self.table))
		B_showall.grid(row=0,column=5,pady=10,sticky='w')
		############

		#####FIELD_INFORMATION-FRAME#####
		field_info_frame = Frame(info_frame,bd=3,relief=RIDGE,bg=self.bg)
		field_info_frame.place(x=13,y=45,width=535,height=450)

		##SCROLLS##
		x_scroll = Scrollbar(field_info_frame,orient=HORIZONTAL)
		y_scroll = Scrollbar(field_info_frame,orient=VERTICAL)
		###########

		###TABLE###
		self.table = ttk.Treeview(field_info_frame,columns=('house','name','gender','dob','day','phone', 'center'),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)
		self.table.heading('house',text='House No.')
		self.table.heading('name',text='Name')
		self.table.heading('gender',text='Gender')
		self.table.heading('dob',text='D.O.B')
		self.table.heading('day',text='Day')
		self.table.heading('phone',text='Phone No.')
		self.table.heading('center',text='Center')

		###########

		##SCROLLS##
		x_scroll.pack(side=BOTTOM,fill=X)
		y_scroll.pack(side=RIGHT,fill=Y)
		x_scroll.config(command =self.table.xview)
		y_scroll.config(command =self.table.yview)	
		###########
		
		#self.TABLE-CONFIGS#
		self.table['show'] = 'headings'
		self.table.column('house', anchor="center",width=50)
		self.table.column('name', anchor="center",width=120)
		self.table.column('gender', anchor="center",width=90)
		self.table.column('dob', anchor="center",width=90)
		self.table.column('day', anchor="center",width=150)
		self.table.column('phone', anchor="center",width=90)
		self.table.column('center', anchor="center",width=90)
		self.table.pack(fill=BOTH,expand=1)
		self.table.bind("<ButtonRelease-1>",on_click)
		###############

		#################################

		#################################


win = Tk()
obj = Student(win)
win.mainloop()
