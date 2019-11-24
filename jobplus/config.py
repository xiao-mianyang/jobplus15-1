class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''
    INDEX_PER_PAGE = 9
    AMIN_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/jobplus?charset=utf8'


class ProductConfig(BaseConfig):

    pass


class TestingConfig(BaseConfig):

    pass


configs = {
        'development':DevelopmentConfig,
        'production':ProductConfig,
        'testing':TestingConfig
        
        }
