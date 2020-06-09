from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import database

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


# Create empty window
window = Tk()
window.title("Dealership Application")

def print_thing():
    print(car_insert_make.get() + ' ' + car_insert_model.get())
    
def submit_car():
    database.insert_car(car_insert_make.get(), car_insert_model.get(), car_insert_year.get(), car_insert_fuel.get(), car_insert_list_price.get(), car_insert_miles.get(), car_insert_category.get())

def edit_car():
    database.edit_car(car_edit_value, car_edit_new_condition, car_edit_cid)

def delete_car():
    database.delete_car(car_delete_value)

def submit_employee():
    database.insert_employee(employee_insert_essn, employee_insert_name, employee_insert_salary)

def edit_employee():
    database.edit_employee(employee_edit_value, employee_edit_new_condition, employee_edit_essn)

def delete_employee():
    database.delete_employee(employee_delete_essn)

def submit_sale():
    database.new_sale(sale_bssn, sale_insurance, sale_name, sale_price, sale_purchase_date, sale_payment_type, sale_payment, sale_cid, sale_essn, sale_commission)

# # Add text widget
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 0)
t1.insert(END, 'INSERT CAR:')
t1.config(state='disabled')

# Add execute button widget
submit_car_button = Button(window, text="Submit car", command = submit_car)
submit_car_button.grid(row = 1, column = 0)

# Add make text entry widget for insert operation
car_insert_make = EntryWithPlaceholder(window, placeholder='make')
car_insert_make.grid(row = 1, column = 1)

# Add model text entry widget for insert operation
car_insert_model = EntryWithPlaceholder(window, placeholder='model')
car_insert_model.grid(row = 1, column = 2)

# Add year text entry widget for insert operation
car_insert_year = EntryWithPlaceholder(window, placeholder='year')
car_insert_year.grid(row = 1, column = 3)

# Add fuel type text entry widget for insert operation
car_insert_fuel = EntryWithPlaceholder(window, placeholder='fuel')
car_insert_fuel.grid(row = 1, column = 4)

# Add list price type text entry widget for insert operation
car_insert_list_price = EntryWithPlaceholder(window, placeholder='list price')
car_insert_list_price.grid(row = 1, column = 5)

# Add miles price type text entry widget for insert operation
car_insert_miles = EntryWithPlaceholder(window, placeholder='miles')
car_insert_miles.grid(row = 1, column = 6)

# Add category price type text entry widget for insert operation
car_insert_category = EntryWithPlaceholder(window, placeholder='category')
car_insert_category.grid(row = 1, column = 7)

# # Add text widget to edit car
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 2, column = 0)
t1.insert(END, 'EDIT CAR:')
t1.config(state='disabled')

# Add execute button widget
edit_car_button = Button(window, text="Edit car", command = edit_car)
edit_car_button.grid(row = 3, column = 0)

# Add value type text entry widget for edit operation
car_edit_value = EntryWithPlaceholder(window, placeholder='value')
car_edit_value.grid(row = 3, column = 1)

# Add new condition type text entry widget for edit operation
car_edit_new_condition = EntryWithPlaceholder(window, placeholder='new condition')
car_edit_new_condition.grid(row = 3, column = 2)

# Add cid type text entry widget for edit operation
car_edit_cid = EntryWithPlaceholder(window, placeholder='cid')
car_edit_cid.grid(row = 3, column = 3)

# # Add text widget to delete car
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 2, column = 4)
t1.insert(END, 'DELETE CAR:')
t1.config(state='disabled')

# Add execute button widget
delete_car_button = Button(window, text="Delete car", command = delete_car)
delete_car_button.grid(row = 3, column = 4)

# Add value type text entry widget for delete operation
car_delete_value = EntryWithPlaceholder(window, placeholder='cid')
car_delete_value.grid(row = 3, column = 5)

# separator
ttk.Separator(window, orient=HORIZONTAL).grid(row=4, columnspan = 100, sticky = "ew")

# # Add text widget to insert employee
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 5, column = 0)
t1.insert(END, 'INSERT EMPLOYEE:')
t1.config(state='disabled')

