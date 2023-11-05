
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
from app.controllers.default import index 

app = Flask(__name__)

'''Configuração padrão da documentação do flask_SQLAlchemy'''

# mysql://username:password@host:port/database_name
# URI que aponta o ORM para o banco de dados a ser trabalhado
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1020@localhost:3306/dbtwitterjulia'
# aqui o ORM recebe nosso app por meio de parâmetro 
# db=SQLAlchemy(app)


#Quero instânciar o Migrate e o Migrate irá cuidar das minhas migrações.
# Ele recebe como parâmetro meu app e meu banco de dados 
# migrate=Migrate(app=app, db=db)

# O Manager irá cuidar dos comandos que executar na inicialização da minha aplicação 

# manager=Manager(app=app)
# @manager.command

# def hello():
#     print ("hello")
