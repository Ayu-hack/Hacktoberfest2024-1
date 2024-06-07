from tkinter import*
import pyodbc
from tkinter import messagebox
def connect():
    try:
        server = 'localhost\SQLEXPRESS'
        database = 'bank'

        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        connection = pyodbc.connect(connection_string)

        print(f"Connected to SQL Server: {server}, Database: {database}")

        return connection

    except pyodbc.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


def insert_data(name, phone, email, gender, nationality, state, address, password, username, dob,balance):
    
    connection=connect()
    if connection:
        try:
            cursor = connection.cursor()
            sql_insert = """
            INSERT INTO registration(Name, Phone, Email, Gender, Nationality, State, Address, Username, Password, DOB,balance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
            """
            values = (name, phone, email, gender, nationality, state, address, username, password, dob,balance)

            cursor.execute(sql_insert, values)
            connection.commit()
            cursor.close()

            print("Data inserted successfully") 

            messagebox.showinfo("welcome ", "vishnu legacy bank : " + username)

        except pyodbc.Error as e:
            messagebox.showinfo("DATABASE SERVER ERROR ",f"Error inserting data: {e}")
        finally:
            connection.close()





def login_data(username, password):
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM registration WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            registration = cursor.fetchone()

            if registration:
                #profile(username)
                print("ADD PROFILE PAGE AFTER LOGIN SUCCESSFULLY")
            else:
                messagebox.showinfo(
                    "Login Failed", "Login failed for username: " + username)
        except pyodbc.Error as e:
            print(f"Error executing SQL query: {e}")
        finally:
            connection.close()

def login_user():
    login_window = Tk()
    login_window.title("LOGIN")

    def login_button_click():
        entered_username = username_entry.get()
        entered_password = password_entry.get()
        print("Entered Username:", entered_username)
        print("Entered Password:", entered_password)

        if not entered_username or not entered_password:
            print("Please enter both username and password")
            return

        if login_data(entered_username, entered_password):
            print("Login successful")

    heading_lb = Label(login_window, text="LOGIN", bg="SystemButtonFace", font=("Arial", 25))
    heading_lb.grid(row=0, padx=470, sticky="w")

    username_label = Label(login_window, text="USERNAME", bg="SystemButtonFace", font=("Arial", 16))
    username_label.grid(row=1, padx=400, sticky="w", pady=20)
    username_entry = Entry(login_window, width=30)
    username_entry.grid(row=1, padx=650, sticky="w")

    password_label = Label(login_window, text="PASSWORD", bg="SystemButtonFace", font=("Arial", 16))
    password_label.grid(row=2, padx=400, sticky="w", pady=20)
    password_entry = Entry(login_window, show="*", width=30)  # Use show="*" to hide password
    password_entry.grid(row=2, padx=650, sticky="w")

    login_btn = Button(login_window, text="LOGIN", bg="grey", fg="white", font=("bold", 20), width=10, command=login_button_click)
    login_btn.grid(row=4, sticky="w", padx=470, pady=30)
    
    forget_btn = Button(login_window, text="FORGET PASSWORD", bg="SystemButtonFace", bd=0, font=("Arial", 16))
    forget_btn.grid(row=4, padx=800, sticky="w")
    login_window.mainloop()


def register():
    register_window = Tk()
    register_window.title("REGISTER")
    name = StringVar()
    DOB = StringVar()
    phone_no = StringVar()
    emailid = StringVar()
    gender = StringVar()
    nationality = StringVar()
    state = StringVar()
    address = StringVar()
    password = StringVar()
    username = StringVar()


    fields = [
        ("NAME"), ("DATE OF BIRTH"), ("PHONE NO."),
        ("EMAIL ID"), ("GENDER"), ("NATION"),
        ("STATE"), ("ADDRESS"), ("Username"), ("PASSWORD")
    ]

    for i, (field_name) in enumerate(fields, start=1):
        label = Label(register_window, text=field_name,
                      bg="SystemButtonFace", font=("Arial", 16))
        label.grid(row=i, padx=400, sticky="w", pady=20)

    
    name_entry = Entry(register_window, textvariable=name, width=30)
    name_entry.grid(row=1, padx=650, sticky="w")
    phone_entry = Entry(register_window, textvariable=phone_no, width=30)
    phone_entry.grid(row=3, padx=650, sticky="w")
    email_entry = Entry(register_window, textvariable=emailid, width=30)
    email_entry.grid(row=4, padx=650, sticky="w")
    gender_entry = Entry(register_window, textvariable=gender, width=30)
    gender_entry.grid(row=5, padx=650, sticky="w")
    nation_entry = Entry(register_window, textvariable=nationality, width=30)
    nation_entry.grid(row=6, padx=650, sticky="w")
    state_entry = Entry(register_window, textvariable=state, width=30)
    state_entry.grid(row=7, padx=650, sticky="w")
    add_entry = Entry(register_window, textvariable=address, width=30)
    add_entry.grid(row=8, padx=650, sticky="w")
    pass_entry = Entry(register_window, textvariable=password, width=30)
    pass_entry.grid(row=10, padx=650, sticky="w")
    user_entry=Entry(register_window, textvariable=username, width=30)
    user_entry.grid(row=9, padx=650, sticky="w")
    
    heading_lb = Label(register_window, text="CREATE YOUR ACCOUNT",
                       bg="SystemButtonFace", font=("Arial", 25))
    heading_lb.grid(row=0, padx=400, sticky="w")

    dob_label = Label(register_window, text="DATE OF BIRTH",bg="SystemButtonFace", font=("Arial", 16))
    dob_label.grid(row=2, padx=400, sticky="w", pady=20)

    dob_entry = Entry(register_window, textvariable=DOB, width=30)
    dob_entry.grid(row=2, padx=650, sticky="w")

    balance=0

    register_btn = Button(register_window, text="REGISTER", bg="grey", fg="white", font=("bold", 20), width=10, command=lambda:insert_data(name_entry.get(),phone_entry.get(),email_entry.get(),gender_entry.get(),nation_entry.get(),state_entry.get(),add_entry.get(),pass_entry.get(),user_entry.get(),dob_entry.get(),balance))
    register_btn.grid(row=10, sticky="e")

    login_btn = Button(register_window, text="LOGIN", bg="grey",fg="white", font=("bold", 20) ,command=login_user)
    login_btn.grid(row=10, padx=55, sticky="w")

    register_window.mainloop()



register()