from db_Connection import get_engine
from sqlalchemy import text

# Create the engine
engine = get_engine()

# Create a connection
with engine.connect() as conn:
    # Create the table if it does not exist
    create_table_query = """
    IF NOT EXISTS (
        SELECT * FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_NAME = 'Feeding'
    )
    BEGIN
        CREATE TABLE Feeding (
            Name VARCHAR(50) NOT NULL,         
            Weight FLOAT NOT NULL,              
            Food VARCHAR(50) NOT NULL,          
            FoodWeight FLOAT NOT NULL           
        );
    END
    """

    conn.execute(text(create_table_query))  # Use text() to execute raw SQL
    print("Table created successfully, or already exists.")

