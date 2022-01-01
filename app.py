from flask import Flask, request, render_template, redirect, session, url_for, flash
import mysql.connector
import numpy as np
import pickle
import os
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
app.secret_key=os.urandom(24)

model = pickle.load(open('ML Models/parkinsons.pkl', 'rb'))
model2=pickle.load(open("ML Models/heartPKL.pkl",'rb'))
model3 = pickle.load(open('ML Models/liver.pkl', 'rb'))
model4=pickle.load(open("ML Models/cancer.pkl",'rb'))
model5=pickle.load(open("ML Models/diabetes.pkl",'rb'))
model7=pickle.load(open("ML Models/kidneyPKL.pkl",'rb'))

conn=mysql.connector.connect(host="localhost",user="root",password="",database="0dUfVC8t7r")
cursor=conn.cursor()

@app.route('/')
def hello_world():
    return render_template("loginpage.html")

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/login_valid',methods=['POST'])
def login_valid():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        session['user_id']=users[0][0]
        return redirect('/home')
    else:
        return render_template('loginpage.html', info='invalid credentials')


@app.route('/add_user',methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    dob = request.form.get('dob')
    password = request.form.get('upassword')
    cursor.execute("""INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `dob`) VALUES (NULL, '{}', '{}', '{}', '{}')""".format(name,email,password,dob))
    conn.commit()
    return render_template('loginpage.html', info='user succesfully registered')


@app.route('/feedback',methods=['POST'])
def add_feedback():
    name = request.form.get('fname')
    email = request.form.get('femail')
    subject = request.form.get('sub')
    message = request.form.get('msg')
    cursor.execute("""INSERT INTO `feedback`(`user_id`, `name`, `email`, `subject`, `message`) VALUES (NULL,'{}','{}','{}','{}')""".format(name,email,subject,message))
    conn.commit()
    msg='Your message has been sent. Thank you!'
    return msg



database = {'shre': '123', 'raj': '456', 'rohit': '789'}


@app.route('/form_loginpage', methods=['POST', 'GET'])
def login():
    name1 = request.form['uname']
    pwd = request.form['pass']
    if name1 not in database:
        return render_template('loginpage.html', info='Invalid User')
    else:
        if database[name1] != pwd:
            return render_template('loginpage.html', info='Invalid Password')
        else:
            return render_template('home.html', name=name1)

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/page')
def page():
    return render_template("parkinson_s.html",length=0)

@app.route('/predict', methods=['POST'])
def predict():
 if request.method == 'POST':
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    output = model.predict(features_value)
    allcol = ["MDVP:Jitter(%) ", "MDVP:Jit ter(Abs) ", "MDVP:RAP ", "MDVP:PPQ ", "Jitter:DDP", "MDVP:Shimmer ",
              "MDVP:Shimmer(dB)",
              "MDVP:APQ", "NHR", "RPDE", "spread1", "spread2", "PPE"]
    cursor.execute("""SELECT * FROM `users` WHERE `user_id`={}""".format(session['user_id']))
    users = cursor.fetchall()

    if output == 1:
        return render_template("parkinson_s.html", predict_text='Parkinson’s Disease Detected',cor="red",pentered=input_features,length=len(input_features),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
    elif output == 0:
        return render_template("parkinson_s.html", predict_text='Parkinson’s Disease Not Detected',cor="green",pentered=input_features,length=len(input_features),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
    else:
        return render_template("parkinson_s.html", predict_text='Something went wrong')

@app.route('/heart')
def heart():
    return render_template('heart.html',length=0)

@app.route('/resultH', methods=['POST'])
def resultH():
    if request.method == 'POST':
        input_features2 = [float(x) for x in request.form.values()]

        features_value2 = np.array(input_features2)
        print(features_value2)
        output2 = model2.predict([features_value2])
        print(output2)
        allcol = ["cp ", "trestbps ", "chol ", "fbs ","restecg ","Thalach ","slope "]
        cursor.execute("""SELECT * FROM `users` WHERE `user_id`={}""".format(session['user_id']))
        users = cursor.fetchall()
        if output2 == 1:
            return render_template('heart.html', predict_text='Heart Disease Detected',cor="red",pentered=input_features2,length=len(input_features2),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        elif output2 == 0:
            return render_template('heart.html', predict_text='Heart Disease Not Detected',cor="green",pentered=input_features2,length=len(input_features2),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        else:
            return render_template('heart.html', predict_text='Something went wrong')




@app.route('/liver')
def liver():
    return render_template('liver.html',length=0)

@app.route('/resultL', methods=['POST'])
def resultL():
    if request.method == 'POST':
        input_features3 = [float(x) for x in request.form.values()]
        features_value3 = np.array(input_features3)
        print(features_value3)
        output3 = model3.predict([features_value3])
        print(output3)
        allcol = ["Total_Bilirubin", "Alamine_Aminotransferase", "Total_Protiens", "Albumin", "Albumin_and_Globulin_Ratio"]
        cursor.execute("""SELECT * FROM `users` WHERE `user_id`={}""".format(session['user_id']))
        users = cursor.fetchall()
        if output3 == 1:
            return render_template('liver.html', predict_text='liver Disease Detected',cor="red",pentered=input_features3,length=len(input_features3),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        elif output3 == 2:
            return render_template('liver.html', predict_text='liver Disease Not Detected',cor="green",pentered=input_features3,length=len(input_features3),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        else:
            return render_template('liver.html', predict_text='Something went wrong')

@app.route('/sugar')
def sugar():
    return render_template('sugar.html',length=0)

@app.route('/resultD', methods=['POST'])
def resultD():
    if request.method == 'POST':
        input_features5 = [float(x) for x in request.form.values()]
        print(input_features5)
        features_value5 = np.array(input_features5)
        print(features_value5)
        output5 = model5.predict([features_value5])
        print(output5)
        allcol = ["Glucose ", "BloodPressure", "Insulin", "BMI","DiabetesPedigreeFunction","Age"]
        cursor.execute("""SELECT * FROM `users` WHERE `user_id`={}""".format(session['user_id']))
        users = cursor.fetchall()
        if output5 == 1:
            return render_template('sugar.html', predict_text='Diabetes Detected',cor='red',pentered=input_features5,length=len(input_features5),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        elif output5 == 0:
            return render_template('sugar.html', predict_text='Diabetes Not Detected',cor='green',pentered=input_features5,length=len(input_features5),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        else:
            return render_template('suagr.html', predict_text='Something went wrong')

@app.route('/cancer')
def cancer():
    return render_template('cancer.html',length=0)

@app.route('/resultC', methods=['POST'])
def resultC():
    if request.method == 'POST':
        input_features4 = [float(x) for x in request.form.values()]
        features_value4 = np.array(input_features4)
        output4 = model4.predict([features_value4])
        print(output4)
        allcol = ["radius_mean ", "perimeter_mean ", "area_mean ", "concavity_mean ", "concave points_mean", "radius_se ", "perimeter_se",
                  "area_se", "radius_worst", "perimeter_worst", "area_worst", "concavity_worst","concave points_worst"]
        cursor.execute("""SELECT * FROM `users` WHERE `user_id`={}""".format(session['user_id']))
        users = cursor.fetchall()
        if output4 == 0:
            return render_template('cancer.html', predict_text='Benign Tumor Detected',cor="green",pentered=input_features4,length=len(input_features4),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        elif output4 == 1:
            return render_template('cancer.html', predict_text='Malignant Tumor Detected',cor="red",pentered=input_features4,length=len(input_features4),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        else:
            return render_template('cancer.html', predict_text='Something went wrong')



@app.route('/kidney')
def kidney():
    return render_template('kidney.html',length=0)


@app.route('/resultK', methods=['POST'])
def resultK():
    if request.method == 'POST':
        input_features5 = [float(x) for x in request.form.values()]
        features_value5 = np.array(input_features5)
        output5 = model7.predict([features_value5])
        print(output5)
        allcol=["Albumin", "Sugar", "Red Blood Cells", "Pus Cell", "Pus Cell Clumps", "Bacteria", "Blood Urea",
         "Serum Creatinine", "Hypertension", "Diabetes Mellitus", "Pedal Edema", "Anemia"]
        cursor.execute("""SELECT * FROM `users` WHERE `user_id`={}""".format(session['user_id']))
        users = cursor.fetchall()

        if output5 == 0:
            return render_template('kidney.html', predict_text='Chronic KIdney Disease Not Detected',cor="green",pentered=input_features5,length=len(input_features5),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        elif output5 == 1:
            return render_template('kidney.html', predict_text='Chronic KIdney Disease Detected',cor="red",pentered=input_features5,length=len(input_features5),kcol=allcol,email=users[0][2],name=users[0][1],dob=users[0][4])
        else:
            return render_template('kidney.html', predict_text='Something went wrong')




if __name__ == '__main__':
    app.run(debug=True)
