from sqlalchemy import create_engine

def get_engine():
    DATABASE_URL = 'mssql+pyodbc://localhost/ReptileDatabase?driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(DATABASE_URL)
    return engine