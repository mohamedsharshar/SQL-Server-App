Program Description
This Python program is a graphical user interface (GUI) application for managing a database. It utilizes the Tkinter library for creating the GUI and the cx_Oracle library for interacting with an Oracle database. The application is designed to perform CRUD (Create, Read, Update, Delete) operations on four database tables: Customers, Orders, Food_Items, and Payments. The interface is organized into tabs, each dedicated to one of these tables.

Key Components:
Imports and Database Connection:

cx_Oracle is imported to handle database interactions.
tkinter and ttk from the Tkinter library are imported for creating the GUI.
A connection to the Oracle database is established using cx_Oracle.connect.
CRUD Functions:

Customers Table:
insert_customer: Inserts a new customer record.
delete_customer: Deletes a customer record based on the customer ID.
update_customer: Updates the customer name based on the customer ID.
Orders Table:
insert_order: Inserts a new order record.
delete_order: Deletes an order record based on the order number.
update_order: Updates the order class based on the order number.
Food_Items Table:
insert_food_item: Inserts a new food item record.
delete_food_item: Deletes a food item record based on the food ID.
update_food_item: Updates the food price based on the food ID.
Payments Table:
insert_payment: Inserts a new payment record.
delete_payment: Deletes a payment record based on the payment ID.
update_payment: Updates the net price and cash paid for a payment based on the payment ID.
Data Fetching Function:

fetch_data: Fetches all records from a specified table and displays them in a Treeview widget.
GUI Setup:

A Tkinter window (root) is created and titled "Database Management".
A Notebook widget (notebook) is added to the root window to manage multiple tabs.
Four tabs are created for managing Customers, Orders, Food_Items, and Payments. Each tab contains entry fields, labels, and buttons for inserting, deleting, and updating records.
The grid layout manager is used to organize the widgets within each tab. The columnconfigure and rowconfigure methods ensure that the elements are centered within each frame by setting equal weights.
Detailed Tab Description:
Customers Tab:

Fields: Customer ID, Customer Name, Customer Email, Customer Contact No.
Buttons: Insert, Delete, Update.
Layout: 4 rows and 2 columns, with an additional row for the buttons.
Orders Tab:

Fields: Order No, Customer ID, Ticket No, Order Date (YYYY-MM-DD), Order Time (HH
), Order Class.
Buttons: Insert, Delete, Update.
Layout: 6 rows and 2 columns, with an additional row for the buttons.
Food_Items Tab:

Fields: Food ID, Food Price, Food Specification, Food Description, Quantity, Order No.
Buttons: Insert, Delete, Update.
Layout: 6 rows and 2 columns, with an additional row for the buttons.
Payments Tab:

Fields: Payment ID, Order No, Payment Net Price, Payment Cash Paid.
Buttons: Insert, Delete, Update.
Layout: 4 rows and 2 columns, with an additional row for the buttons.
Each tab uses the grid layout to ensure that all input fields and buttons are properly aligned and centered. The rows and columns are configured to expand and adjust the layout dynamically, providing a user-friendly interface.

Overall, this program provides a comprehensive solution for managing the data within an Oracle database through an intuitive GUI, making it easier for users to perform CRUD operations on multiple tables.
