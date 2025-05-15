from flask import Flask
from models import *
from dotenv import load_dotenv
from config import Config
from db_config import db
from migrate_config import migrate
from marshmallow_config import ma
from flask_restful import Api
from xpi_config import api
from routes import register_all_routes


from controllers.home_controller import HomeController

# cargar las variables de entorno
load_dotenv()

# instanciar la clase flask y agregar las variables de configuracion
app=Flask(__name__)
app.config.from_object(Config)

# instanciar las extenciones
db.init_app(app)
with app.app_context():
    db.create_all()
ma.init_app(app)
# migrate.init_app(app,db)
# api.init_app(app)

api=Api(app)

# registrar las rutas
register_all_routes(api)


# correr el servidor
if __name__=="__main__":
    app.run(debug=True,port=5000)
