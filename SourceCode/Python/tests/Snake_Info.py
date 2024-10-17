from sqlalchemy.orm import sessionmaker
from db_connection import get_engine
from sqlalchemy import text


engine = get_engine()


Session = sessionmaker(bind=engine)
session = Session()

try:

    insert_data_query = """
    INSERT INTO Feeding (Name, Weight, Food, FoodWeight) 
    VALUES (:name, :weight, :food, :food_weight);
    """

    data_to_insert = [
        {'name': 'Python', 'weight': 100.5, 'food': 'Rats', 'food_weight': 2.0},
        {'name': 'Boa Constrictor', 'weight': 75.0, 'food': 'Mice', 'food_weight': 1.5},
        {'name': 'Anaconda', 'weight': 200.0, 'food': 'Fish', 'food_weight': 5.0}
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
