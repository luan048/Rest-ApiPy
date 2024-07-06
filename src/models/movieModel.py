from database.db import get_connection
from .entities.movie import Movie

class MovieModel():

    @classmethod
    def get_movie(self): #Esse é o params

        try:
            connection = get_connection()
            movies=[]

            with connection.cursor() as cursor: #Conector com DB
                cursor.execute("SELECT id, title, duration, released FROM filmes ORDER BY title ASC")

                resultset=cursor.fetchall() # Pega todas as linhas do DB

                for row in resultset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())

            connection.close()
            return movies
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_oneMovie(cls, movie_id):  # Certifique-se de usar 'cls' como primeiro parâmetro
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, duration, released FROM filmes WHERE id = %s", (movie_id, ))
                row = cursor.fetchone()  # Pega uma única linha do DB

                movie = None
                if row is not None:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movie = movie.to_JSON()

            connection.close()
            return movie

        except Exception as ex:
            raise Exception(ex)

        
    @classmethod
    def add_movie(cls, movie):

        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO filmes (id, title, duration, released) VALUES (%s, %s, %s, %s)', (movie.id, movie.title, movie.duration, movie.released))

                affected_rows = cursor.rowcount # Quantas linhas foram alteradas no DB
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)