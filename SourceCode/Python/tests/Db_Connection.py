from sqlalchemy import create_engine

def get_engine():
    server = 'localHost'
    database = 'ReptileDatabase'  

    DATABASE_URL = 'mssql+pyodbc://localHost/ReptileDatabase?driver=ODBC+Driver+17+for+SQL+Server'

    
    engine = create_engine(DATABASE_URL)
    return engine