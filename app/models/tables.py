'''
Referência para pesquisas futuras:
https://www.youtube.com/watch?v=R3nS66dgo2w&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=4
'''

from app import db


class User(db.Model):
    
    # no banco de dados o nome da nossa tabela será users
    __tablename__='users'
    
    # id é uma coluna e recebe de db.Model um tipo Inteiro e uma chave primária
    id=db.Column(db.Integer, primary_key=True)
    # username é uma coluna e recebe de db.Model um tipo String e chave unica 
    # não podendo haver repetição
    password=db.Column(db.String(8))
    username=db.Column(db.String(120),unique=True )
    name=db.Column(db.String(100))
    email=db.Column(db.Sting, unique=True)
    
    #Construtor da Classe:
    '''
    *   Para se criar um usuário no banco de dados será necessário 
        Ele ter os parâmetros abaixo explicitado conforme descrito 
        no método construtor __init__:
        - username;
        - password;
        - name;
        - email.  
    '''
    
    def __init__(self, username, password,name, email):
        self.username=username
        self.password=password
        self.name=name
        self.email=email
        
    def __repr__(self):
       return "<User %f>" % self.username     
   
class Post(db.Model):
        __tablename__='posts'
       
        id=db.Column(db.Integer, primary_key=True)
        content=db.Column(db.Text)
       # o campo user_id recebe uma coluna que será uma chave estrangeira que fará
       # referência e relacionamento com o campo [id da tabela users]
        user_id=db.Column(db.Integer, db.Foreignkey('users_id'))
        
        # evita ter que fazer join para saber que é o usário 
        # quando fizer uma pesquisa na tabela Post       
        user = db.relationship('User', foreign_keys=user_id)
        
         #Construtor da Classe:
        '''
        *   Para se criar um post no banco de dados será necessário 
            Ele ter os parâmetros abaixo explicitado conforme descrito 
            no método construtor __init__:
            - content;
            - user_id.
        '''
       
        def __init__(self, content, user_id):
            self.conten=content
            self.user_id=user_id
            
        def __repr__(self):
            return "<Post %r>" % self.id    

class Follow(db.Model): 
    __tablename__="follow"
    
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.Foreignkey('users_id'))
    follower_id = db.Column(db.Integer,db.Foreignkey('users_id'))
    
    
    # evita ter que fazer join para saber que é o usário 
    # quando fizer uma pesquisa na tabela Follow       
    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)       