from app import db


class User(db.Model):
    
    # no banco de dados o nome da nossa tabela será users
    __tablename__='users'
    
    # id é uma coluna e recebe de db.Model um tipo Inteiro e uma chave primária
    id=db.Column(db.Integer, primary_key=True)
    # username é uma coluna e recebe de db.Model um tipo String e chave unica 
    # não podendo haver repetição
    username=db.Column(db.String(120),unique=True )