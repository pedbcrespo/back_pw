from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import dados_bd as dbd


conn = "mysql+pymysql://{}:{}@{}/{}".format(dbd.usuario, dbd.senha, dbd.host, dbd.bancoDados)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
mail = Mail()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['UPLOAD_FOLDER'] = '/imgs'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'projprogweb@gmail.com'
app.config['MAIL_PASSWORD'] = dbd.senha_gmail
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)

db = SQLAlchemy(app)
api = Api(app)
CORS(app)

cors = CORS(app, resources={
    r"/*":{
        "origins":"*"
    }
})
