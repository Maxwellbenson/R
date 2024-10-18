from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db_connection import get_engine

data_to_insert = [
    {
        'snake_name': 'James', 
        'sex': 'M', 
        'species': 'Ball Python', 
        'weight': 1200.0, 
        'length': 95.0, 
        'traits': 'Albino', 
        'proven': 0, 
        'birthdate': '2023-01-01', 
        'origin': 'Born in captivity', 
        'purchased': 0, 
        'purchase_price': 0.00, 
        'disabilities': 0, 
        'disability': ''
    },
    {
        'snake_name': 'Stacy', 
        'sex': 'F', 
        'species': 'Corn Snake', 
        'weight': 800.0, 
        'length': 85.0, 
        'traits': 'Albino', 
        'proven': 1, 
        'birthdate': '2020-06-10', 
        'origin': 'Purchased at pet store', 
        'purchased': 1, 
        'purchase_price': 200.0, 
        'disabilities': 0, 
        'disability': ''
    }
]

insert_query = """
INSERT INTO Snake_Main (SnakeName, Sex, Species, Weight, Length, Traits, Proven, BirthDate, Origin, Purchased, PurchasePrice, Disabilities, Disability) 
VALUES (:snake_name, :sex, :species, :weight, :length, :traits, :proven, :birthdate, :origin, :purchased, :purchase_price, :disabilities, :disability)
"""

def insert_data():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        with engine.connect() as connection:
            for data in data_to_insert:
                connection.execute(text(insert_query), **data)
        
        session.commit()  
        print("Data inserted successfully.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    insert_data()
