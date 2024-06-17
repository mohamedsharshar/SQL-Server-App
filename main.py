import cx_Oracle
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Oracle database connection setup
conn = cx_Oracle.connect('sys/root@localhost:1521/orcl', mode=cx_Oracle.SYSDBA)
cursor = conn.cursor()

# Insert, Delete, and Update functions for customer table
def insert_customer():
    try:
        sql = "INSERT INTO Customers (Customer_id, Customer_Name, Customer_Email, Customer_Contact_No) VALUES (:1, :2, :3, :4)"
        cursor.execute(sql, (cust_id_entry.get(), cust_name_entry.get(), cust_email_entry.get(), cust_contact_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Customer inserted successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

def delete_customer():
    try:
        sql = "DELETE FROM Customers WHERE Customer_id = :1"
        cursor.execute(sql, (cust_id_entry.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Customer deleted successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

def update_customer():
    try:
        # Assuming you want to update only the Customer_Name column
        new_customer_name = cust_name_entry.get()
        customer_id = cust_id_entry.get()

        sql = "UPDATE Customers SET Customer_Name = :1 WHERE Customer_id = :2"
        cursor.execute(sql, (new_customer_name, customer_id))
        conn.commit()

        messagebox.showinfo("Success", "Customer name updated successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

# Insert, Delete, and Update functions for order table
def insert_order():
    try:
        sql = "INSERT INTO Orders (Order_No, Customer_id, Ticket_No, Order_Date, Order_Time, Order_Class) VALUES (:1, :2, :3, TO_DATE(:4,'YYYY-MM-DD'), TO_TIMESTAMP(:5, 'HH24:MI'), :6)"
        cursor.execute(sql, (order_no_entry.get(), cust_id2_entry.get(), ticket_no_entry.get(), order_date_entry.get(), order_time_entry.get(), order_class_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Order inserted successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

def delete_order():
    try:
        sql = "DELETE FROM Orders WHERE Order_No = :1"
        cursor.execute(sql, (order_no_entry.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Order deleted successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

def update_order():
    try:
        # Assuming you want to update only the Order_Class column
        new_order_class = order_class_entry.get()
        order_no = order_no_entry.get()

        sql = "UPDATE Orders SET Order_Class = :1 WHERE Order_No = :2"
        cursor.execute(sql, (new_order_class, order_no))
        conn.commit()

        messagebox.showinfo("Success", "Order class updated successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

# Food item insert, update, delete
def insert_food_item():
    try:
        sql = "INSERT INTO Food_Items (Food_id, Food_Price, Food_Specification, Food_Description, QTY, Order_No) VALUES (:1, :2, :3, :4, :5, :6)"
        cursor.execute(sql, (food_id_entry.get(), food_price_entry.get(), food_spec_entry.get(), food_desc_entry.get(), qty_entry.get(), order_no_food_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Food item inserted successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

def delete_food_item():
    try:
        sql = "DELETE FROM Food_Items WHERE Food_id = :1"
        cursor.execute(sql, (food_id_entry.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Food item deleted successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

def update_food_item():
    try:
        # Assuming you want to update only the Food_Price column
        new_food_price = food_price_entry.get()
        food_id = food_id_entry.get()

        sql = "UPDATE Food_Items SET Food_Price = :1 WHERE Food_id = :2"
        cursor.execute(sql, (new_food_price, food_id))
        conn.commit()

        messagebox.showinfo("Success", "Food item price updated successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

# Payment insert, delete, update
# Insert function for payments
def insert_payment():
    try:
        sql = "INSERT INTO Payments (Payment_id, Order_No, Payment_NetPrice, Payment_CashPaid) VALUES (:1, :2, :3, :4)"
        cursor.execute(sql, (payment_id_entry.get(), order_no_payment_entry.get(), payment_net_price_entry.get(), payment_cash_paid_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Payment inserted successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

# Delete function for payments
def delete_payment():
    try:
        sql = "DELETE FROM Payments WHERE Payment_id = :1"
        cursor.execute(sql, (payment_id_entry.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Payment deleted successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

# Update function for payments
def update_payment():
    try:
        new_net_price = payment_net_price_entry.get()
        new_cash_paid = payment_cash_paid_entry.get()
        payment_id = payment_id_entry.get()

        sql = "UPDATE Payments SET Payment_NetPrice = :1, Payment_CashPaid = :2 WHERE Payment_id = :3"
        cursor.execute(sql, (new_net_price, new_cash_paid, payment_id))
        conn.commit()

        messagebox.showinfo("Success", "Payment details updated successfully")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

# Fetch data from tables and display in Treeview
def fetch_data(table_name, treeview):
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        treeview.delete(*treeview.get_children())
        for row in rows:
            treeview.insert("", tk.END, values=row)
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", str(error))

# Define Tkinter window
root = tk.Tk()
root.title("Database Management")

# Create Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Customer Tab
customer_frame = ttk.Frame(notebook, width=400, height=400)
customer_frame.pack(fill='both', expand=True)
notebook.add(customer_frame, text='Customers')

for i in range(4):
    customer_frame.columnconfigure(i, weight=1)
for i in range(5):
    customer_frame.rowconfigure(i, weight=1)

cust_id_label = tk.Label(customer_frame, text="Customer ID")
cust_id_label.grid(row=0, column=0, padx=10, pady=10)
cust_id_entry = tk.Entry(customer_frame)
cust_id_entry.grid(row=0, column=1, padx=10, pady=10)

cust_name_label = tk.Label(customer_frame, text="Customer Name")
cust_name_label.grid(row=1, column=0, padx=10, pady=10)
cust_name_entry = tk.Entry(customer_frame)
cust_name_entry.grid(row=1, column=1, padx=10, pady=10)

cust_email_label = tk.Label(customer_frame, text="Customer Email")
cust_email_label.grid(row=2, column=0, padx=10, pady=10)
cust_email_entry = tk.Entry(customer_frame)
cust_email_entry.grid(row=2, column=1, padx=10, pady=10)

cust_contact_label = tk.Label(customer_frame, text="Customer Contact No")
cust_contact_label.grid(row=3, column=0, padx=10, pady=10)
cust_contact_entry = tk.Entry(customer_frame)
cust_contact_entry.grid(row=3, column=1, padx=10, pady=10)

insert_button = tk.Button(customer_frame, text="Insert", command=insert_customer)
insert_button.grid(row=4, column=0, padx=10, pady=10)

delete_button = tk.Button(customer_frame, text="Delete", command=delete_customer)
delete_button.grid(row=4, column=1, padx=10, pady=10)

update_button = tk.Button(customer_frame, text="Update", command=update_customer)
update_button.grid(row=4, column=2, padx=10, pady=10)

# Order Tab
orders_frame = ttk.Frame(notebook, width=400, height=400)
orders_frame.pack(fill='both', expand=True)
notebook.add(orders_frame, text='Orders')

for i in range(4):
    orders_frame.columnconfigure(i, weight=1)
for i in range(7):
    orders_frame.rowconfigure(i, weight=1)

order_no_label = tk.Label(orders_frame, text="Order No")
order_no_label.grid(row=0, column=0, padx=10, pady=10)
order_no_entry = tk.Entry(orders_frame)
order_no_entry.grid(row=0, column=1, padx=10, pady=10)

cust_id2_label = tk.Label(orders_frame, text="Customer ID")
cust_id2_label.grid(row=1, column=0, padx=10, pady=10)
cust_id2_entry = tk.Entry(orders_frame)
cust_id2_entry.grid(row=1, column=1, padx=10, pady=10)

ticket_no_label = tk.Label(orders_frame, text="Ticket No")
ticket_no_label.grid(row=2, column=0, padx=10, pady=10)
ticket_no_entry = tk.Entry(orders_frame)
ticket_no_entry.grid(row=2, column=1, padx=10, pady=10)

order_date_label = tk.Label(orders_frame, text="Order Date (YYYY-MM-DD)")
order_date_label.grid(row=3, column=0, padx=10, pady=10)
order_date_entry = tk.Entry(orders_frame)
order_date_entry.grid(row=3, column=1, padx=10, pady=10)

order_time_label = tk.Label(orders_frame, text="Order Time (HH:MM)")
order_time_label.grid(row=4, column=0, padx=10, pady=10)
order_time_entry = tk.Entry(orders_frame)
order_time_entry.grid(row=4, column=1, padx=10, pady=10)

order_class_label = tk.Label(orders_frame, text="Order Class")
order_class_label.grid(row=5, column=0, padx=10, pady=10)
order_class_entry = tk.Entry(orders_frame)
order_class_entry.grid(row=5, column=1, padx=10, pady=10)

insert_button2 = tk.Button(orders_frame, text="Insert", command=insert_order)
insert_button2.grid(row=6, column=0, padx=10, pady=10)

delete_button2 = tk.Button(orders_frame, text="Delete", command=delete_order)
delete_button2.grid(row=6, column=1, padx=10, pady=10)

update_button2 = tk.Button(orders_frame, text="Update", command=update_order)
update_button2.grid(row=6, column=2, padx=10, pady=10)

# Food Items Tab
food_frame = ttk.Frame(notebook, width=400, height=400)
food_frame.pack(fill='both', expand=True)
notebook.add(food_frame, text='Food Items')

for i in range(4):
    food_frame.columnconfigure(i, weight=1)
for i in range(7):
    food_frame.rowconfigure(i, weight=1)

food_id_label = tk.Label(food_frame, text="Food ID")
food_id_label.grid(row=0, column=0, padx=10, pady=10)
food_id_entry = tk.Entry(food_frame)
food_id_entry.grid(row=0, column=1, padx=10, pady=10)

food_price_label = tk.Label(food_frame, text="Food Price")
food_price_label.grid(row=1, column=0, padx=10, pady=10)
food_price_entry = tk.Entry(food_frame)
food_price_entry.grid(row=1, column=1, padx=10, pady=10)

food_spec_label = tk.Label(food_frame, text="Food Specification")
food_spec_label.grid(row=2, column=0, padx=10, pady=10)
food_spec_entry = tk.Entry(food_frame)
food_spec_entry.grid(row=2, column=1, padx=10, pady=10)

food_desc_label = tk.Label(food_frame, text="Food Description")
food_desc_label.grid(row=3, column=0, padx=10, pady=10)
food_desc_entry = tk.Entry(food_frame)
food_desc_entry.grid(row=3, column=1, padx=10, pady=10)

qty_label = tk.Label(food_frame, text="Quantity")
qty_label.grid(row=4, column=0, padx=10, pady=10)
qty_entry = tk.Entry(food_frame)
qty_entry.grid(row=4, column=1, padx=10, pady=10)

order_no_food_label = tk.Label(food_frame, text="Order No")
order_no_food_label.grid(row=5, column=0, padx=10, pady=10)
order_no_food_entry = tk.Entry(food_frame)
order_no_food_entry.grid(row=5, column=1, padx=10, pady=10)

insert_button3 = tk.Button(food_frame, text="Insert", command=insert_food_item)
insert_button3.grid(row=6, column=0, padx=10, pady=10)

delete_button3 = tk.Button(food_frame, text="Delete", command=delete_food_item)
delete_button3.grid(row=6, column=1, padx=10, pady=10)

update_button3 = tk.Button(food_frame, text="Update", command=update_food_item)
update_button3.grid(row=6, column=2, padx=10, pady=10)

# Payments Tab
payments_frame = ttk.Frame(notebook, width=400, height=400)
payments_frame.pack(fill='both', expand=True)
notebook.add(payments_frame, text='Payments')

for i in range(4):
    payments_frame.columnconfigure(i, weight=1)
for i in range(6):
    payments_frame.rowconfigure(i, weight=1)

payment_id_label = tk.Label(payments_frame, text="Payment ID")
payment_id_label.grid(row=0, column=0, padx=10, pady=10)
payment_id_entry = tk.Entry(payments_frame)
payment_id_entry.grid(row=0, column=1, padx=10, pady=10)

order_no_payment_label = tk.Label(payments_frame, text="Order No")
order_no_payment_label.grid(row=1, column=0, padx=10, pady=10)
order_no_payment_entry = tk.Entry(payments_frame)
order_no_payment_entry.grid(row=1, column=1, padx=10, pady=10)

payment_net_price_label = tk.Label(payments_frame, text="Payment Net Price")
payment_net_price_label.grid(row=2, column=0, padx=10, pady=10)
payment_net_price_entry = tk.Entry(payments_frame)
payment_net_price_entry.grid(row=2, column=1, padx=10, pady=10)

payment_cash_paid_label = tk.Label(payments_frame, text="Payment Cash Paid")
payment_cash_paid_label.grid(row=3, column=0, padx=10, pady=10)
payment_cash_paid_entry = tk.Entry(payments_frame)
payment_cash_paid_entry.grid(row=3, column=1, padx=10, pady=10)

insert_button4 = tk.Button(payments_frame, text="Insert", command=insert_payment)
insert_button4.grid(row=4, column=0, padx=10, pady=10)

delete_button4 = tk.Button(payments_frame, text="Delete", command=delete_payment)
delete_button4.grid(row=4, column=1, padx=10, pady=10)

update_button4 = tk.Button(payments_frame, text="Update", command=update_payment)
update_button4.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
