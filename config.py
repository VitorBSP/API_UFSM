class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://api_ufsm:admin@localhost:5432/ufsm_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'studing-api-fundamentals' #'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']