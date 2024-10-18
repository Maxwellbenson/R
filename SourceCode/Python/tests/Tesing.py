from sqlalchemy import create_engine

def get_engine():
    
    return create_engine('mssql+pyodbc://username:password@server/database')
