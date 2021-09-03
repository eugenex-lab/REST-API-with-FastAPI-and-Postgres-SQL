#PLease feel free to use the code and make comments
#  Date: 2021.08.03
#  Author: eugenex
import os
import urllib
import databases
import sqlalchemy

#DATABASE_URL = "sqlite:///./test.db"

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'eugenex')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'sankore123')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

wealthng = sqlalchemy.Table(
    "wealthng",
    metadata,
    sqlalchemy.Column("product_id", sqlalchemy.Integer, primary_key=True, autoincrement=True,index=True),
    sqlalchemy.Column("product_name", sqlalchemy.String,unique=True,index=True),
    sqlalchemy.Column("minimum_investment", sqlalchemy.Integer, index=True),
    sqlalchemy.Column("product_tenor", sqlalchemy.String,index=True),
    sqlalchemy.Column("investment_return", sqlalchemy.Integer, index=True),
    sqlalchemy.Column("activate_rollover", sqlalchemy.Boolean,index=True),
)

engine = sqlalchemy.create_engine(
    #DATABASE_URL, connect_args={"check_same_thread": False}
    DATABASE_URL, pool_size=5, max_overflow=0
)
metadata.create_all(engine)



