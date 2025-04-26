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

class Inventory(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Inventory Management System", width=800, height=600)

        """Lists for Employees, Products, and Suppliers"""
        self.employees = []
        self.products = []
        self.suppliers = []

        """Title Label"""
        headerLabel = self.addLabel(text="Inventory Management System", row=0, column=0, columnspan=4, sticky="NSEW")
        headerLabel["font"] = ("Arial", 20)
        headerLabel["bg"] = "blue"
        headerLabel["fg"] = "white"

        """Home Image"""
        home_image_Label = self.addLabel(text="", row=1, column=0, sticky="W")
        self.image = PhotoImage(file="home.png")
        home_image_Label["image"] = self.image

        """Home Label"""
        homeLabel = self.addLabel(text="Home", row=1, column=1, sticky="W")
        homeLabel["font"] = ("Arial", 20)
        homeLabel["bg"] = "blue"
        homeLabel["fg"] = "white"


        """Buttons for Employee, Product, and Supplier Windows"""
        self.addButton(text="Employee", row=3, column=0, command=self.open_employee_window)
        self.addButton(text="Product", row=3, column=1, command=self.open_product_window)
        self.addButton(text="Supplier", row=3, column=2, command=self.open_supplier_window)

    """Function for Employee Window"""
    def open_employee_window(self):
        popup = Toplevel(self)
        popup.title("Employee Management")
        popup.geometry("400x300")
        popup.configure(bg="white")
        popup.resizable(False, False)

        Label(popup, text="Employee Management", bg="blue", fg="white", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=2, pady=10)

        Label(popup, text="Employee Name:", bg="white").grid(row=1, column=0, sticky="E", padx=10)
        self.empName = Entry(popup, width=25)
        self.empName.grid(row=1, column=1, padx=10)

        Label(popup, text="Employee ID:", bg="white").grid(row=2, column=0, sticky="E", padx=10)
        self.empID = Entry(popup, width=25)
        self.empID.grid(row=2, column=1, padx=10)

        Label(popup, text="Employment Type:", bg="white").grid(row=3, column=0, sticky="E", padx=10)
        self.empType = StringVar()
        self.empType.set("Select")
        OptionMenu(popup, self.empType, "Full-Time", "Part-Time", "Contract", "Intern").grid(row=3, column=1, sticky="W", padx=10)

        Label(popup, text="Hire Date (YYYY-MM-DD):", bg="white").grid(row=4, column=0, sticky="E", padx=10)
        self.hireDate = Entry(popup, width=25)
        self.hireDate.grid(row=4, column=1, padx=10)

        Button(popup, text="Add Employee", command=self.add_employee).grid(row=5, column=0, pady=15)
        Button(popup, text="View Employees", command=self.view_employees_window).grid(row=5, column=1, pady=15)

    """Function to add Employee"""
    def add_employee(self):
        name = self.empName.get().strip()
        emp_id = self.empID.get().strip()
        emp_type = self.empType.get()
        hire_date = self.hireDate.get().strip()

        if not name or not emp_id or emp_type == "Select" or not hire_date:
            messagebox.showerror("Missing Info", "Please fill in all fields.")
            return

        self.employees.append({
            "name": name,
            "id": emp_id,
            "type": emp_type,
            "hire_date": hire_date
        })

        messagebox.showinfo("Employee Added", f"Employee '{name}' (ID: {emp_id}) added successfully.")
        self.empName.delete(0, END)
        self.empID.delete(0, END)
        self.empType.set("Select")
        self.hireDate.delete(0, END)

    """Function to view the Employee Window"""
    def view_employees_window(self):
        if not self.employees:
            messagebox.showinfo("No Employees", "No employee records yet.")
            return

        popup = Toplevel(self)
        popup.title("Employee List")
        popup.geometry("400x300")
        Label(popup, text="Employee Records", font=("Arial", 14, "bold")).pack(pady=10)

        for emp in self.employees:
            Label(popup, text=f"{emp['name']} (ID: {emp['id']}) - {emp['type']} - Hired: {emp['hire_date']}").pack(anchor="w", padx=20)

    """Function for the Product Window"""
    def open_product_window(self):
        popup = Toplevel(self)
        popup.title("Product Management")
        popup.geometry("400x300")
        popup.configure(bg="white")
        popup.resizable(False, False)

        Label(popup, text="Product Management", bg="blue", fg="white", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=2, pady=10)

        Label(popup, text="Product Name:", bg="white").grid(row=1, column=0, sticky="E", padx=10)
        self.proName = Entry(popup, width=25)
        self.proName.grid(row=1, column=1, padx=10)

        Label(popup, text="Product ID:", bg="white").grid(row=2, column=0, sticky="E", padx=10)
        self.proID = Entry(popup, width=25)
        self.proID.grid(row=2, column=1, padx=10)

        Label(popup, text="Stock Type:", bg="white").grid(row=3, column=0, sticky="E", padx=10)
        self.proType = StringVar()
        self.proType.set("Select")
        OptionMenu(popup, self.proType, "In-Stock", "Out-of-Stock").grid(row=3, column=1, sticky="W", padx=10)

        Button(popup, text="Add Product", command=self.add_product).grid(row=4, column=0, pady=15)
        Button(popup, text="View Products", command=self.view_product_window).grid(row=4, column=1, pady=15)

    """Function to add Product"""
    def add_product(self):
        name = self.proName.get().strip()
        pro_id = self.proID.get().strip()
        pro_type = self.proType.get()

        if not name or not pro_id or pro_type == "Select":
            messagebox.showerror("Missing Info", "Please fill in all fields.")
            return

        self.products.append({
            "name": name,
            "id": pro_id,
            "type": pro_type,
        })

        messagebox.showinfo("Product Added", f"Product '{name}' (ID: {pro_id}) added successfully.")
        self.proName.delete(0, END)
        self.proID.delete(0, END)
        self.proType.set("Select")
    
    """Function to view the Product Window"""
    def view_product_window(self):
        if not self.products:
            messagebox.showinfo("No Products", "No product records yet.")
            return

        popup = Toplevel(self)
        popup.title("Product List")
        popup.geometry("400x300")
        Label(popup, text="Product Records", font=("Arial", 14, "bold")).pack(pady=10)

        for pro in self.products:
            Label(popup, text=f"{pro['name']} (ID: {pro['id']}) - {pro['type']}").pack(anchor="w", padx=20)

    """Function for the Supplier Window"""
    def open_supplier_window(self):
        popup = Toplevel(self)
        popup.title("Supplier Management")
        popup.geometry("400x200")
        popup.configure(bg="white")
        popup.resizable(False, False)

        Label(popup, text="Supplier Management", bg="blue", fg="white", font=("Arial", 16, "bold")).place(x=200, y=30, anchor="center")
        Button(popup, text="Exit", command=popup.destroy).place(x=200, y=150, anchor="center")


"""Launches the GUI"""
Inventory().mainloop()
