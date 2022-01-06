from tkinter import *
import sqlite3

root = Tk()
root.title('Address Book')
root.geometry('700x300')
root.configure(background='#000000')

key = sqlite3.connect('The Database.db')
cur = key.cursor()

# insert table
# cur.execute("""
#     CREATE TABLE address_table (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         zipcode integer
#     )
# """) 

# LABEL WIDGETS
first_label = Label(root, text='First Name', font=('Arial', 12), bg='#00cccc')
first_label.grid(row=0, column=0, sticky='WE', ipady=5,
                 pady=(15, 0))  # The tuple adds padding 15 to the top of the widget, but padding 0 to the bottom

last_label = Label(root, text='Last Name', font=('Arial', 12), bg='#00e6e6', fg='black')
last_label.grid(row=1, column=0, sticky='WE', ipady=5)

address_label = Label(root, text='Address', font=('Arial', 12), bg='#4dffff')
address_label.grid(row=2, column=0, sticky='WE', ipady=5)

city_label = Label(root, text='City', font=('Arial', 12), bg='#99ffff')
city_label.grid(row=3, column=0, sticky='WE', ipady=5)

zipcode_label = Label(root, text='Zipcode', font=('Arial', 12), bg='#ccffff')
zipcode_label.grid(row=4, column=0, sticky='WE', ipady=5)

# ENTRY WIDGETS
f_name = Entry(root, width=30, bg='#d9d9d9')
f_name.grid(row=0, column=1, sticky='WE', columnspan=4, ipady=7, pady=(15, 0))

l_name = Entry(root, width=30, bg='#d9d9d9')
l_name.grid(row=1, column=1, sticky='WE', columnspan=4, ipady=7)

address = Entry(root, width=30, bg='#d9d9d9')
address.grid(row=2, column=1, sticky='WE', columnspan=4, ipady=7)

city = Entry(root, width=30, bg='#d9d9d9')
city.grid(row=3, column=1, sticky='WE', columnspan=4, ipady=7)

zipcode = Entry(root, width=30, bg='#d9d9d9')
zipcode.grid(row=4, column=1, sticky='WE', columnspan=4, ipady=7)


# FUNCTIONS
# Submit function
def submit_record():
    # When you use a sqlite3 syntax inside a function, its like you've open a new module
    # and you gotta connect to the database again, create the cursor etc.
    key = sqlite3.connect('The Database.db')
    cur = key.cursor()

    mList = [f_name.get(), l_name.get(), address.get(), city.get(), zipcode.get()]
    # INSERT INTO TABLE
    cur.execute("INSERT INTO address_table VALUES(?,?,?,?,?)", mList)

    key.commit()
    key.close()
    # Delete everything innside entry after submitting a record
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)


# Query function
def query_func():
    key = sqlite3.connect('The Database.db')
    cur = key.cursor()

    cur.execute('SELECT rowid,* FROM address_table')
    records = cur.fetchall()
    i = ""
    for data in records:
        i += str(data) + '\n'
        # The reason i has to be created, instead of us just having the label widget within the loop is because when the
    # label widget displays 'data' for each iteration of the loop, the data isn't displayed on a new line, like the way
    # the print statement does it. The label widget displays the data on the same line, on top of the previous data which
    # is obviosuly unreadable (overlapping data)
    # Also, because we are using + to concatenate, we convert 'data' to string. 'Data' actually represents each tuple from the
    # list of tuples. So, i don't get how we can convert a tuple to a string, but somehow sqlite3 does it.
    data_label = Label(root, text=i, bg='#ffffff', font=('Arial', 12))
    data_label.grid(row=10, column=1, columnspan=4, sticky='WE', pady=(15, 0))

    # Leave
    key.commit()
    key.close()
    ##########


# Delete Function
def delete_func():
    key = sqlite3.connect('The Database.db')
    cur = key.cursor()
    cur.execute(
        'DELETE FROM address_table WHERE rowid=' + delete_entry.get())  # You don't put a comma, you concatenate which is really strange.
    delete_entry.delete(0, END)

    key.commit()
    key.close()
    ###########


