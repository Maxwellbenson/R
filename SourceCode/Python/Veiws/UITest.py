import os
import sys
import tkinter as tk
from tkinter import messagebox
from sqlalchemy import insert
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from db_Connection import get_engine  
from sqlalchemy import Column, Integer, String, Float, Boolean, inspect
from sqlalchemy.orm import declarative_base
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DB.Tables.Snake_Main import Snake


engine = get_engine()

def table_exists(engine, table_name):
    """Check if a table exists in the database."""
    inspector = inspect(engine)
    return table_name in inspector.get_table_names()

def insert_snake(snake_data):
    """Insert a new snake record into the database."""
    insert_stmt = insert(Snake).values(**snake_data)
    with engine.connect() as conn:
        conn.execute(insert_stmt)
        conn.commit()
    print("Data inserted successfully.")

def submit_data():
    """Handle the submission of data from the form."""
    new_snake = {
        'SnakeName': snake_name_entry.get(),
        'Sex': sex_entry.get(),
        'Species': species_entry.get(),
        'Weight': float(weight_entry.get()),
        'Length': float(length_entry.get()) if length_entry.get() else None,
        'Traits': traits_entry.get(),
        'Proven': proven_var.get(),
        'Origin': origin_entry.get(),
        'Purchased': purchased_var.get(),
        'PurchasePrice': float(purchase_price_entry.get()) if purchase_price_entry.get() else None,
        'Disabilities': disabilities_var.get(),
        'Disability': disability_entry.get()
    }
    
    # Insert the snake data into the database
    insert_snake(new_snake)
    messagebox.showinfo("Success", "Data inserted successfully.")

# Create the main application window
root = tk.Tk()
root.title("Snake Database Entry")

# Create form fields
tk.Label(root, text="Snake Name").grid(row=0, column=0)
snake_name_entry = tk.Entry(root)
snake_name_entry.grid(row=0, column=1)

tk.Label(root, text="Sex (M/F)").grid(row=1, column=0)
sex_entry = tk.Entry(root)
sex_entry.grid(row=1, column=1)

tk.Label(root, text="Species").grid(row=2, column=0)
species_entry = tk.Entry(root)
species_entry.grid(row=2, column=1)

tk.Label(root, text="Weight").grid(row=3, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=3, column=1)

tk.Label(root, text="Length").grid(row=4, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=4, column=1)

tk.Label(root, text="Traits").grid(row=5, column=0)
traits_entry = tk.Entry(root)
traits_entry.grid(row=5, column=1)

tk.Label(root, text="Proven").grid(row=6, column=0)
proven_var = tk.BooleanVar()
proven_checkbox = tk.Checkbutton(root, variable=proven_var)
proven_checkbox.grid(row=6, column=1)

tk.Label(root, text="Origin").grid(row=7, column=0)
origin_entry = tk.Entry(root)
origin_entry.grid(row=7, column=1)

tk.Label(root, text="Purchased").grid(row=8, column=0)
purchased_var = tk.BooleanVar()
purchased_checkbox = tk.Checkbutton(root, variable=purchased_var)
purchased_checkbox.grid(row=8, column=1)

tk.Label(root, text="Purchase Price").grid(row=9, column=0)
purchase_price_entry = tk.Entry(root)
purchase_price_entry.grid(row=9, column=1)

tk.Label(root, text="Disabilities").grid(row=10, column=0)
disabilities_var = tk.BooleanVar()
disabilities_checkbox = tk.Checkbutton(root, variable=disabilities_var)
disabilities_checkbox.grid(row=10, column=1)

tk.Label(root, text="Disability").grid(row=11, column=0)
disability_entry = tk.Entry(root)
disability_entry.grid(row=11, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=12, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
