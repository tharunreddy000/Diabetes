import pickle
from flask import *

o=open("model","rb")
cls=pickle.load(o)

app=Flask(__name__,template_folder="templates")

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
       data={}
       data["got"]=True
       pr=request.form["Pregnancies"]
       gl=float(request.form["Glucose"])
       bp=float(request.form["bp"])
       st=float(request.form["SkinThickness"])
       dpf = float(request.form["DiabetesPedigreeFunction"])
       bmi = float(request.form["BMI"])
       ins= float(request.form["Insulin"])
       d=[pr,gl,bp,st,ins,bmi,dpf]
       out=cls.predict([d])
       data["output"]=out[0]
       return  render_template("index.html",data=data)
    else:
        data = {}
        data["got"] = False
        return render_template("index.html",data=data)


if __name__ == '__main__':
    app.run()

