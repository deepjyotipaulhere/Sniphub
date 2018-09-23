from flask import Flask,request,make_response,jsonify
import pymongo
import jwt
from functools import wraps
from flask_mail import Mail, Message


app=Flask(__name__)
app.config['SECRET_KEY']='SnIpHuB'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'daniel.ramirez302@gmail.com'
app.config['MAIL_PASSWORD'] = 'rabindranath'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def connection():
    client=pymongo.MongoClient('139.59.39.127',27017)
    db=client.sniphub
    return db


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
        
        if not token:
            return make_response("token required",500)

        try:
            data=jwt.decode(token,app.config['SECRET_KEY'])
            current_user={
                "name":data["name"],
                "email":data["email"]
            }
        except:
            return make_response("Invalid token",501)
        return f(current_user,*args,**kwargs)
    return decorated

@app.route("/login",methods=['POST'])
def login():
    try:
        x=request.get_json()
        db=connection()
        users=db.user_profile
        result=users.find_one({"email":x["email"]})
        print(result)
        user={
            "id":result["_id"],
            "name":result["name"],
            "email":result["email"]
        }
        token=jwt.encode(user,app.config['SECRET_KEY'])
        return jsonify({"auth":token})
    except:
        return make_response("Some error occurred",500)

@app.route("/register",methods=['POST'])
def register():
    try:
        x=request.get_json()
        user={
            "name":x["name"],
            "email":x["email"]
        }
        token=jwt.encode(user,app.config['SECRET_KEY'])

        msg = Message('Verify your profile - Sniphub', sender = 'Sniphub', recipients = [x["email"]])
        msg.html = "<a href='http://localhost:3000/done?key='"+token.decode('UTF-8')+">Verify</a>"
        mail.send(msg)
        return jsonify({"msg":"sent"})
    except:
        return jsonify({"msg":"error"})