from infrastructure.databases.factory_database import FactoryDatabase
# from infrastructure.databases.postgres import init_postgres
# from infrastructure.databases.mssql import init_mssql
# from infrastructure.models import import_all_models
def init_db(app):
    # init_mssql(app)
    FactoryDatabase.get_database('POSTGRES').init_database(app)
    # init_postgres(app)
    
# Migration Entities -> tables
from infrastructure.databases.mssql import Base