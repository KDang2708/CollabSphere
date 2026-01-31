from infrastructure.databases.factory_database import FactoryDatabase
# from infrastructure.databases.mssql import init_mssql
# from infrastructure.databases.postgres import init_postgres
from infrastructure.models import Du_An_Model, Giang_Vien_Model, Lop_Hoc_Hoc_Sinh, Lop_Hoc_Model, Moc_Quan_Trong_Model, Mon_Hoc_Model

def init_db(app):
    # init_mssql(app)
    FactoryDatabase.get_database('POSTGREE').init_database(app)
    # init_postgres(app)
    
# Migration Entities -> tables
from infrastructure.databases.mssql import Base