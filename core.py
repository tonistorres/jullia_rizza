from datetime import datetime
from sqlalchemy import (
    create_engine, MetaData, Column, Table, Integer, String, DateTime
)

engine =create_engine('sqlite:///teste.db', echo=False)
# engine=create_engine('mysql://root:1020@localhost:3306/dbtwitterjulia',echo=True)
# engine = create_engine("mysql+pymysql://root:1020@localhost/dbtwitterjulia?charset=utf8mb4")

# engine = create_engine("mysql+pymysql://root:1020@localhost/dbtwitterjulia",
#                             pool_recycle=3306, echo=True)

metadata = MetaData(engine)

user_table=Table('user', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('username',String(40), index=True), # coloquei o index pois a possibilidade de muitas consultas está nesse campo
                 Column('password',String(8), nullable=False), # coluna do password não pode ser vazia
                 Column('name',String(60)),
                 Column('email', String(100)),
                 Column('created',DateTime, default=datetime.now),
                 Column('updated',DateTime, default=datetime.now, onupdate=datetime.now)
                
                
                 )

metadata.create_all()


