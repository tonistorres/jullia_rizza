
WRITE_FILES_INIT_APP(){

cat << EOF > __init__.py

from flask import Flask

app = Flask(__name__)

from app.controllers import default


EOF
}



WRITE_DEFAULT_PY(){

cat << EOF > default.py
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

cd .. # saindo de controllers
cd .. # saindo de app



touch run.py
WRITE_FILES_RUN_PY


python3 run.py
}

CREATE_FOLDERS