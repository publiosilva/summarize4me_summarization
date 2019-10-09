class ProductionConfig():
    DEBUG = False
    ENV = 'production'


class DevelopmentConfig():
    DEBUG = True
    ENV = 'development'


class TestingConfig():
    TESTING = True