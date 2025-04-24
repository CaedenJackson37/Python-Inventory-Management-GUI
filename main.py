"""

Author:  Caeden Jackson
Date written: 04/15/25
Assignment:   Module8 exercise1 part1 (1 or 2), etc.
Short Desc:   This program is my final project of developing a working GUI Breezy application.
This application is a GUI for a restaurant inventory management system.

"""
from breezypythongui import EasyFrame
from tkinter import *
from tkinter import messagebox

"""Window for the Home page"""
class Inventory(EasyFrame):

    """GUI"""

    def __init__(self):
        EasyFrame.__init__(self, title = "Inventory Management System", width = 800, height = 600)

        """Allows us to store employee details"""
        self.employees = []

        """Label for title"""
        headerLabel = self.addLabel(text = "Inventory Management System", row = 1, column = 0,columnspan = 4, sticky = "N,S,W,E")
        font = ("Arial", 20)
        headerLabel["font"] = font
        headerLabel["bg"] = "blue"
        headerLabel["fg"] = "white"


        """Label and Image for Home"""
        homeLabel = self.addLabel(text = "Home", row = 2, column = 1, sticky = "W")
        font = ("Arial", 20)
        homeLabel["font"] = font
        homeLabel["bg"] = "blue"
        homeLabel["fg"] = "white"

        home_image_Label = self.addLabel(text = "Home", row = 2, column = 0, sticky = "W")
        self.image = PhotoImage(file = "home.png")
        home_image_Label["image"] = self.image


        """Button and Image for Employee Page"""
        self.addLabel(text="Employee Management", row=4, column=0, columnspan=2, sticky="NSEW").configure(
            font=("Arial", 16, "bold"))

        self.addLabel(text="Employee Name:", row=5, column=0, sticky="E")
        self.empName = self.addTextField("", row=5, column=1)

        self.addLabel(text="Employee ID:", row=6, column=0, sticky="E")
        self.empID = self.addTextField("", row=6, column=1)

        self.addLabel(text="Employment Type:", row=7, column=0, sticky="E")
        self.empType = StringVar()
        self.empType.set("Select")
        self.empTypeMenu = OptionMenu(self, self.empType, "Full-Time", "Part-Time", "Contract", "Intern")
        self.empTypeMenu.grid(row=7, column=1, sticky="W")

        self.addLabel(text="Hire Date (YYYY-MM-DD):", row=8, column=0, sticky="E")
        self.hireDate = self.addTextField("", row=8, column=1)

        self.addButton(text="Add Employee", row=9, column=0, command=self.add_employee)
        self.addButton(text="View Employees", row=9, column=1, command=self.view_employees_window)


        """Button and Image for Product Page"""
        productButton = self.addButton(text = "Product", row = 4, column = 0, command = self.open_product_window).grid(row = 5, column = 0, sticky = "W")


        """Button and Image for Supplier Page"""
        supplierButton = self.addButton(text = "Supplier", row = 5, column = 0, command = self.open_supplier_window).grid(row = 6, column = 0, sticky = "W")



    """Functionality"""

    """Function for the Employee Page"""

    def open_employee_window(self):
        popup = Toplevel(self)
        popup.title("Employee Page")
        popup.configure(bg="white")
        popup.geometry("600x350")
        popup.resizable(False, False)

        # Title Label
        Label(popup, text="Employee Page", bg="blue", fg="white", font=("Arial", 20)).grid(row=0, column=0,
                                                                                           columnspan=2, pady=10,
                                                                                           padx=10)

        # Employee Name
        Label(popup, text="Employee Name:", bg="white").grid(row=1, column=0, sticky="E", padx=10, pady=5)
        name_entry = Entry(popup, width=30)
        name_entry.grid(row=1, column=1, padx=10)

        # Employee ID
        Label(popup, text="Employee ID:", bg="white").grid(row=2, column=0, sticky="E", padx=10, pady=5)
        id_entry = Entry(popup, width=30)
        id_entry.grid(row=2, column=1, padx=10)

        # Employment Type
        Label(popup, text="Employment Type:", bg="white").grid(row=3, column=0, sticky="E", padx=10, pady=5)
        emp_type_var = StringVar(popup)
        emp_type_var.set("Select")  # Default
        emp_type_menu = OptionMenu(popup, emp_type_var, "Full-Time", "Part-Time", "Contract", "Intern")
        emp_type_menu.grid(row=3, column=1, sticky="W", padx=10)

        # Hire Date
        Label(popup, text="Hire Date (YYYY-MM-DD):", bg="white").grid(row=4, column=0, sticky="E", padx=10, pady=5)
        hire_date_entry = Entry(popup, width=30)
        hire_date_entry.grid(row=4, column=1, padx=10)

        # Submit Button

    def add_employee(self):
        name = self.empName.getText().strip()
        emp_id = self.empID.getText().strip()
        emp_type = self.empType.get()
        hire_date = self.hireDate.getText().strip()

        if not name or not emp_id or emp_type == "Select" or not hire_date:
            messagebox.showerror("Missing Info", "Please fill in all fields.")
            return

        # Add employee to the internal list
        self.employees.append({
            "name": name,
            "id": emp_id,
            "type": emp_type,
            "hire_date": hire_date
        })

        messagebox.showinfo("Employee Added", f"Employee '{name}' (ID: {emp_id}) added successfully.")

        # Clear the fields
        self.empName.setText("")
        self.empID.setText("")
        self.empType.set("Select")
        self.hireDate.setText("")


    def view_employees_window(self):
        if not self.employees:
            messagebox.showinfo("No Employees", "No employee records yet.")
            return

        popup = Toplevel(self)
        popup.title("Employee List")
        popup.geometry("400x300")
        Label(popup, text="Employee Records", font=("Arial", 14, "bold")).pack(pady=10)

        for emp in self.employees:
            Label(popup, text=f"{emp['name']} (ID: {emp['id']}) - {emp['type']} - Hired: {emp['hire_date']}").pack(
                anchor="w", padx=20)

    """Function for the Product Page"""
    def open_product_window(self):
        popup = Toplevel(bg = "white")
        popup.title("Product Page")
        popup.resizable(False, False)
        popup.geometry("650x350")
        product_exit_button = Button(popup, text = "Exit", command = popup.destroy)
        product_label = Label(popup, text = "Product", bg = "blue", fg = "white", font = ("Arial", 20))

        """Button Packing"""
        product_exit_button.pack()
        product_label.pack()

        """Positions our buttons"""
        product_exit_button.place(x = 300, y = 325, anchor = "center")
        product_label.place(x = 300, y = 15, anchor = "center")

    """Function for the Supplier Page"""
    def open_supplier_window(self):
        popup = Toplevel(bg = "white")
        popup.title("Supplier Page")
        popup.resizable(False, False)
        popup.geometry("650x350")
        supplier_exit_button = Button(popup, text = "Exit", command = popup.destroy)
        supplier_label = Label(popup, text = "Supplier", bg = "blue", fg = "white", font = ("Arial", 20))

        """Button Packing"""
        supplier_exit_button.pack()
        supplier_label.pack()

        """Positions our buttons"""
        supplier_exit_button.place(x = 300, y = 325, anchor = "center")
        supplier_label.place(x = 300, y = 15, anchor = "center")


Inventory().mainloop()
