import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.tree import DecisionTreeClassifier
import pickle

data=pd.read_csv("diabetes.csv")

data.drop(data[data["SkinThickness"]==0].index,inplace=True)
data.drop(data[data.BloodPressure==0].index,inplace=True)
data.drop(data[data.Glucose==0].index,inplace=True)
data.drop(data[data["Insulin"]==0].index,inplace=True)


X_train,X_test,Y_train,Y_test = tts(data.drop(["Age","Outcome"],axis="columns"),data[["Outcome"]],test_size=30)

cs3=DecisionTreeClassifier()

cs3.fit(X_train,Y_train)

score=cs3.score(X_test,Y_test)*100

w=open("model","wb")
pickle.dump(cs3,w)