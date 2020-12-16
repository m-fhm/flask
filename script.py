from flask import Flask,render_template,url_for
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/sample')
def sample():  
    return render_template("sample.html")
@app.route('/home')
def home():
    return render_template('home.html')
if __name__=="__main__":
    app.run(debug=True)