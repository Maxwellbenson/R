from sqlalchemy import Table, Column, Integer, String, Float, DateTime, ForeignKey, MetaData, Boolean
from db_Connection import get_engine

engine = get_engine()
metadata = MetaData()

snake_main = Table(
    'Snake_Main', metadata,
    Column('SnakeId', Integer, primary_key=True),  
    Column('SnakeName', String(50), nullable=False),
    Column('Sex', String(1), nullable=False),
    Column('Species', String(50), nullable=False),
    Column('Weight', Float, nullable=False),
    Column('Length', Float),
    Column('Traits', String(60)),
    Column('Proven', Integer),  # Change BOOLEAN to Integer or use Boolean if your dialect translates it to BIT
    Column('Origin', String(200)),
    Column('Purchased', Integer),  # Change BOOLEAN to Integer or use Boolean
    Column('PurchasePrice', Float),
    Column('Disabilities', Integer),  # Change BOOLEAN to Integer or use Boolean
    Column('Disability', String(100))
)

# Create the table in the database
metadata.create_all(engine)

print("Table created successfully.")
