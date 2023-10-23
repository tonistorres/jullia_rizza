from app import app 

@app.route("/")
def index():
    return f" 🤟 Hellow World"
