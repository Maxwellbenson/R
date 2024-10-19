from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db_Connection import get_engine
from Python.Tables.Snake_Main import Snake_main  

# Create an engine and session
engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

def insert_data():
    try:
        # Prepare the data to be inserted
        new_snake = {
            'SnakeName': 'Monty',
            'Sex': 'M',
            'Species': 'Python',
            'Weight': 1200.0,
            'Length': 100.5,
            'Traits': 'Albino',
            'Proven': 1,  # Use 1 for True
            'Origin': 'Born in captivity',
            'Purchased': 1,  # Use 1 for True
            'PurchasePrice': 200.0,
            'Disabilities': 0,  # Use 0 for False
            'Disability': ''
        }
        
        # Insert data into the table
        session.execute(snake_main.insert().values(new_snake))
        session.commit()  
        print("Data inserted successfully.")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()

if __name__ == '__main__':
    insert_data()
