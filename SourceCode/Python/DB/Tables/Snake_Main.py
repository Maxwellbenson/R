from sqlalchemy import Column, Integer, String, Float, Boolean, insert, inspect
import sys
import os
from sqlalchemy.orm import declarative_base
from db_Connection import get_engine  
Base = declarative_base()

class Snake(Base):
    __tablename__ = 'Snake_Main' 
    
    SnakeId = Column(Integer, primary_key=True, autoincrement=True)
    SnakeName = Column(String(50), nullable=False)
    Sex = Column(String(1), nullable=False)
    Species = Column(String(50), nullable=False)
    Weight = Column(Float, nullable=False)
    Length = Column(Float)
    Traits = Column(String(60))
    Proven = Column(Boolean)
    Origin = Column(String(200))
    Purchased = Column(Boolean)
    PurchasePrice = Column(Float)
    Disabilities = Column(Boolean)
    Disability = Column(String(100))

engine = get_engine()

def table_exists(engine, table_name):
    """Check if a table exists in the database."""
    inspector = inspect(engine)
    return table_name in inspector.get_table_names()

if __name__ == "__main__":
    if not table_exists(engine, Snake.__tablename__):
        Base.metadata.create_all(engine)
        print("Tables created successfully.")
    else:
        print("Table already exists")