# Edit Record Function
def update_record():
    # TOP WINDOW SYNTAX
    top = Toplevel()  # Even using Tk() works
    top.title('Edit Record')
    top.geometry('400x400')
    # Button(top, text='EXIT', command= top.destroy).pack()   #This gives an error, and I think its because of the pack, since I get
    # this error: _tkinter.TclError: cannot use geometry manager grid
    # inside . which already has slaves managed by pack
    # TKINTER SYNTAX
    # LABEL WIDGETS
    first_label = Label(top, text='First Name', font='Arial', bg='#ccccff')
    first_label.grid(row=0, column=0, pady=(15, 0),
                     sticky='WE')  # The tuple adds padding 15 to the top of the widget, but padding 0 to the bottom

    last_label = Label(top, text='Last Name', font='Arial', bg='#cceeff', fg='black')
    last_label.grid(row=1, column=0, sticky='WE')

    address_label = Label(top, text='Address', font='Arial', bg='#ff9999')
    address_label.grid(row=2, column=0, sticky='WE')

    city_label = Label(top, text='City', font='Arial', bg='#b3ffb3')
    city_label.grid(row=3, column=0, sticky='WE')

    zipcode_label = Label(top, text='Zipcode', font='Arial', bg='#ffff99')
    zipcode_label.grid(row=4, column=0, sticky='WE')

    # ENTRY WIDGETS
    global f_name_update
    global l_name_update
    global address_update
    global city_update
    global zipcode_update

    f_name_update = Entry(top, width=30)
    f_name_update.grid(row=0, column=1, sticky='WE', ipady=5, pady=(15, 0), columnspan=2)

    l_name_update = Entry(top, width=30)
    l_name_update.grid(row=1, column=1, sticky='WE', ipady=5, columnspan=2)

    address_update = Entry(top, width=30)
    address_update.grid(row=2, column=1, sticky='WE', ipady=5, columnspan=2)

    city_update = Entry(top, width=30)
    city_update.grid(row=3, column=1, sticky='WE', ipady=5, columnspan=2)

    zipcode_update = Entry(top, width=30)
    zipcode_update.grid(row=4, column=1, sticky='WE', ipady=5, columnspan=2)

    # BUTTON WIDGETS
    # Save stuff
    submit = Button(top, text='Save Changes', command=save_func, bg='#cccccc', border=0, font='Arial')
    submit.grid(row=5, column=1, ipady=5, ipadx=5, pady=(15, 0), columnspan=2, sticky='WE')
    # Exit Stuff
    exit_button = Button(top, text='EXIT', command=top.destroy, bg='#33cccc', fg='white', border=0, font='Arial')
    exit_button.grid(row=6, column=1, pady=(15, 0), columnspan=2)

    # SQL SYNTAX
    key = sqlite3.connect('The Database.db')
    cur = key.cursor()
    cur.execute(
        'SELECT * FROM address_table WHERE rowid=' + update_entry.get())  # The issue was that i put a comma before the +. I thought
    # that there had to be a comma because it was also there for the placeholder thing when inserting multiple records.
    records = cur.fetchall()
    for record in records:
        f_name_update.insert(0, record[0])
        l_name_update.insert(0, record[1])
        address_update.insert(0, record[2])
        city_update.insert(0, record[3])
        zipcode_update.insert(0, record[4])
    # DONT TOUCH
    key.commit()
    key.close()


def save_func():
    key = sqlite3.connect('The Database.db')
    cur = key.cursor()  # From what Ive seen in the tutorials, :f_name seems to be a placeholer just like the
    # question mark placeholders we were using. If the field name is f_name, the placeholder doesn't have to be that name, but for the
    # sake of simplicity, it's better to put it that way.
    cur.execute("""UPDATE address_table SET     
            first_name= :first_name,
            last_name= :last_name,              
            address= :address,
            city= :city,
            zipcode= :zipcode
            WHERE rowid= :rowid""",
                {
                    'first_name': f_name_update.get(),  # Don't forget the commas here and also above.
                    'last_name': l_name_update.get(),
                    'address': address_update.get(),
                    'city': city_update.get(),
                    'zipcode': zipcode_update.get(),
                    'rowid': update_entry.get()
                    # Remember, the last one doesn't get a comma there is nothing coming after it.
                }
                # While the placeholders have colons before their name, for some reason, you don't have to include them in the dictionary.
                )

    # DON'T TOUCH
    # update_entry.delete(0,END)
    key.commit()
    key.close()


# BUTTON WIDGETS
# Insert Stuff
insert = Button(root, text='Insert Record', command=submit_record, bg='#ff4d94', border=0, font=('Arial', 12),
                fg='white')
insert.grid(row=0, column=5, padx=(15, 0), pady=(15, 0),
            sticky='WE')  # Apparently, there is a form of paddin called ipadx and ipady

# Fetch Stuff- It is always the last button
fetch = Button(root, text='Fetch Records', command=query_func, bg='#ff4d94', border=0, font=('Arial', 12), fg='white')
fetch.grid(row=1, column=5, padx=(15, 0), sticky='WE')

# Update Record Stuff
update = Button(root, text='Update Record', command=update_record, bg='#ff4d94', border=0, font=('Arial', 12),
                fg='white')
update.grid(row=6, column=1, ipady=5, ipadx=5, pady=(15, 0), sticky='WE', padx=(15, 0))

update_label = Label(root, text='Row ID to Update:', font=('Arial', 10), bg="#ffffff")
update_label.grid(row=5, column=1, ipady=5, ipadx=5, pady=(15, 0), sticky='WE', padx=(15, 0))

update_entry = Entry(root, width=4, bg='#d9d9d9')
update_entry.grid(row=5, column=2, ipady=5, ipadx=5, pady=(15, 0), padx=(15, 0))

# Delete Stuff
delete = Button(root, text='Delete Record', command=delete_func, bg='#ff4d94', border=0, font=('Arial', 12), fg='white')
delete.grid(row=6, column=3, ipady=5, ipadx=5, pady=(15, 0), sticky='WE', padx=(15, 0))

delete_label = Label(root, text='Row ID to Delete:', font=('Arial', 10), bg="#ffffff")
delete_label.grid(row=5, column=3, ipady=5, ipadx=5, pady=(15, 0), sticky='WE', padx=(15, 0))

delete_entry = Entry(root, width=4, bg='#d9d9d9')
delete_entry.grid(row=5, column=4, ipady=5, ipadx=5, pady=(15, 0), padx=(15, 0))

# Don't Touch
key.commit()
key.close()
root.mainloop()
