import sys
import os

# Set up the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Print current sys.path for debugging
print("Current sys.path:", sys.path)

# Import the Snake class correctly
from DB.Tables.Snake_Main import Snake  # Adjusted import

from db_Connection import get_engine
from sqlalchemy import insert

engine = get_engine()
new_snake = {
    'SnakeName': 'Python',
    'Sex': 'M',
    'Species': 'Ball Python',
    'Weight': 1.2,
    'Length': 1.5,
    'Traits': 'Albino',
    'Proven': False,
    'Origin': 'Reptile Expo',
    'Purchased': True,
    'PurchasePrice': 300.0,
    'Disabilities': False,
    'Disability': None
}

insert_stmt = insert(Snake).values(**new_snake)
with engine.connect() as conn:
    conn.execute(insert_stmt)
    conn.commit()  

print("Data inserted successfully.")
