from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("test.html")

# @app.route("/update",methods=["POST"])
# def index():
    # name = request.values["name"]
    # sex = request.values["sex"]
    # num = request.values["n"]
    # return {"name":name+" is robot","sex":sex+" is a boy","n":int(num)+5}

if __name__=="__main__":
    app.run(debug=True)