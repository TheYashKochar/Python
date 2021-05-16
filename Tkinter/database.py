# Basic Address Book Program
# GUI and Database Integrated Program
from tkinter import *
from PIL import ImageTk,Image
import sqlite3
root = Tk()
root.title('Database Test')
root.geometry('400x400')

#conn = sqlite3.connect('dbs/address_book.db')

#c = conn.cursor()

'''
c.execute(""" CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)""")
'''
# Submit Function
def submit():
    conn = sqlite3.connect('dbs/address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state,:zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address':address.get(),
            'city':city.get(),
            'state':state.get(),
            'zipcode':zipcode.get()
        }
    )
    conn.commit()
    conn.close()
    # Clearing Text Boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# query function
def query():
    conn = sqlite3.connect('dbs/address_book.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses") # oid is primary key set but sqlite
    records = c.fetchall() # fetches all the records others : fetchone(), fetchmany(no. of items to be fetched)
    print_records = ''
    # looping results
    for record in records:
        #print_records += str(record) + "\n"
        #print_records += str(record[0]) + " "+ str(record[1]) +  " "+str(record[2]) + " "+ str(record[3]) + " "+str(record[4]) + " "+str(record[5]) + "\n"
        print_records += str(record[0]) + " "+ str(record[1]) +  "\t"+str(record[6]) +"\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan = 2)
    conn.commit()
    conn.close()

# delete record
def delete():
    conn = sqlite3.connect('dbs/address_book.db')
    c = conn.cursor()
    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())
    conn.commit()
    conn.close()

# update record
def update():
    #db connection
    conn = sqlite3.connect('dbs/address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute(""" UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = oid""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode' : zipcode_editor.get(),
            'oid' : record_id
        }
    )
    conn.commit()
    conn.close()
    editor.destroy()

# edit record
def edit():
    global editor
    editor = Tk()
    editor.title('Update a Record')
    editor.geometry('400x300')

    #db connection
    conn = sqlite3.connect('dbs/address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = "+ record_id)
    records = c.fetchall()

    # creating global variables
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Entry widgets
    f_name_editor =Entry(editor, width=30)
    f_name_editor.grid(row=0, column =1,padx=20,pady=(10,0))
    l_name_editor =Entry(editor, width=30)
    l_name_editor.grid(row=1, column =1,padx=20)
    address_editor =Entry(editor, width=30)
    address_editor.grid(row=2, column =1,padx=20)
    city_editor =Entry(editor, width=30)
    city_editor.grid(row=3, column =1,padx=20)
    state_editor =Entry(editor, width=30)
    state_editor.grid(row=4, column =1,padx=20)
    zipcode_editor =Entry(editor, width=30)
    zipcode_editor.grid(row=5, column =1,padx=20)

    # Create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0,column =0,pady=(10,0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1,column =0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2,column =0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3,column =0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4,column =0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5,column =0)

    # update button
    save_btn = Button(editor, text='Save Record', command=update)
    save_btn.grid(row=6,column =0, columnspan=2, pady =10, padx=10,ipadx=130)

    # loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    '''
    label = Label(editor,text='Connected to db')
    label.grid(row=0,column =0)
    '''
    conn.commit()
    conn.close()


# Entry widgets
f_name =Entry(root, width=30)
f_name.grid(row=0, column =1,padx=20,pady=(10,0))
l_name =Entry(root, width=30)
l_name.grid(row=1, column =1,padx=20)
address =Entry(root, width=30)
address.grid(row=2, column =1,padx=20)
city =Entry(root, width=30)
city.grid(row=3, column =1,padx=20)
state =Entry(root, width=30)
state.grid(row=4, column =1,padx=20)
zipcode =Entry(root, width=30)
zipcode.grid(row=5, column =1,padx=20)

delete_box = Entry(root,width=30)
delete_box.grid(row=9, column=1,pady=(10,0))

# Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0,column =0,pady=(10,0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1,column =0)
address_label = Label(root, text="Address")
address_label.grid(row=2,column =0)
city_label = Label(root, text="City")
city_label.grid(row=3,column =0)
state_label = Label(root, text="State")
state_label.grid(row=4,column =0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5,column =0)
delete_box_label =Label(root,text='Select ID')
delete_box_label.grid(row=9, column=0 ,pady=(10,0))

#create Submit button
submit_btn = Button(root, text="Add record to database",  command=submit)
submit_btn.grid(row=6,column=0,columnspan=2, pady =10,padx =10,ipadx=100)

# query button
query_btn = Button(root, text='Get Records', command=query)
query_btn.grid(row=7,column =0, columnspan=2, pady =10, padx=10,ipadx=130)

# delete button
delete_btn = Button(root, text='Delete Record', command=delete)
delete_btn.grid(row=10,column =0, columnspan=2, pady =10, padx=10,ipadx=126)

# update button
update_btn = Button(root, text='Update Record', command=edit)
update_btn.grid(row=11,column =0, columnspan=2, pady =10, padx=10,ipadx=124)

'''
# Commit changes
conn.commit()
# Close Connection
conn.close()
'''

root.mainloop()