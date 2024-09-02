# README

## Database Management System

This project is a Database Management System (DBMS) application built using Python and Tkinter, designed to manage customers, orders, food items, and payments in an Oracle database.

### Project Overview

- **Name**: Database Management System
- **Language**: Python
- **Libraries**: 
  - `cx_Oracle`: For Oracle database connectivity
  - `tkinter`: For creating the graphical user interface (GUI)

### Features

- **Customer Management**: Insert, update, and delete customer records.
- **Order Management**: Manage orders with options to insert, update, and delete order details.
- **Food Item Management**: Add, update, and remove food items associated with orders.
- **Payment Management**: Handle payment records with options to insert, update, and delete payment details.
- **User-Friendly Interface**: Intuitive GUI for easy navigation and data management.

### Installation

To run this project locally, follow these steps:

1. **Prerequisites**: Ensure you have Python installed along with the `cx_Oracle` library. You can install it via pip:
   ```bash
   pip install cx_Oracle
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/db-management-system.git
   ```

3. **Navigate to the project directory**:
   ```bash
   cd db-management-system
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

### Database Configuration

- The application connects to an Oracle database. Make sure to set up the database with the required tables (`Customers`, `Orders`, `Food_Items`, `Payments`) before running the application.
- Update the database connection string in the `main.py` file as needed.

### How to Use

1. Launch the application, and a window with four tabs (Customers, Orders, Food Items, Payments) will appear.
2. Select a tab to manage the respective data.
3. Use the input fields to enter data and click the corresponding buttons (Insert, Update, Delete) to perform operations.
4. Success or error messages will be displayed as appropriate.

### Contact Information

- For inquiries or support, please reach out via email or GitHub.

### Contribution

If you would like to contribute to this project, please open an issue or submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for using this Database Management System! We hope it helps you manage your data efficiently.
