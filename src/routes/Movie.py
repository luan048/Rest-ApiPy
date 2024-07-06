from flask import Blueprint, jsonify, request
import uuid

from models.entities.movie import Movie

#Models
from models.movieModel import MovieModel

main=Blueprint('movie_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_movie():

    try:
        movie = MovieModel.get_movie()
        return jsonify(movie)

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<movie_id>', methods=['GET'])
def get_oneMovie(movie_id):

    try:
        movie = MovieModel.get_oneMovie(movie_id)
        
        if movie is not None:
            return jsonify(movie), 200  # Retorna o filme de acordo com o id
        else:
            return jsonify({'message': 'Not Found'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


    
@main.route('/', methods=['POST'])
def add_movie():

    try:
        data = request.json

        title = data.get('title')
        duration = data.get('duration')
        released = data.get('released')
        
        id = uuid.uuid4()

        movie = Movie(str(id), title, duration, released)

        affected_rows = MovieModel.add_movie(movie) #Armazena os dados da API no movie

        if affected_rows:
            return jsonify({'message': 'Sucessfully'}), 201

        else:
            return jsonify({'message': 'Failed'}), 500        

    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500