from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, inspect
from sqlalchemy.orm import declarative_base
from db_Connection import get_engine  

Base = declarative_base()

class Feed(Base):
    __tablename__ = 'Feed_Main'
    
    FeedId = Column(Integer, primary_key=True, autoincrement=True)
    SnakeId = Column(Integer) 
    Time = Column(DateTime)
    Food = Column(String, nullable=False)
    FoodWeight = Column(Float)
    AddedSupplements = Column(Boolean)
    Supplements = Column(String(100))
    AttitudeTowardsFood = Column(String(100))
    NewFood = Column(Boolean)
    Count = Column(Integer)

engine = get_engine()

def table_exists(engine, table_name):
    inspector = inspect(engine)
    return table_name in inspector.get_table_names()

if __name__ == "__main__":
    if not table_exists(engine, Feed.__tablename__):
        Base.metadata.create_all(engine)
        print("Tables created successfully.")
    else:
        print("Table already exists.")
