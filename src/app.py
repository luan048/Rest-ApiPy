from flask import Flask

from config import config

#Routes
from routes import Movie

app = Flask(__name__)

def page_not_found(error): #Opicional
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(Movie.main, url_prefix='/api/movies') #Quando coloque essa rota, vai imprimir o que está em Movie.py, para todas as API'S

    app.register_error_handler(404, page_not_found) #Está sendo listado na web page
    app.run()