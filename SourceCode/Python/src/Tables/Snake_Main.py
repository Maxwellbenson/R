from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime,Boolean
from sqlalchemy.orm import sessionmaker

# Database connection string
DATABASE_URL = 'mssql+pyodbc://localHost/ReptileDatabase?driver=ODBC+Driver+17+for+SQL+Server'
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
    BirthDate = Column(DateTime)
    Origin = Column(String(200))
    Purchased = Column(Boolean)
    PurchasePrice = Column(Float)
    Disabilities = Column(Boolean)
    Disability = Column(String(100))

# Function to create the table
def create_table():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Table created successfully.")

if __name__ == '__main__':
    create_table()
