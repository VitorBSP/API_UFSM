class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://api_ufsm:admin@localhost:5432/ufsm_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False