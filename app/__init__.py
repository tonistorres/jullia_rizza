
from flask import Flask


app = Flask(__name__)

# importando o módulo controllers para o módulo  
# principal de execução
from app.controllers import default