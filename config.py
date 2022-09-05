class Config(object):
    #put any configuration here that are common across the all env
    SECRET_KEY='ABC14'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:user@localhost:3306/python'
    SQLALCHEMY_TRACK_MODIFICATION=False

class DevelopmentConfig(Config):
    #development configuration
    DEBUG=True
    SLQALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATION=False

#
# class ProductionConfig(Config):
#     #development configuration
#
#     DEBUG=True
# class TestingConfig(Config):
#     #tessting configuration
#
#     DEBUG=True
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:user@localhost:3306/python'
#     SQLALCHEMY_TRACK_MODIFICATION = False

app_config={
    'development':DevelopmentConfig,
    # 'testing':TestingConfig,
    # 'production':ProductionConfig
}