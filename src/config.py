from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG=True #Quando existe mudaça, server reinicia sozinho

config={
    'development': DevelopmentConfig
}