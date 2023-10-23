MENU_ISNTALL_ENVIRONMENT='
---------------------------------------------------
Create structure Foders of the Project
https://www.youtube.com/watch?v=0iHsyTkyoXo&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=3
---------------------------------------------------
'
TIME(){
echo "In 2s"
sleep 1
echo "In 1s"
sleep 1    
}

WRITE_FILES_INIT_APP(){

cat << EOF > __init__.py
'''
O __init__.py que está na pasta app é o principal, pois, ele 
está na camada mais externa os proximos estarão dentro de pastas
contidas dentro da pasta app, portanto (sub-pastas) que equivale 
dizer no mundo flask são módulos de alguma forma interligados ao 
módulo principal (main) '''

from flask import Flask

app = Flask(__name__)

from app.controllers import default


EOF
}



WRITE_DEFAULT_PY(){

cat << EOF > run.py
from app import app 



@app.route("/")
def index():
    return f" 🤟 Hellow World"


EOF


}



WRITE_FILES_RUN_PY(){

cat << EOF > run.py
from app import app


if __name__ =="__main__":
    app.run()

EOF


}


CREATE_FOLDERS(){
mkdir app
cd app
mkdir models
mkdir controllers
mkdir templates
mkdir static
touch __init__.py
WRITE_FILES_INIT_APP

cd models
touch __init__.py
cd ..
cd controllers
touch __init__.py
touch default.py
WRITE_DEFAULT_PY

cd ..
cd ..

run.py
WRITE_FILES_RUN_PY
bash run.py
}

CREATE_FOLDERS