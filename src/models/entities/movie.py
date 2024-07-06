from utils.dateFormate import DateFormat

class Movie():

    def __init__(self, id, title, duration, released):
        self.id = id
        self.title = title
        self.duration = duration
        self.released = released

    def to_JSON(self): # Controla tudo que vai ser impresso formato JSON na API
        
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'released': DateFormat.convert_date(self.released)
        }