# Add execute button widget
submit_employee_button = Button(window, text="Submit Employee", command = submit_employee)
submit_employee_button.grid(row = 6, column = 0)

# Add essn type text entry widget for insert operation
employee_insert_essn = EntryWithPlaceholder(window, placeholder='essn')
employee_insert_essn.grid(row = 6, column = 1)

# Add name type text entry widget for insert operation
employee_insert_name = EntryWithPlaceholder(window, placeholder='name')
employee_insert_name.grid(row = 6, column = 2)

# Add salary type text entry widget for insert operation
employee_insert_salary = EntryWithPlaceholder(window, placeholder='salary')
employee_insert_salary.grid(row = 6, column = 3)

# # Add text widget to edit employee
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 7, column = 0)
t1.insert(END, 'EDIT EMPLOYEE:')
t1.config(state='disabled')

# # Add text widget to delete employee
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 7, column = 4)
t1.insert(END, 'DELETE EMPLOYEE:')
t1.config(state='disabled')

# Add salary type text entry widget for insert operation
employee_edit_salary = EntryWithPlaceholder(window, placeholder='salary')
employee_edit_salary.grid(row = 6, column = 3)

# Add execute button widget
edit_employee_button = Button(window, text="Edit Employee", command = print_thing)
edit_employee_button.grid(row = 8, column = 0)

# Add value type text entry widget for edit operation
employee_edit_value = EntryWithPlaceholder(window, placeholder='value')
employee_edit_value.grid(row = 8, column = 1)

# Add new condition type text entry widget for edit operation
employee_edit_new_condition = EntryWithPlaceholder(window, placeholder='new condition')
employee_edit_new_condition.grid(row = 8, column = 2)

# Add essn type text entry widget for edit operation
employee_edit_essn = EntryWithPlaceholder(window, placeholder='essn')
employee_edit_essn.grid(row = 8, column = 3)

# Add execute button widget
delete_employee_button = Button(window, text="Delete Employee", command = print_thing)
delete_employee_button.grid(row = 8, column = 4)

# Add essn type text entry widget for delete operation
employee_delete_essn = EntryWithPlaceholder(window, placeholder='essn')
employee_delete_essn.grid(row = 8, column = 5)

# separator
ttk.Separator(window, orient=HORIZONTAL).grid(row=9, columnspan = 100, sticky = "ew")

# # Add text widget to delete employee
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 10, column = 0)
t1.insert(END, 'NEW SALE:')
t1.config(state='disabled')

# Add execute button widget
submit_sale_button = Button(window, text="Submit Sale", command = print_thing)
submit_sale_button.grid(row = 11, column = 0)

# sale operation
sale_bssn = EntryWithPlaceholder(window, placeholder='bssn')
sale_bssn.grid(row = 11, column = 1)

# sale operation
sale_insurance = EntryWithPlaceholder(window, placeholder='insurance')
sale_insurance.grid(row = 11, column = 2)

# sale operation
sale_name = EntryWithPlaceholder(window, placeholder='name')
sale_name.grid(row = 11, column = 3)

# sale operation
sale_price = EntryWithPlaceholder(window, placeholder='price')
sale_price.grid(row = 11, column = 4)

# sale operation
sale_purchase_date = EntryWithPlaceholder(window, placeholder='date (yyyy-mm-dd)')
sale_purchase_date.grid(row = 11, column = 5)

# sale operation
sale_payment_type = EntryWithPlaceholder(window, placeholder='payment type')
sale_payment_type.grid(row = 11, column = 6)

# sale operation
sale_payment = EntryWithPlaceholder(window, placeholder='payment')
sale_payment.grid(row = 11, column = 7)

# sale operation
sale_cid = EntryWithPlaceholder(window, placeholder='cid')
sale_cid.grid(row = 12, column = 1)

# sale operation
sale_essn = EntryWithPlaceholder(window, placeholder='essn')
sale_essn.grid(row = 12, column = 2)

# sale operation
sale_commission = EntryWithPlaceholder(window, placeholder='commission')
sale_commission.grid(row = 12, column = 3)

window.mainloop()