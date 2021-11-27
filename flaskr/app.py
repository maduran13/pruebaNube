#from flaskr import create_app
from vistas.vistas import RecursoDescargar, RecursoLogin, RecursoTarea, RecursoTareas, RecursoUsuario
from models.modelos import db, Usuario
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:12345678@first-database-01.cnycdfoyjqmp.us-east-1.rds.amazonaws.com:3306/first-database-01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'k#4ASfdfjo4343@$.-'
app.config['UPLOAD_FOLDER'] = './originales'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['BROKER_TRANSPORT'] = 'sqs'
app.config['BROKER_TRANSPORT_OPTIONS'] = { 'region': 'us-east-1'}
app.config['BROKER_USER'] = 'ASIAQEO3TSAJ5Q3Q4FNI'
app.config['BROKER_PASSWORD'] = 'WmcfdMXZqjgaVadwWnIMoHiQDR44S3G5GgJqA2ey'

app_context = app.app_context()
app_context.push()


db.init_app(app)
api = Api(app)
jwt = JWTManager(app)

api.add_resource(RecursoUsuario, '/api/auth/signup')
api.add_resource(RecursoLogin, '/api/auth/login')
api.add_resource(RecursoTareas, '/api/tasks')
api.add_resource(RecursoTarea, '/api/tasks/<int:id_conversion>')
api.add_resource(RecursoDescargar, '/api/files/<string:name>')
#testing
with app.app_context():
    u = Usuario(username='cris', password='p', email='q@q.com')
    print(Usuario.query.all())


