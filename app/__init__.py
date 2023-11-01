
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

'''Configuração padrão da documentação do flask_SQLAlchemy'''

# mysql://username:password@host:port/database_name
# URI que aponta o ORM para o banco de dados a ser trabalhado
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1020@localhost:3306/dbtwitterjulia'
# aqui o ORM recebe nosso app por meio de parâmetro 
db=SQLAlchemy(app)


from app.controllers import default


