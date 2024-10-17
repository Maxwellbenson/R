from sqlalchemy.orm import sessionmaker
from Db_Connection import get_engine
from sqlalchemy import text

engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

try:

    insert_data_query = """
    INSERT INTO Feeding (Name, Weight, Food, FoodWeight) 
    VALUES (?, ?, ?, ?);
    """

    data_to_insert = [
        {'Python',  100.5,'Rats',  2.0},
        {'Boa Constrictor',  75.0, 'Mice', 1.5},
        {'Anaconda', 200.0, 'Fish',  5.0}
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
