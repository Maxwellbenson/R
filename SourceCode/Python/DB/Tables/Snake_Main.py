from sqlalchemy import Table, Column, Integer, String, Float, DateTime, ForeignKey, MetaData, BOOLEAN
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
    Column('Proven', BOOLEAN),
    Column('Origin', String(200)),
    Column('Purchased', BOOLEAN),
    Column('PurchasePrice', Float),
    Column('Disabilities', BOOLEAN),
    Column('Disability', String(100))
)

metadata.create_all(engine)

print("Table created successfully.")