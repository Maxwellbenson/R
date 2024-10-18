from sqlalchemy.orm import sessionmaker
from db_connection import get_engine
from sqlalchemy import text

engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

try:

    insert_data_query = """
    INSERT INTO Feeding (Name, Weight, Food, FoodWeight) 
    VALUES (:Name, :Weight, :Food, :FoodWeight)
    """

    data_to_insert = [
        {'Name':'Python', 'Weight': 100.5,'Food': 'Rats', 'FoodWeight': 2.0},
        {'Name':'Boa Constrictor', 'Weight': 75.0, 'Food': 'Mice', 'FoodWeight': 1.5},
        {'Name':'Anaconda', 'Weight': 200.0, 'Food': 'Fish', 'FoodWeight':  5.0}
    ]

    for data in data_to_insert:
        session.execute(text(insert_data_query), data)

    session.commit()  
    print("Data inserted successfully.")

except Exception as e:
    session.rollback()  
    print(f"An error occurred: {e}")
finally:
    session.close()  
