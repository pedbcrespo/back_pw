from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import dados_bd as dbd


conn = "mysql+pymysql://{}:{}@{}/{}".format(dbd.usuario, dbd.senha, dbd.host, dbd.bancoDados)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['UPLOAD_FOLDER'] = '/imgs'
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
api = Api(app)
CORS(app)

cors = CORS(app, resources={
    r"/*":{
        "origins":"*"
    }
})
