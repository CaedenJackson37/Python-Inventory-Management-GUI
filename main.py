"""

Author:  Caeden Jackson
Date written: 04/15/25
Assignment:   Module8 exercise1 part1 (1 or 2), etc.
Short Desc:   This program is my final project of developing a working GUI Breezy application.
This application is a GUI for a restaurant inventory management system.

"""
import time

import pandas as pd

from tkinter import *
from tkinter import messagebox

from breezypythongui import EasyFrame


class Inventory(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Inventory Management System", width=800, height=600)

        """Lists for Employees, Products, and Suppliers"""
        self.employees = []
        self.products = []
        self.supplier = []

        """Images for Home, Employees, Products, and Suppliers"""
        self.title_image = PhotoImage(file="title.png")
        self.employee_image = PhotoImage(file="employee.png")
        self.product_image = PhotoImage(file="product.png")
        self.supplier_image = PhotoImage(file="supplier.png")

        """Title Label"""
        Label(self, text="Inventory Management", image=self.title_image, compound="left",
              font=("Arial", 20), bg="beige", fg="navajowhite3").grid(row=0, column=0, columnspan=3, sticky="EW", padx=10, pady=0)

        """Time Label"""
        self.timeLabel = self.addLabel(text="", row=1, column=0, columnspan=3, sticky="EW")
        self.timeLabel["font"] = ("Arial", 20)
        self.timeLabel["bg"] = "light goldenrod"
        self.timeLabel["fg"] = "white"
        self.timeLabel["anchor"] = "center"


        """Buttons for Employees, Products, and Suppliers"""
        self.emp_btn = self.addButton(text="Employee", row=3, column=0,command=self.open_employee_window)
        self.emp_btn.config(image=self.employee_image, compound="left")
        self.emp_btn.grid(row=2, column=0, sticky="W", padx=10, pady=10)

        self.prod_btn = self.addButton(text="Product", row=3, column=1, command=self.open_product_window)
        self.prod_btn.config(image=self.product_image, compound="left")
        self.prod_btn.grid(row=3, column=0, sticky="W", padx=10, pady=10)

        self.supp_btn = self.addButton(text="Supplier", row=3, column=2, command=self.open_supplier_window)
        self.supp_btn.config(image=self.supplier_image, compound="left")
        self.supp_btn.grid(row=4, column=0, sticky="W", padx=10, pady=10)

        """Calls the time function to allow it to show up"""
        self.update_time()

    """Function to show the current time"""
    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.timeLabel["text"] = current_time
        self.after(1000, self.update_time)

    """Function for Employee Window"""
    def open_employee_window(self):
        popup = Toplevel(self)
        popup.title("Employee Management")
        popup.geometry("400x300")
        popup.configure(bg="white")
        popup.resizable(False, False)

        Label(popup, text="Employee Management", bg="beige", fg="navajowhite3", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="EW", pady=10)

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

        Button(popup, text="Save to Excel", command=self.employee_excel).grid(row=5, column=0, padx=10)
        Button(popup, text="Add Employee", command=self.add_employee).grid(row=5, column=1, pady=15)
        Button(popup, text="View Employees", command=self.view_employees_window).grid(row=5, column=2, pady=15)


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

    """Function to Save to Excel"""
    def employee_excel(self):
        employee_df = pd.DataFrame(self.employees)
        excel_file_path = 'output.xlsx'
        employee_df.to_excel(excel_file_path, index=False)
        print(f"DataFrame successfully saved to {excel_file_path}")

    """Function for the Product Window"""
    def open_product_window(self):
        popup = Toplevel(self)
        popup.title("Product Management")
        popup.geometry("400x300")
        popup.configure(bg="white")
        popup.resizable(False, False)

        Label(popup, text="Product Management", bg="beige", fg="navajowhite3", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=2, sticky= "EW", pady=10)

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

        Button(popup, text="Save to Excel", command=self.product_excel).grid(row=4, column=0, padx=10)
        Button(popup, text="Add Product", command=self.add_product).grid(row=4, column=1, pady=15)
        Button(popup, text="View Products", command=self.view_product_window).grid(row=4, column=2, pady=15)

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

    """Function to Save to Excel"""
    def product_excel(self):
        product_df = pd.DataFrame(self.products)
        excel_file_path = 'output.xlsx'
        product_df.to_excel(excel_file_path, index=False)
        print(f"DataFrame successfully saved to {excel_file_path}")

    """Function for the Supplier Window"""
    def open_supplier_window(self):
        popup = Toplevel(self)
        popup.title("Supplier Management")
        popup.geometry("500x200")
        popup.configure(bg="white")
        popup.resizable(False, False)

        Label(popup, text="Supplier Management", bg="beige", fg="navajowhite3", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2,sticky="EW",pady=10)

        Label(popup, text="Supplier Name:", bg="white").grid(row=1, column=0, sticky="E", padx=10)
        self.supName = Entry(popup, width=25)
        self.supName.grid(row=1, column=1, padx=10)

        Label(popup, text="Supplier ID:", bg="white").grid(row=2, column=0, sticky="E", padx=10)
        self.supID = Entry(popup, width=25)
        self.supID.grid(row=2, column=1, padx=10)

        Label(popup, text="Hire Date (YYYY-MM-DD):", bg="white").grid(row=4, column=0, sticky="E", padx=10)
        self.hireDate = Entry(popup, width=25)
        self.hireDate.grid(row=4, column=1, padx=10)

        Button(popup, text="Save to Excel", command=self.supplier_excel).grid(row=5, column=0, padx=10)
        Button(popup, text="Add Supplier", command=self.add_supplier).grid(row=5, column=1, pady=15)
        Button(popup, text="View Supplier", command=self.view_supplier_window).grid(row=5, column=2, pady=15)

    """Function to add Supplier"""
    def add_supplier(self):
        name = self.supName.get().strip()
        sup_id = self.supID.get().strip()
        hire_date = self.hireDate.get()

        if not name or not sup_id or not hire_date:
            messagebox.showerror("Missing Info", "Please fill in all fields.")
            return

        self.supplier.append({
            "name": name,
            "id": sup_id,
            "hire_date": hire_date
        })

        messagebox.showinfo("Supplier Added", f"Supplier '{name}' (ID: {sup_id}) added successfully.")
        self.supName.delete(0, END)
        self.supID.delete(0, END)
        self.hireDate.delete(0, END)

    def view_supplier_window(self):
        if not self.supplier:
            messagebox.showinfo("No Supplier", "No supplier records yet.")
            return

        popup = Toplevel(self)
        popup.title("Supplier List")
        popup.geometry("400x300")
        Label(popup, text="Supplier Records", font=("Arial", 14, "bold")).pack(pady=10)

        for sup in self.supplier:
            Label(popup, text=f"{sup['name']} (ID: {sup['id']}) - {sup['hire_date']}").pack(anchor="w", padx=20)

    """Function to Save to Excel"""
    def supplier_excel(self):
        supplier_df = pd.DataFrame(self.supplier)
        excel_file_path = 'output.xlsx'
        supplier_df.to_excel(excel_file_path, index=False)
        print(f"DataFrame successfully saved to {excel_file_path}")

"""Launches the GUI"""
Inventory().mainloop()
