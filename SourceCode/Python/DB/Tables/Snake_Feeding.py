from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from db_Connection import get_engine

Base = declarative_base()

class Feeding(Base):
    __tablename__ = 'Feeding_Main'  

    FeedId = Column(Integer, primary_key=True, autoincrement=True)
    SnakeId = Column(Integer, ForeignKey('Snake_Main.SnakeId'), nullable=False)  # Corrected ForeignKey
    Time = Column(DateTime)
    Food = Column(Float, nullable=False)
    FoodWeight = Column(Float)
    AddedSupplements = Column(Boolean)
    Supplements = Column(String(100))
    AttitudeTowardsFood = Column(String(100))
    NewFood = Column(Boolean)
    Count = Column(Integer)

def create_table():
    engine = get_engine()
    Base.metadata.create_all(engine)  # This will create the table only if it doesn't exist
    print("Table created successfully.")