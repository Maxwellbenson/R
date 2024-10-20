import os
import sys
import tkinter as tk
from tkinter import messagebox
from sqlalchemy import insert
from db_Connection import get_engine  
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, inspect
from sqlalchemy.orm import declarative_base
from datetime import datetime  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DB.Tables.Snake_Feeding import Feed

engine = get_engine()

def insert_feed(feed_data):
    """Insert a new feed record into the database."""
    insert_stmt = insert(Feed).values(**feed_data)
    with engine.connect() as conn:
        conn.execute(insert_stmt)
        conn.commit()
    print("Data inserted successfully.")

def submit_data():
    """Handle the submission of data from the form.""" 
    new_feed = {
            'SnakeId': int(snake_id_entry.get()),
            'Time': datetime.now(),  
            'Food': food_entry.get(),
            'FoodWeight': food_weight_entry.get() if food_weight_entry.get() else None,
            'AddedSupplements': added_supplements_var.get(),
            'Supplements': supplements_entry.get(),
            'AttitudeTowardsFood': attitude_entry.get(),
            'NewFood': new_food_var.get(),
            'Count': int(count_entry.get()) if count_entry.get() else None
        }

    insert_feed(new_feed)
    messagebox.showinfo("Success", "Data inserted successfully.")


root = tk.Tk()
root.title("Feed Database Entry")

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
tk.Label(root, text="Time").grid(row=1, column=0)
time_entry = tk.Entry(root)
time_entry.insert(0, current_time)  
time_entry.grid(row=1, column=1)


tk.Label(root, text="Snake ID").grid(row=0, column=0)
snake_id_entry = tk.Entry(root)
snake_id_entry.grid(row=0, column=1)

tk.Label(root, text="Food").grid(row=2, column=0)
food_entry = tk.Entry(root)
food_entry.grid(row=2, column=1)

tk.Label(root, text="Food Weight(g)").grid(row=3, column=0)
food_weight_entry = tk.Entry(root)
food_weight_entry.grid(row=3, column=1)

tk.Label(root, text="Added Supplements").grid(row=4, column=0)
added_supplements_var = tk.BooleanVar()
added_supplements_checkbox = tk.Checkbutton(root, variable=added_supplements_var)
added_supplements_checkbox.grid(row=4, column=1)

tk.Label(root, text="Supplements").grid(row=5, column=0)
supplements_entry = tk.Entry(root)
supplements_entry.grid(row=5, column=1)

tk.Label(root, text="Attitude Towards Food").grid(row=6, column=0)
attitude_entry = tk.Entry(root)
attitude_entry.grid(row=6, column=1)

tk.Label(root, text="New Food").grid(row=7, column=0)
new_food_var = tk.BooleanVar()
new_food_checkbox = tk.Checkbutton(root, variable=new_food_var)
new_food_checkbox.grid(row=7, column=1)

tk.Label(root, text="Count").grid(row=8, column=0)
count_entry = tk.Entry(root)
count_entry.grid(row=8, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=9, columnspan=2)
root.mainloop()
